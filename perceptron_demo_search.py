import itertools
import random
import time
import numpy as np
from naive_bayes_model import group_kfold, compute_metrics
from perceptron import Perceptron, load_features, report

# DEMO of Method 1: same search as perceptron_feature_search.py, but only on a small random sample of subsets.
# N_COMBOS controls how many of the 511 subsets are tried (511 = the full search).

N_COMBOS = 3                                               # number of feature subsets to try
SEED = 42                                                   # same seed = same sample of subsets every run

if __name__ == "__main__":
    X, y, groups, tr, te, names = load_features()
    fit, val = next(group_kfold(groups[tr], 5))             # this splits the train part again, relatives stay together
    fit, val = tr[fit], tr[val]                             # this converts the positions back to the original row indices
    baseline = max(y[val].mean(), 1 - y[val].mean())        # accuracy of always guessing the larger class

    # this lists all 511 non-empty subsets, then picks a small random sample of them
    all_combos = [c for r in range(1, len(names) + 1)
                  for c in itertools.combinations(range(len(names)), r)]
    n = min(N_COMBOS, len(all_combos))
    sample = random.Random(SEED).sample(all_combos, n)

    print(f"DEMO: testing {n} of {len(all_combos)} subsets | baseline accuracy {baseline:.2%}\n")

    best = None                                             # (f1, acc, combo, model)
    start = time.time()
    for i, combo in enumerate(sample, 1):
        c = list(combo)                                     # column positions of the current subset
        model = Perceptron().fit(X[fit][:, c], y[fit])      # this trains on the fit rows only
        *_, acc, _, _, f1 = compute_metrics(y[val], model.predict(X[val][:, c]))   # this scores on the validation rows
        eligible = acc > baseline                           # only subsets that beat the baseline can win
        print(f"{i:>3}/{n} | F1 {f1:6.2%} | acc {acc:6.2%} | {'eligible' if eligible else 'skipped '} | "
              + " + ".join(names[j] for j in c))
        if eligible and (best is None or f1 > best[0]):     # this keeps the best F1 among eligible subsets
            best = (f1, acc, c, model)

    print(f"\nFinished in {time.time() - start:.1f} seconds")

    if best is None:                                        # this stops if no sampled subset beat the baseline
        raise SystemExit(f"No sampled subset beat the {baseline:.2%} majority baseline. Try a larger N_COMBOS.")
    f1, acc, c, model = best
    print(f"Best subset (val F1 {f1:.2%}, val acc {acc:.2%}, baseline {baseline:.2%})")
    # this scores the same model that earned the validation result on the test set, only once
    report("DEMO - BEST SUBSET (test set, scored once)", [names[i] for i in c], names,
           model, X[fit], y[fit], X[te], y[te])