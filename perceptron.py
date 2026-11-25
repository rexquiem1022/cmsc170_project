import numpy as np
from naive_bayes_model import (DATA_PATH, TARGET_COL, GROUP_COL, load_balanced_rows,
                               factorize, group_kfold, compute_metrics, metrics_summary)
from naive_combo_finder import build_all_features

# Perceptron Convergence Algorithm:
#   x = [1, x1..xm], w(0) = 0, y = sgn(w.x), w <- w + eta * (d - y) * x, d = +1 fat / -1 non-fat

# this trains the weights using the perceptron convergence algorithm
def _train(X, d, eta, max_epochs):
    w = np.zeros(X.shape[1])                                # w(0) = 0, one weight per column (bias included)
    for epoch in range(max_epochs):                         # one epoch = one full pass over the training data
        changed = False                                     # this tracks if any weight was updated in this pass
        for n in range(len(X)):
            y = 1 if (w * X[n]).sum() > 0 else -1          # sgn(w.x); sgn(0) -> -1
            if y != d[n]:                                   # this only updates the weights when the prediction is wrong
                w += eta * (d[n] - y) * X[n]
                changed = True
        if not changed:                                     # a full pass with no mistakes means it converged
            return w, epoch + 1, True
    return w, max_epochs, False                             # this stops at max_epochs even if it never converged


class Perceptron:
    def __init__(self, eta=0.1, max_epochs=50):
        self.eta, self.max_epochs = eta, max_epochs         # learning rate and the epoch limit

    def fit(self, X, y):
        X = np.hstack((np.ones((len(X), 1)), X))           # x0 = +1 bias input
        d = np.where(y == 1, 1, -1)                        # fat -> +1, non-fat -> -1
        self.w, self.epochs_run, self.converged = _train(X, d, self.eta, self.max_epochs)
        return self

    def predict(self, X):
        # this adds the bias column, computes w.x for every row, then converts back to 1 = fat, 0 = non-fat
        return (np.hstack((np.ones((len(X), 1)), X)) @ self.w > 0).astype(int)


def load_features(path=DATA_PATH):
    """Same balanced rows and 9 features as Naive Bayes; family-grouped train/test split."""
    rows = load_balanced_rows(path)                         # this loads the 50/50 balanced rows with tenure
    feats = build_all_features(rows)                        # this builds the 9 features as integer codes
    names = list(feats)
    cols = [feats[n][0].astype(float) for n in names]       # this takes only the codes of each feature
    cols[names.index("Tenure")] = np.array([float(r["tenure"]) for r in rows])   # numeric, not string-sorted codes
    X = np.column_stack(cols)                               # this combines the 1D arrays into one 2D matrix
    span = X.max(0) - X.min(0)
    X = (X - X.min(0)) / np.where(span == 0, 1, span)      # min-max to [0, 1]; avoids dividing by zero on constant columns
    y = np.array([int(r[TARGET_COL]) for r in rows])        # target: fat = 1, non-fat = 0
    groups, _ = factorize([r[GROUP_COL] for r in rows])     # family group id per row (last name)
    tr, te = next(group_kfold(groups, 5))        # relatives never split across train/test
    return X, y, groups, tr, te, names


def min_errors(X, y):
    """Fewest training mistakes ANY classifier can make: identical feature rows with mixed labels."""
    _, inv = np.unique(X, axis=0, return_inverse=True)      # this gives the same number to rows with identical features
    inv = inv.ravel()
    fat, total = np.bincount(inv, weights=y), np.bincount(inv)   # fat count and total count of each identical-row group
    return int(np.minimum(fat, total - fat).sum())          # the smaller label in each group is always wrong


def report(title, feature_names, names, model, X_tr, y_tr, X_te, y_te):
    cols = [names.index(f) for f in feature_names]          # this converts feature names to column positions
    pred = model.predict(X_te[:, cols])                     # this predicts on the test set using only those columns
    print(f"\n{title}\nFeatures: {feature_names}")
    print(f"Epochs run: {model.epochs_run} | Converged: {model.converged} | Predicted fat: {pred.mean():.1%}")
    print("Weights [bias, " + ", ".join(feature_names) + "]:", np.round(model.w, 3))
    metrics_summary("Perceptron", *compute_metrics(y_te, pred))   # this prints the confusion matrix values and metrics
    mistakes = int(np.sum(model.predict(X_tr[:, cols]) != y_tr))  # this counts wrong predictions on the training set
    print(f"Train mistakes of final weights: {mistakes:,}/{len(y_tr):,} | "
          f"unavoidable with these features: {min_errors(X_tr[:, cols], y_tr):,}")


# Method 2: top 3 feature sets from naive_combo_finder.py
NB_TOP3 = [
    ["Position", "Region", "Province", "Tenure"],
    ["Position", "Region", "Province", "Tenure", "Is_Major_Party"],
    ["Region", "Tenure"],
]

if __name__ == "__main__":
    X, y, groups, tr, te, names = load_features()
    print(f"Train {len(tr):,} | Test {len(te):,} | test fat rate {y[te].mean():.1%}")
    for i, feats in enumerate(NB_TOP3, 1):
        cols = [names.index(f) for f in feats]              # columns of the current feature set
        model = Perceptron().fit(X[tr][:, cols], y[tr])     # this trains a fresh perceptron on the train rows only
        report(f"METHOD 2 - NAIVE BAYES TOP {i}", feats, names, model, X[tr], y[tr], X[te], y[te])