import csv
import numpy as np

# ------------------------------------------------------------------ CONFIG
DATA_PATH = "political_dynasty.csv"   # training CSV
K_SMOOTHING = 1.0                     # smoothing factor (1 = Laplace)
THRESHOLD = 0.5                     
SHOW = 15                             # Alter to change # of printed incorrect classifications
									# None to show all

TARGET_COL = "fat"
GROUP_COL = "Last Name"          # family proxy: used only to keep relatives together
VAR_COLS = ["Position", "tenure", "Province"]


# =============================================================================
# 1. Load the CSV, derive tenure, integer-code the categorical columns
# =============================================================================
def load_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def add_tenure(rows): # Derived from year of serving
    key = lambda r: (r["First Name"].strip(), r["Last Name"], r["Province"])
    years = {}
    for r in rows:
        years.setdefault(key(r), set()).add(r["Year"])
    for r in rows:
        r["tenure"] = str(len(years[key(r)]))


def factorize(values):
    cats = sorted(set(values))
    lookup = {c: i for i, c in enumerate(cats)}
    return np.array([lookup[v] for v in values], dtype=np.int64), cats


def prepare(rows):
    y = np.array([int(r[TARGET_COL]) for r in rows], dtype=np.int64)
    groups, _ = factorize([r[GROUP_COL] for r in rows])
    cols = VAR_COLS
    feats = {c: factorize([r[c] for r in rows]) for c in cols}
    return feats, y, groups


# =============================================================================
# 2. Grouped K-fold (relatives always stay in the same fold)
# =============================================================================
def group_kfold(groups, n_splits):
    sizes = np.bincount(groups)
    fold_of_group = np.zeros(len(sizes), dtype=np.int64)
    fold_sizes = np.zeros(n_splits, dtype=np.int64)
    for g in np.argsort(sizes, kind="stable")[::-1]:   # largest groups first
        f = int(np.argmin(fold_sizes))                 # lightest fold so far
        fold_of_group[g] = f
        fold_sizes[f] += sizes[g]
    fold = fold_of_group[groups]
    for i in range(n_splits):
        yield np.where(fold != i)[0], np.where(fold == i)[0]   # (train_idx, test_idx)


# =============================================================================
# 3. Main Naive-Bayes + smoothing process
# =============================================================================
class NaiveBayes:
    def __init__(self, n_cats, k=1.0):
        self.n_cats, self.k = n_cats, k

    def fit(self, X, y):
        self.log_prior = np.log(np.bincount(y, minlength=2) / len(y))
        self.log_lik = []                                  # per feature: (2, n_categories)
        for i in range(X.shape[1]):
            n_c = self.n_cats[i]
            table = np.zeros((2, n_c))
            for c in (0, 1):
                counts = np.bincount(X[y == c, i], minlength=n_c)
                table[c] = np.log((counts + self.k) / (counts.sum() + self.k * n_c))
            self.log_lik.append(table)
        return self

    def predict_proba(self, X):
        logp = np.tile(self.log_prior, (X.shape[0], 1))
        for i, table in enumerate(self.log_lik):
            logp += table[:, X[:, i]].T
        return 1.0 / (1.0 + np.exp(np.clip(logp[:, 0] - logp[:, 1], -50, 50)))



# =============================================================================
# 4. Confusion metrics for evaluation + suited threshold tuning
# =============================================================================
def compute_metrics(y_true, y_pred):
    tp = int(np.sum((y_true == 1) & (y_pred == 1)))
    fp = int(np.sum((y_true == 0) & (y_pred == 1)))
    tn = int(np.sum((y_true == 0) & (y_pred == 0)))
    fn = int(np.sum((y_true == 1) & (y_pred == 0)))
    total = len(y_true)
    acc = (tp + tn) / total if total > 0 else 0.0
    prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0
    return tp, fp, tn, fn, acc, prec, rec, f1


