import textwrap
import numpy as np
import matplotlib.pyplot as plt
from naive_bayes_model import DATA_PATH, NaiveBayes, THRESHOLD, K_SMOOTHING, load_balanced_rows, compute_metrics
from naive_combo_finder import build_all_features
from perceptron import Perceptron, load_features, min_errors, NB_TOP3

# Plots for Method 2 (perceptron on the top 3 Naive Bayes feature sets).
# Perceptron and Naive Bayes are both trained and tested on the SAME grouped split, so the bars are comparable.

BLUE, ORANGE, GRAY = "#0072b2", "#e69f00", "#999999"


# this trains Naive Bayes on the same train/test split as the perceptron and returns its metrics
def nb_metrics(feature_names, nb_feats, y, tr, te):
    Xc = np.column_stack([nb_feats[n][0] for n in feature_names])       # integer category codes
    n_cats = [len(nb_feats[n][1]) for n in feature_names]
    model = NaiveBayes(n_cats, K_SMOOTHING).fit(Xc[tr], y[tr])
    pred = (model.predict_proba(Xc[te]) >= THRESHOLD).astype(int)
    return compute_metrics(y[te], pred)


if __name__ == "__main__":
    X, y, groups, tr, te, names = load_features()
    nb_feats = build_all_features(load_balanced_rows(DATA_PATH))        # same rows, same order as X

    labels = [f"Top {i}" for i in range(1, len(NB_TOP3) + 1)]
    titles = [textwrap.fill(" + ".join(f), 30) for f in NB_TOP3]        # feature set text, wrapped for the plot
    p_res, n_res, train_err, min_err = [], [], [], []

    for feats in NB_TOP3:
        cols = [names.index(f) for f in feats]
        model = Perceptron().fit(X[tr][:, cols], y[tr])                 # this trains a fresh perceptron
        p_res.append(compute_metrics(y[te], model.predict(X[te][:, cols])))
        n_res.append(nb_metrics(feats, nb_feats, y, tr, te))
        train_err.append(int(np.sum(model.predict(X[tr][:, cols]) != y[tr])))   # train mistakes of the final weights
        min_err.append(min_errors(X[tr][:, cols], y[tr]))               # unavoidable mistakes with these features

    # ---------------- Figure 1: confusion matrices of the perceptron ----------------
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.6))
    for ax, lab, title, res in zip(axes, labels, titles, p_res):
        tp, fp, tn, fn = res[:4]
        cm = np.array([[tn, fp], [fn, tp]])
        ax.imshow(cm, cmap="Blues", vmin=0, vmax=cm.max() * 1.15)   # scale from 0 so shades match the counts
        for (i, j), v in np.ndenumerate(cm):                            # this writes the count inside each cell
            ax.text(j, i, f"{v:,}", ha="center", va="center", fontsize=13, fontweight="bold",
                    color="white" if v > cm.max() * 0.6 else "black")
        ax.set_xticks([0, 1]); ax.set_xticklabels(["Pred non-fat", "Pred fat"])
        ax.set_yticks([0, 1]); ax.set_yticklabels(["Actual non-fat", "Actual fat"])
        ax.set_title(f"{lab}\n{title}", fontsize=9, fontweight="bold")
    fig.suptitle("Perceptron Confusion Matrices (test set)", fontweight="bold")
    plt.tight_layout()
    plt.savefig("perceptron_confusion_matrices.png", dpi=300)

    # ---------------- Figure 2: train mistakes vs unavoidable mistakes ----------------
    x = np.arange(len(labels)); w = 0.38
    plt.figure(figsize=(8, 4.5))
    plt.bar(x - w / 2, train_err, w, color=BLUE, label="Mistakes of final weights")
    plt.bar(x + w / 2, min_err, w, color=ORANGE, label="Unavoidable mistakes (best possible)")
    for xi, a, b in zip(x, train_err, min_err):                         # this prints the counts above the bars
        plt.text(xi - w / 2, a, f"{a:,}", ha="center", va="bottom", fontsize=9)
        plt.text(xi + w / 2, b, f"{b:,}", ha="center", va="bottom", fontsize=9)
    plt.xticks(x, labels)
    plt.ylabel(f"Training mistakes (out of {len(tr):,})", fontweight="bold")
    plt.title("Why the Perceptron Cannot Converge", fontweight="bold")
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig("perceptron_mistakes.png", dpi=300)

    # ---------------- Figure 3: perceptron vs Naive Bayes ----------------
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    for ax, idx, name in zip(axes, (4, 7), ("Accuracy (%)", "F1-Score (%)")):   # index 4 = acc, 7 = f1
        pv = [r[idx] * 100 for r in p_res]
        nv = [r[idx] * 100 for r in n_res]
        ax.bar(x - w / 2, pv, w, color=BLUE, label="Perceptron")
        ax.bar(x + w / 2, nv, w, color=ORANGE, label="Naive Bayes")
        for xi, a, b in zip(x, pv, nv):
            ax.text(xi - w / 2, a, f"{a:.1f}", ha="center", va="bottom", fontsize=9)
            ax.text(xi + w / 2, b, f"{b:.1f}", ha="center", va="bottom", fontsize=9)
        if idx == 4:
            ax.axhline(50, color=GRAY, linestyle="--", linewidth=1.5, label="50% (chance on balanced data)")
        ax.set_xticks(x); ax.set_xticklabels(labels)
        ax.set_ylabel(name, fontweight="bold"); ax.set_ylim(0, 100)
        ax.grid(axis="y", linestyle="--", alpha=0.4)
        ax.legend(loc="upper right", fontsize=8)
    fig.suptitle("Perceptron vs Naive Bayes on the Same Feature Sets and Test Split", fontweight="bold")
    plt.tight_layout()
    plt.savefig("perceptron_vs_bayes.png", dpi=300)

    print("Saved: perceptron_confusion_matrices.png, perceptron_mistakes.png, perceptron_vs_bayes.png")
    for lab, p, n in zip(labels, p_res, n_res):
        print(f"{lab}: perceptron acc {p[4]:.2%} F1 {p[7]:.2%} | naive bayes acc {n[4]:.2%} F1 {n[7]:.2%}")
    plt.show()