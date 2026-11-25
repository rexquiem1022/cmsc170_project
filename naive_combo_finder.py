import itertools
import numpy as np

from naive_bayes_model import *

# ------------------------------------------------------------------ CONFIG
MIN_COMBO_SIZE = 0      # Smallest number of features in a combination (0 = empty set, class prior only)
MAX_COMBO_SIZE = None   # Largest number of features in a combination (None = all features)
N_SPLITS = 5            # 80/20 split: 1 of 5 grouped folds (20%) is the test set, the other 4 (80%) train
RANK_BY = "f1"          # f1 score ranking
TOP = 10                # get top 10 best combos

# same domain rules used in data_preprocessing.load_data
EXEC_KEYWORDS = ["GOVERNOR", "MAYOR", "CONGRESSMAN", "REPRESENTATIVE", "HOUSE"]
MAJOR_PARTIES = ["PDP-LABAN", "LAKAS", "LIBERAL", "NACIONALISTA", "NPC", "UNA"]


# =============================================================================
# 1. Build all 9 candidate features as integer category codes
# =============================================================================
'''
    Builds every candidate feature as integer category codes.
    Extracts the stripped Position, Party, Region, Province, and Municipality.City text columns from the rows.
    Stores the 0/1 flags as the strings '0' and '1' so that all nine features pass through the same factorize routine.
    Parameter rows: The balanced row dictionaries.
    Returns: A dictionary mapping each of the nine feature names to a (codes, categories) tuple from factorize.
'''
def build_all_features(rows):
    pos = [r["Position"].strip() for r in rows]
    party = [r["Party"].strip() for r in rows]
    reg = [r["Region"].strip() for r in rows]
    prov = [r["Province"].strip() for r in rows]
    muni = [r["Municipality.City"].strip() for r in rows]

    raw = {
        "Position": pos,
        "Party": party,
        "Region": reg,
        "Province": prov,
        "Municipality.City": muni,
        "Tenure": [r["tenure"] for r in rows],      # from naive_model add_tenure()
        "Is_Executive": [str(int(any(k in p.upper() for k in EXEC_KEYWORDS))) for p in pos],
        "Location_Combined": [f"{pr}_{mu}" for pr, mu in zip(prov, muni)],
        "Is_Major_Party": [str(int(any(m in p.upper() for m in MAJOR_PARTIES))) for p in party],
    }
    return {name: factorize(vals) for name, vals in raw.items()}   # name (codes, categories)


# =============================================================================
# 2. Evaluate one feature combination with grouped K-fold
# =============================================================================
'''
    Scores one combination of features with grouped cross validation.
    Stacks the chosen feature columns into one matrix and records the number of categories of each.
    Handles an empty combination by giving the model zero feature columns, so it predicts from the class prior alone.
    Trains one NaiveBayes model on the training rows (80%) and predicts the held out test rows (20%), thresholding at THRESHOLD.
    Computes the metrics on the test rows only, so the model is never scored on data it was trained on, and every combination is judged on the same rows.
    Parameters tr and te: The train and test row positions, computed once with group_kfold and reused for every combination.
    Returns: A dictionary with the keys features, tp, fp, tn, fn, acc, prec, rec, and f1.
'''
def evaluate_combo(names, feats, y, tr, te, k):
    X = (np.column_stack([feats[n][0] for n in names]) if names
         else np.empty((len(y), 0), dtype=np.int64))      # Empty set: zero feature columns
    n_cats = [len(feats[n][1]) for n in names]

    model = NaiveBayes(n_cats, k).fit(X[tr], y[tr])                           # Fit on the 80% training rows only
    y_pred = (model.predict_proba(X[te]) >= THRESHOLD).astype(np.int64)       # Predict the 20% test rows

    # Metrics use the held-out test rows only
    tp, fp, tn, fn, acc, prec, rec, f1 = compute_metrics(y[te], y_pred)
    return {"features": names, "tp": tp, "fp": fp, "tn": tn, "fn": fn,
            "acc": acc, "prec": prec, "rec": rec, "f1": f1}


# =============================================================================
# 3. Main
# =============================================================================
if __name__ == "__main__": # Runs on execution
    rows = load_balanced_rows(DATA_PATH)                 # Balanced 50/50, tenure included
    y = np.array([int(float(r[TARGET_COL] or 0)) for r in rows], dtype=np.int64)
    groups, _ = factorize([r[GROUP_COL] for r in rows])
    feats = build_all_features(rows)
    tr, te = next(group_kfold(groups, N_SPLITS))         # 80/20 split by last name (same as run_model), computed once and reused for every combo

    all_names = list(feats.keys())
    max_size = len(all_names) if MAX_COMBO_SIZE is None else min(MAX_COMBO_SIZE, len(all_names))
    # Exhaustive search: every subset of every size from MIN_COMBO_SIZE up to max_size
    combos = [c for size in range(MIN_COMBO_SIZE, max_size + 1)
              for c in itertools.combinations(all_names, size)]
    print(f"Loaded {len(rows):,} balanced records  |  fat rate {y.mean():.1%}")
    print(f"Testing {len(combos)} combinations of {MIN_COMBO_SIZE} to {max_size} features out of {len(all_names)} "
          f"(k={K_SMOOTHING}, threshold={THRESHOLD})")
    print(f"Train: {len(tr):,} records ({len(tr) / len(rows):.0%}, fat rate {y[tr].mean():.1%})  |  "
          f"Test: {len(te):,} records ({len(te) / len(rows):.0%}, fat rate {y[te].mean():.1%})  |  grouped by {GROUP_COL}\n")

    # King of the hill type to minimize high volume sorting
    top = []                                             # always sorted best-first
    for names in combos:
        r = evaluate_combo(names, feats, y, tr, te, K_SMOOTHING)

        # Keep r if there is room, or it strictly beats the current worst survivor.
        # Strict ">" means a result that merely ties 10th place does not displace it.
        if (TOP is None or len(top) < TOP
                or (r[RANK_BY], r["acc"]) > (top[-1][RANK_BY], top[-1]["acc"])):
            top.append(r)
            top.sort(key=lambda x: (x[RANK_BY], x["acc"]), reverse=True)   # Stable: earlier combos win ties
            if TOP is not None:
                del top[TOP:]                            # Drop anything past position TOP

    results = top

    # Top 10 leaderboard
    shown = results if TOP is None else results[:TOP]
    print(f"TOP {len(shown)} COMBINATIONS (ranked by {RANK_BY.upper()})")
    label_of = lambda r: " + ".join(r["features"]) or "(no features: class prior only)"   # Empty set is the baseline
    w = max(45, max(len(label_of(r)) for r in shown))   # Features column width, grows for big combos
    print(f"{'#':<3} | {'Features':<{w}} | {'Acc':>7} | {'Prec':>7} | {'Recall':>7} | {'F1':>7}")
    print("-" * (w + 45))
    for i, r in enumerate(shown, 1):
        label = label_of(r)
        print(f"{i:<3} | {label:<{w}} | {r['acc']:>7.2%} | {r['prec']:>7.2%} | "
              f"{r['rec']:>7.2%} | {r['f1']:>7.2%}")

    # Top 1 details
    best = results[0]
    print("\nBEST COMBINATION:", label_of(best))
    metrics_summary("Naive Bayes (best combo)", best["tp"], best["fp"], best["tn"], best["fn"],
                    best["acc"], best["prec"], best["rec"], best["f1"])
    print_confusion_matrix(best["tp"], best["fp"], best["tn"], best["fn"])