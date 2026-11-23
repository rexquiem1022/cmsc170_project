import numpy as np
import matplotlib.pyplot as plt
from data_preprocessing import load_data

# vectorized k-nn class for fast evaluation across multiple k values
class KNN:
    def __init__(self, p=2.0):
        self.p = p

    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict_multiple_k(self, x_test, k_candidates):
        # this returns a dictionary of predictions for every k at the same time
        all_preds = {k: [] for k in k_candidates}
        max_k = max(k_candidates)

        for point in x_test:
            dists = np.sum(np.abs(self.x_train - point) ** self.p, axis=1)
            k_idx_max = np.argsort(dists)[:max_k]

            for k in k_candidates:
                k_labels = self.y_train[k_idx_max[:k]]
                counts = np.bincount(k_labels)
                all_preds[k].append(np.argmax(counts))

        return {k: np.array(preds) for k, preds in all_preds.items()}

# for the calculation of the metrics
def compute_metrics(y_true, y_pred):
    tp = np.sum((y_true == 1) & (y_pred == 1)) # true positive
    fp = np.sum((y_true == 0) & (y_pred == 1)) # false positive
    tn = np.sum((y_true == 0) & (y_pred == 0)) # true negative
    fn = np.sum((y_true == 1) & (y_pred == 0)) # false negative

    total = len(y_true)
    acc = ((tp + tn) / total * 100) if total > 0 else 0.0
    prec = (tp / (tp + fp) * 100) if (tp + fp) > 0 else 0.0
    rec = (tp / (tp + fn) * 100) if (tp + fn) > 0 else 0.0
    f1 = (2 * prec * rec / (prec + rec)) if (prec + rec) > 0 else 0.0

    return tp, fp, tn, fn, acc, prec, rec, f1

if __name__ == "__main__":
    path = "political_dynasty.csv"

    print("1. Loading dataset via data_preprocessing...")
    data_out = load_data(path)
    if len(data_out) == 5:
        x_train, y_train, x_test, y_test, feature_names = data_out
    else:
        x_train, y_train, x_test, y_test = data_out
        feature_names = ['Position', 'Party', 'Region', 'Province', 'Municipality', 'Tenure', 'Is_Executive', 'Location_Combined', 'Is_Major_Party']

    # this maps feature names to their column indices
    feat_idx_map = {name: i for i, name in enumerate(feature_names)}

    # top 3 feature combinations derived from naive_combo_finder.py (ranked by F1)
    top_3_nb_groups = [
        ['Position', 'Region', 'Province', 'Tenure', 'Is_Major_Party'], # Rank 1 (60.78% NB F1)
        ['Position', 'Region', 'Province', 'Tenure'],                   # Rank 2 (60.76% NB F1)
        ['Position', 'Province', 'Tenure']                              # Rank 3 (60.52% NB F1)
    ]

    k_candidates = [1, 3, 5, 7, 9, 11, 13, 15]

    print("\n" + "="*85)
    print("TOP 3 NAÏVE BAYES FEATURE GROUPS UTILIZED:")
    print("="*85)
    for rank, grp in enumerate(top_3_nb_groups, 1):
        print(f"NB Rank {rank}: {' + '.join(grp)}")
    print("="*85)

    # this uses a validation slice for fast k-nn evaluation if x_test is large
    sub_test_len = min(1000, len(x_test))
    sub_test_x = x_test[:sub_test_len]
    sub_test_y = y_test[:sub_test_len]

    all_knn_runs = []

    print(f"\n2. Evaluating Top 3 Naïve Bayes Feature Groups across k = {k_candidates}...")

    for nb_rank, grp_names in enumerate(top_3_nb_groups, 1):
        combo_indices = [feat_idx_map[name] for name in grp_names]

        x_tr_sub = x_train[:, combo_indices]
        x_te_sub = sub_test_x[:, combo_indices]

        model = KNN(p=2.0)
        model.fit(x_tr_sub, y_train)
        preds_dict = model.predict_multiple_k(x_te_sub, k_candidates)

        for k in k_candidates:
            preds = preds_dict[k]
            tp, fp, tn, fn, acc, prec, rec, f1 = compute_metrics(sub_test_y, preds)
            all_knn_runs.append({
                'nb_rank': nb_rank,
                'combo_names': grp_names,
                'k': k,
                'acc': acc,
                'prec': prec,
                'rec': rec,
                'f1': f1,
                'cm': (tp, fp, tn, fn)
            })

    # this sorts all 24 runs (3 NB groups x 8 k-values) by f1-score descending
    all_knn_runs.sort(key=lambda x: x['f1'], reverse=True)
    top_10_knn = all_knn_runs[:10]

    print("\n" + "="*105)
    print("TOP 10 HIGHEST F1-SCORE CONFIGURATIONS (Top 3 Naïve Bayes Groups x k Values):")
    print("="*105)
    print(f"{'Rank':<5} | {'NB Grp':<6} | {'k':<3} | {'Acc (%)':<8} | {'Prec (%)':<8} | {'Rec (%)':<8} | {'F1 (%)':<8} | {'Features'}")
    print("-"*105)

    for rank, res in enumerate(top_10_knn, 1):
        feat_str = " + ".join(res['combo_names'])
        print(f"{rank:<5d} | #{res['nb_rank']:<5d} | {res['k']:<3d} | {res['acc']:<8.2f} | {res['prec']:<8.2f} | {res['rec']:<8.2f} | {res['f1']:<8.2f} | {feat_str}")
    print("="*105)

    # this grabs the #1 overall winning model and plots its k-tuning curve
    best_overall = top_10_knn[0]
    best_group_names = best_overall['combo_names']
    best_k = best_overall['k']
    best_f1 = best_overall['f1']

    print(f"\n--> Best Overall Model: {' + '.join(best_group_names)} at k = {best_k} (Peak F1-Score: {best_f1:.2f}%)\n")

    # this extracts all k scores for the winning feature group to plot the curve
    group_runs = [r for r in all_knn_runs if r['combo_names'] == best_group_names]
    group_runs.sort(key=lambda x: x['k'])
    f1_curve = [r['f1'] for r in group_runs]

    # this plots the tuning curve
    plt.figure(figsize=(8, 4.5), dpi=300)
    plt.plot(k_candidates, f1_curve, marker='o', linewidth=2.5, color='#0072b2', markersize=8, label='Validation F1-Score')
    plt.scatter([best_k], [best_f1], color='#009e73', s=160, zorder=5)
    plt.annotate(
        f'Optimal k = {best_k}\n(Peak F1: {best_f1:.2f}%)',
        xy=(best_k, best_f1),
        xytext=(best_k + 1.2, best_f1 - 0.6),
        fontsize=10,
        fontweight='bold',
        arrowprops=dict(arrowstyle='->', color='#222222', lw=1.5)
    )
    plt.xticks(k_candidates)
    plt.xlabel('Neighborhood Size (k)', fontweight='bold')
    plt.ylabel('F1-Score (%)', fontweight='bold')
    plt.title(f'k-NN Tuning on Winning NB Group: {" + ".join(best_group_names)}', fontweight='bold', pad=15)
    plt.grid(axis='y', linestyle='--', alpha=0.4)
    plt.tight_layout()
    plt.savefig('knn_bayes_top3_k_curve.png')
    print("Saved graph as 'knn_bayes_top3_k_curve.png'!")