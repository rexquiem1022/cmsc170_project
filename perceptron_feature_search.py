import itertools
import numpy as np
from naive_bayes_model import group_kfold, compute_metrics
from perceptron import Perceptron, load_features, report

# Method 1: best subset of the 2^9 - 1 = 511 non-empty feature subsets, chosen by validation F1.
# Train and validation come from the TRAIN part only (family-grouped); the test set is used once.
# A subset is only eligible if its validation accuracy beats the majority-class baseline.
# (On balanced data an "always fat" model scores F1 ~ 66.5% while learning nothing, so F1 alone
#  would reward it.)

if __name__ == "__main__":
    X, y, groups, tr, te, names = load_features()
    fit, val = next(group_kfold(groups[tr], 5))             # this splits the train part again, relatives stay together
    fit, val = tr[fit], tr[val]                             # this converts the positions back to the original row indices
    baseline = max(y[val].mean(), 1 - y[val].mean())        # accuracy of always guessing the larger class

    best = None                                    # (f1, acc, combo, model)
    for r in range(1, len(names) + 1):                      # this loops through every subset size, 1 to 9 features
        for combo in itertools.combinations(range(len(names)), r):   # this generates all subsets of that size
            c = list(combo)                                 # column positions of the current subset
            model = Perceptron().fit(X[fit][:, c], y[fit])  # this trains on the fit rows only
            *_, acc, _, _, f1 = compute_metrics(y[val], model.predict(X[val][:, c]))   # this scores on the validation rows
            if acc > baseline and (best is None or f1 > best[0]):   # this keeps the best F1 among subsets that beat the baseline
                best = (f1, acc, c, model)

    if best is None:                                        # this stops if no subset was better than the baseline
        raise SystemExit(f"No subset beat the {baseline:.2%} majority baseline.")
    f1, acc, c, model = best
    print(f"Best subset (val F1 {f1:.2%}, val acc {acc:.2%}, baseline {baseline:.2%})")
    # this scores the same model that earned the validation result on the test set, only once
    report("METHOD 1 - BEST SUBSET (test set, scored once)", [names[i] for i in c], names,
           model, X[fit], y[fit], X[te], y[te])