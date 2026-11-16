import numpy as np
from data_preprocessing import load_data

# Perceptron Convergence Algorithm
#   x(n) = [1, x1, ..., xm]        (x0 = +1 is the fixed bias input)
#   w(0) = 0
#   y(n) = sgn(w(n)^T x(n))        (hard limiter)
#   w(n+1) = w(n) + eta * [d(n) - y(n)] * x(n)
#   d(n) = +1 for class C1 (fat), -1 for class C2 (non-fat)


def sgn(v):
    # +1 if v > 0 and -1 if v < 0; v == 0 is not defined,
    # so we send it to -1 here.
    return 1 if v > 0 else -1


class Perceptron:
    def __init__(self, eta=0.1, max_epochs=50):
        self.eta = eta                  # learning rate, 0 < eta < 1
        self.max_epochs = max_epochs    # stop even if it never converges
        self.epochs_run = 0
        self.converged = False

    def fit(self, x_train, y_train):
        # Step 1: add x0 = +1 to every input, set w(0) = 0
        ones = np.ones((x_train.shape[0], 1))
        x = np.hstack((ones, x_train))
        d = np.where(y_train == 1, 1, -1)       # desired response: fat -> +1, non-fat -> -1
        self.w = np.zeros(x.shape[1])

        for epoch in range(self.max_epochs):
            changed = False
            for n in range(len(x)):
                y = sgn(np.dot(self.w, x[n]))                   # Step 3: actual response
                if y != d[n]:
                    self.w = self.w + self.eta * (d[n] - y) * x[n]   # Step 4: adapt weights
                    changed = True
            self.epochs_run = epoch + 1
            if not changed:                     # weights no longer change -> converged
                self.converged = True
                break

    def predict(self, x_test):
        ones = np.ones((x_test.shape[0], 1))
        x = np.hstack((ones, x_test))
        v = x @ self.w
        return np.where(v > 0, 1, 0)            # back to 1 = fat, 0 = non-fat


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
    print(f"EVALUATION SUMMARY: {model_name.upper()}")
    print(f"True Positives (TP/Hit): {tp}")
    print(f"False Positives (FP/False Alarm): {fp}")
    print(f"True Negatives (TN/Correct Reject): {tn}")
    print(f"False Negatives (FN/Miss): {fn}")
    print(f"Accuracy: {acc * 100:.2f}%")
    print(f"Precision: {prec * 100:.2f}%")
    print(f"Recall: {rec * 100:.2f}%")
    print(f"F1-Score: {f1 * 100:.2f}%")

FEATURES = ["Position", "Party", "Region", "Province"]   # baseline features
# FEATURES = ['Position', 'Municipality', 'Location_Combined']   # searched features


def load_features(path):
    """load_data's output without the Tenure column (Tenure is not used)."""
    x_train, y_train, x_test, y_test, names = load_data(path)
    keep = [i for i, n in enumerate(names) if n != "Tenure"]
    return x_train[:, keep], y_train, x_test[:, keep], y_test, [names[i] for i in keep]


if __name__ == "__main__":
    path = "political_dynasty.csv"
    x_train, y_train, x_test, y_test, feature_names = load_features(path)

    cols = [feature_names.index(n) for n in FEATURES]
    x_train, x_test = x_train[:, cols], x_test[:, cols]

    model = Perceptron(eta=0.1, max_epochs=50)
    model.fit(x_train, y_train)
    preds = model.predict(x_test)

    print("PERCEPTRON CLASSIFICATION RESULTS")
    print("eta =", model.eta)
    print("Epochs run:", model.epochs_run)
    print("Converged:", model.converged)
    print("Features:", FEATURES)
    print("Weights [bias, " + ", ".join(n.lower() for n in FEATURES) + "]:", np.round(model.w, 3))

    correct = np.sum(preds == y_test)
    total = len(y_test)
    print("Correct predictions:", correct)
    print("Incorrect predictions:", total - correct)
    print(f"Accuracy: {correct / total * 100:.2f}%\n")

    tp, fp, tn, fn, acc, prec, rec, f1 = compute_metrics(y_test, preds)
    metrics_summary("Perceptron", tp, fp, tn, fn, acc, prec, rec, f1)

    # reference: F1 of a model that always predicts "fat"
    p_fat = y_test.mean()
    print(f"\nAlways-'fat' baseline F1: {2 * p_fat / (1 + p_fat) * 100:.2f}%")