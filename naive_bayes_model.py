import csv
import numpy as np
from data_preprocessing import *

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

'''
    Reads a CSV file from disk and returns its rows as dictionaries.
    Opens the file with the utf-8-sig encoding so that a leading byte order mark, which spreadsheet exports often add, is dropped instead of polluting the first column name.
    Uses newline='' as the csv module recommends, so that line breaks embedded inside quoted fields are handled correctly.
    Parses every row with csv.DictReader, so each record is keyed by the column names found in the header line.
    Every value is returned as a raw string, and no type conversion or cleaning happens here.
    Parameter path: The file system path of the CSV file to read.
    Returns: A list of dictionaries, one per data row, mapping each column name to its string value.
'''
def load_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))



'''
    Adds a tenure value to every row, counting the distinct years the same politician appears in.
    Identifies a politician by the combination of first name, last name, and province, because the data has no unique person identifier.
    Collects the set of distinct Year values found for each of those identities, so repeated rows for the same year are counted only once.
    Writes the size of that set back onto every row of the same politician under the new key tenure, stored as a string so that factorize can later treat it as a category.
    Only the first name is stripped of whitespace in the identity key, so a last name with stray spaces would be treated as a different politician.
    Modifies the rows in place and returns nothing.
    This must run before any balancing or undersampling, otherwise removed rows would shrink the year counts and produce wrong tenure values.
    Parameter rows: The list of row dictionaries produced by load_csv, which is mutated in place.
    Returns: Nothing.
'''
def add_tenure(rows): # Derived from year of serving
    key = lambda r: (r["First Name"].strip(), r["Last Name"], r["Province"])
    years = {}
    for r in rows:
        years.setdefault(key(r), set()).add(r["Year"])
    for r in rows:
        r["tenure"] = str(len(years[key(r)]))


'''
    Loads the dataset and returns a class balanced (50/50) subset of its rows.
    Reads the CSV through load_csv and tags every row with the key _row, the original line number in the file, where the header is line 1 and the first data row is line 2, so rows can be traced back after balancing.
    Derives tenure with add_tenure before any rows are removed, which keeps the year counts correct.
    Builds the target vector from the TARGET_COL column, treating empty values as 0 and converting through float so that values such as 1.0 are accepted.
    Passes the row indices and targets to undersample_5050, imported from data_preprocessing, which selects the indices to keep so that both classes are equally represented, using the seed for reproducibility.
    Returns the kept rows in their original order, because the kept indices are sorted before they are used.
    Returns: A list of row dictionaries forming the balanced dataset.
'''

def load_balanced_rows(path, seed=42):
    rows = load_csv(path)
    for i, r in enumerate(rows):
        r["_row"] = i + 2                      # original CSV row number
    add_tenure(rows)                           # BEFORE balancing, or tenure counts get wrong
    y = np.array([int(float(r[TARGET_COL] or 0)) for r in rows])
    keep, _ = undersample_5050(np.arange(len(rows)), y, seed=seed)
    return [rows[i] for i in sorted(keep)]     # balanced 50/50 rows


'''
    Converts a list of categorical values into integer codes.
    Builds the sorted list of unique values, so code 0 belongs to the first category in sorted order and the mapping is the same on every run.
    Creates a lookup from each category to its position in that list and uses it to encode every input value.
    The integer codes are what the Naive Bayes count tables use as indices.
    Parameter values: A list of hashable and mutually sortable values, such as strings.
    Returns: A tuple of a numpy int64 array of codes, aligned with the input, and the sorted list of categories, where categories[code] recovers the original value.
'''

def factorize(values):
    cats = sorted(set(values))
    lookup = {c: i for i, c in enumerate(cats)}
    return np.array([lookup[v] for v in values], dtype=np.int64), cats


'''
    Builds the feature codes, the targets, and the family groups from the loaded rows.
    Creates the target vector y from TARGET_COL by converting each value directly with int, so unlike load_balanced_rows it expects no empty values.
    Factorizes GROUP_COL, the last name, into integer group ids, which are used only to keep relatives together when splitting and never as a feature.
    Factorizes every column listed in VAR_COLS and stores the codes and categories in a dictionary keyed by column name.
    Parameter rows: The balanced row dictionaries, which must already contain the tenure key.
    Returns: A tuple of feats (a dictionary of column name to a (codes, categories) tuple), y (the int64 target array), and groups (the int64 group id array).
'''
def prepare(rows):
    y = np.array([int(r[TARGET_COL]) for r in rows], dtype=np.int64)
    groups, _ = factorize([r[GROUP_COL] for r in rows])
    cols = VAR_COLS
    feats = {c: factorize([r[c] for r in rows]) for c in cols}
    return feats, y, groups


