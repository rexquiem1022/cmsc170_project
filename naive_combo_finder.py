import itertools
import numpy as np

from naive_bayes_model import *

# ------------------------------------------------------------------ CONFIG
COMBO_SIZE = 2          # Features to be chosen
N_SPLITS = 5            # grouped K-fold (relatives stay in the same fold)
RANK_BY = "f1"          # f1 score ranking
TOP = 10                # get top 10 best combos

# same domain rules used in data_preprocessing.load_data
EXEC_KEYWORDS = ["GOVERNOR", "MAYOR", "CONGRESSMAN", "REPRESENTATIVE", "HOUSE"]
MAJOR_PARTIES = ["PDP-LABAN", "LAKAS", "LIBERAL", "NACIONALISTA", "NPC", "UNA"]


# =============================================================================
# 1. Build all 9 candidate features as integer category codes
# =============================================================================
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
def evaluate_combo(names, feats, y, folds, k):
    X = np.column_stack([feats[n][0] for n in names])
    n_cats = [len(feats[n][1]) for n in names]

    y_pred = np.zeros(len(y), dtype=np.int64)
    for tr, te in folds:
        model = NaiveBayes(n_cats, k).fit(X[tr], y[tr])
        y_pred[te] = (model.predict_proba(X[te]) >= THRESHOLD).astype(np.int64)

    # every row is in exactly one test fold, so y_pred holds out-of-fold predictions for all rows
    tp, fp, tn, fn, acc, prec, rec, f1 = compute_metrics(y, y_pred)
    return {"features": names, "tp": tp, "fp": fp, "tn": tn, "fn": fn,
            "acc": acc, "prec": prec, "rec": rec, "f1": f1}


# =============================================================================
# 3. Main
# =============================================================================
if __name__ == "__main__":
    rows = load_balanced_rows(DATA_PATH)                 # balanced 50/50, tenure included
    y = np.array([int(float(r[TARGET_COL] or 0)) for r in rows], dtype=np.int64)
    groups, _ = factorize([r[GROUP_COL] for r in rows])
    feats = build_all_features(rows)
    folds = list(group_kfold(groups, N_SPLITS))          # computed once, reused for every combo

    all_names = list(feats.keys())
    combos = list(itertools.combinations(all_names, COMBO_SIZE))
    print(f"Loaded {len(rows):,} balanced records  |  fat rate {y.mean():.1%}")
    print(f"Testing {len(combos)} combinations of {COMBO_SIZE} from {len(all_names)} features "
          f"({N_SPLITS}-fold grouped CV, k={K_SMOOTHING}, threshold={THRESHOLD})\n")

    results = []
    for names in combos:
        results.append(evaluate_combo(names, feats, y, folds, K_SMOOTHING))

    results.sort(key=lambda r: (r[RANK_BY], r["acc"]), reverse=True)

    # ---- ranking table
    shown = results if TOP is None else results[:TOP]
    print(f"TOP {len(shown)} COMBINATIONS (ranked by {RANK_BY.upper()})")
    print(f"{'#':<3} | {'Features':<45} | {'Acc':>7} | {'Prec':>7} | {'Recall':>7} | {'F1':>7}")
    print("-" * 90)
    for i, r in enumerate(shown, 1):
        label = " + ".join(r["features"])
        print(f"{i:<3} | {label:<45} | {r['acc']:>7.2%} | {r['prec']:>7.2%} | "
              f"{r['rec']:>7.2%} | {r['f1']:>7.2%}")

    # ---- full detail for the winner
    best = results[0]
    print("\nBEST COMBINATION:", " + ".join(best["features"]))
    metrics_summary("Naive Bayes (best combo)", best["tp"], best["fp"], best["tn"], best["fn"],
                    best["acc"], best["prec"], best["rec"], best["f1"])
    print_confusion_matrix(best["tp"], best["fp"], best["tn"], best["fn"])