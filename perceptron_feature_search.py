import itertools
import numpy as np
from perceptron import Perceptron, compute_metrics, FEATURES, load_features

# Trained on the "best" features found by a search.
#
#   1. Try every subset of the features returned by load_data.
#   2. Train on 80% of the TRAIN data, score F1 on the other 20% (validation).
#      The test set is not used for choosing.
#   3. Train the baseline and the chosen subset on the full train data and
#      compare them once on the test set.

EPOCHS = 50
MIN_FAT, MAX_FAT = 0.10, 0.90    # skip subsets that predict one class for (almost) everyone


def run(cols, x_a, y_a, x_b, y_b):
    model = Perceptron(eta=0.1, max_epochs=EPOCHS)
    model.fit(x_a[:, cols], y_a)
    preds = model.predict(x_b[:, cols])
    tp, fp, tn, fn, acc, prec, rec, f1 = compute_metrics(y_b, preds)
    return f1, acc, rec, preds.mean()


if __name__ == "__main__":
    x_train, y_train, x_test, y_test, names = load_features("political_dynasty.csv")

    usable = list(range(len(names)))

    # split the train data into fit / validation
    cut = int(0.8 * len(y_train))
    x_fit, y_fit, x_val, y_val = x_train[:cut], y_train[:cut], x_train[cut:], y_train[cut:]

    print(f"Searching {2 ** len(usable) - 1} subsets of: {[names[i] for i in usable]}")
    best_f1, best_cols = -1.0, None
    for r in range(1, len(usable) + 1):
        for combo in itertools.combinations(usable, r):
            f1, acc, rec, fat_rate = run(list(combo), x_fit, y_fit, x_val, y_val)
            if MIN_FAT <= fat_rate <= MAX_FAT and f1 > best_f1:
                best_f1, best_cols = f1, list(combo)
    print("Best features (validation F1 %.2f%%):" % (best_f1 * 100), [names[i] for i in best_cols])

    # final comparison on the test set
    base_cols = [names.index(n) for n in FEATURES]
    p_fat = y_test.mean()
    print(f"\n{'':<10}{'F1':>8}{'Accuracy':>10}{'Recall':>9}{'Pred fat':>10}   Features")
    for label, cols in [("Baseline", base_cols), ("Searched", best_cols)]:
        f1, acc, rec, fr = run(cols, x_train, y_train, x_test, y_test)
        print(f"{label:<10}{f1:>8.2%}{acc:>10.2%}{rec:>9.2%}{fr:>10.1%}   {[names[i] for i in cols]}")
    print(f"Always-'fat' baseline F1: {2 * p_fat / (1 + p_fat):.2%}")