def metrics_summary(model_name, tp, fp, tn, fn, acc, prec, rec, f1):
    print(f"\nEVALUATION SUMMARY: {model_name.upper()} \n")
    print(f"True Positives (TP/Hit): {tp}")
    print(f"False Positives (FP/False Alarm): {fp}")
    print(f"True Negatives (TN/Correct Reject): {tn}")
    print(f"False Negatives (FN/Miss): {fn}")
    print(f"Accuracy: {acc * 100:.2f}%")
    print(f"Precision: {prec * 100:.2f}%")
    print(f"Recall: {rec * 100:.2f}%")
    print(f"F1-Score: {f1 * 100:.2f}%")


def print_confusion_matrix(tp, fp, tn, fn):
    w = 14  
    print(f"{'':<16}{'Pred non-fat':>{w}}{'Pred fat':>{w}}")
    print(f"{'Actual non-fat':<16}{'TN = ' + format(tn, ','):>{w}}{'FP = ' + format(fp, ','):>{w}}")
    print(f"{'Actual fat':<16}{'FN = ' + format(fn, ','):>{w}}{'TP = ' + format(tp, ','):>{w}}")


# =============================================================================
# 5. Run model
# =============================================================================
def run_model(rows, feats, y, groups, k, show):
    cols = VAR_COLS
    X = np.column_stack([feats[c][0] for c in cols])
    n_cats = [len(feats[c][1]) for c in cols]

    # 80/20 split by last name (fold 0 of 5 is the test set)
    tr, te = next(group_kfold(groups, 5))

    model = NaiveBayes(n_cats, k).fit(X[tr], y[tr])
    proba = model.predict_proba(X[te])
    flagged = proba >= THRESHOLD                       # the model's "fat" calls
    y_te = y[te]

    n_flag = int(flagged.sum())
    right = int(np.sum(flagged & (y_te == 1)))

    print(f"NAIVE-BAYES MODEL")
    print(f"Features          : {', '.join(cols)}")
    print(f"k (smoothing)     : {k}")
    print(f"Threshold         : {THRESHOLD:.2f}  (fixed; flag fat when P(fat) >= {THRESHOLD:.2f})")
    print(f"Training records  : {len(tr):,}   (fat rate {y[tr].mean():.1%})")
    print(f"Test records      : {len(te):,}   (fat rate {y_te.mean():.1%})")
    print(f"Flagged as fat    : {n_flag:,} of {len(te):,} test records")
    print(f"  Correct (actually fat)     : {right:,}")
    print(f"  Incorrect (actually non-fat): {n_flag - right:,}\n")

    tp, fp, tn, fn, acc, prec, rec, f1 = compute_metrics(y_te, flagged.astype(np.int64))
    metrics_summary(f"Naive Bayes", tp, fp, tn, fn, acc, prec, rec, f1)
    print_confusion_matrix(tp, fp, tn, fn)

    # ---- incorrect classifications: flagged fat, but actually non-fat
    wrong = np.where(flagged & (y_te == 0))[0]
    print(f"\n Incorrect Fat Calls out of {len(wrong):,}")
    print(f"{'CSV Row #':<10} | {'Name':<28} | {'Province':<20} | {'Position':<22} | "
          f"{'Actual':<8} | {'Predicted':<9} | P(fat)")
    for j in wrong[:show]:
        r = rows[te[j]]
        name = f"{r['First Name'].strip()} {r['Last Name']}"[:28]
        print(f"{te[j] + 2:<10} | {name:<28} | {r['Province'][:20]:<20} | "
              f"{r['Position'][:22]:<22} | {'non-fat':<8} | {'fat':<9} | {proba[j]:.3f}")



if __name__ == "__main__":
    rows = load_csv(DATA_PATH)
    add_tenure(rows)
    feats, y, groups = prepare(rows)
    print(f"Loaded {len(rows):,} records from {DATA_PATH}  |  fat rate {y.mean():.1%}")
    run_model(rows, feats, y, groups, K_SMOOTHING, SHOW)