# =============================================================================
# 2. Grouped K-fold (relatives always stay in the same fold)
# =============================================================================
'''
    Yields train and test index splits in which every group stays inside a single fold.
    Counts the rows in every group with bincount.
    Goes through the groups from largest to smallest and assigns each one to the fold that is currently the lightest, a greedy strategy that keeps the folds close to equal in size.
    Because all rows of a family share one group, relatives never appear on both sides of a split, which prevents leakage through matching surnames.
    The assignment is deterministic and uses no randomness.
    Is a generator, so the splits are produced lazily, one per fold, and callers that need them repeatedly should wrap the call in list, as the combo finder does.
    Parameter groups: An integer array of group ids, one per row, such as the output of factorize on the last names.
    Parameter n_splits: The number of folds to create.
    Yields: A tuple of (train_idx, test_idx), both numpy arrays of row positions, once per fold.
'''
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
'''
    Categorical Naive Bayes classifier for a binary target with additive smoothing.
    Treats every feature as an integer coded category and assumes the features are independent given the class.
    Learns a log prior and one log likelihood table per feature during fit, and combines them by addition in log space during prediction.
    Uses additive smoothing, where a smoothing constant of 1 gives Laplace smoothing, so a category never seen in a class does not receive a probability of zero.
'''
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
# 4. Metrics Computation & Summary
# =============================================================================

'''    
    Computes the confusion matrix counts and the standard classification metrics.
    Counts true positives, false positives, true negatives, and false negatives by comparing the true and predicted labels, where 1 is the positive (fat) class.
    Derives accuracy, precision, recall, and the F1 score from those counts.
    Guards every ratio against division by zero and falls back to 0.0.
    Returns: confusion matrix data and its derived values
'''

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


'''
    Provides a metric summary for the confusion matrix and its derived values
'''
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


'''
    Prints the confusion matrix as a small table.
    Uses the actual classes as rows and the predicted classes as columns, with TN and FP in the first row and FN and TP in the second.
'''
def print_confusion_matrix(tp, fp, tn, fn):
    w = 14  
    print(f"{'':<16}{'Pred non-fat':>{w}}{'Pred fat':>{w}}")
    print(f"{'Actual non-fat':<16}{'TN = ' + format(tn, ','):>{w}}{'FP = ' + format(fp, ','):>{w}}")
    print(f"{'Actual fat':<16}{'FN = ' + format(fn, ','):>{w}}{'TP = ' + format(tp, ','):>{w}}")


# =============================================================================
# 5. Main model run
# =============================================================================
'''
    Trains the Naive Bayes model on a single grouped split and prints a full report.
    Stacks the columns listed in VAR_COLS into a feature matrix and collects the number of categories of each.
    Fits the model on the training part and flags a test row as fat when its predicted probability reaches THRESHOLD.
    Prints the settings, the record counts, the fat rate of each part, and how many flags were correct and incorrect.
    Prints the metrics and the confusion matrix through metrics_summary and print_confusion_matrix.
'''
def run_model(rows, feats, y, groups, k, show):
    cols = VAR_COLS
    X = np.column_stack([feats[c][0] for c in cols])
    n_cats = [len(feats[c][1]) for c in cols]

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

    # Flagged fat but non-fat counts
    wrong = np.where(flagged & (y_te == 0))[0]
    print(f"\n Incorrect Fat Calls out of {len(wrong):,}")
    print(f"{'CSV Row #':<10} | {'Name':<28} | {'Province':<20} | {'Position':<22} | "
          f"{'Actual':<8} | {'Predicted':<9} | P(fat)")
    for j in wrong[:show]:
        r = rows[te[j]]
        name = f"{r['First Name'].strip()} {r['Last Name']}"[:28]
        print(f"{r['_row']:<10} | {name:<28} | {r['Province'][:20]:<20} | "
            f"{r['Position'][:22]:<22} | {'non-fat':<8} | {'fat':<9} | {proba[j]:.3f}")



if __name__ == "__main__": # Runs on execution
    rows = load_balanced_rows(DATA_PATH)       # was: load_data(...) + add_tenure(rows)
    feats, y, groups = prepare(rows)
    print(f"Loaded {len(rows):,} records from {DATA_PATH}  |  fat rate {y.mean():.1%}")
    run_model(rows, feats, y, groups, K_SMOOTHING, SHOW)