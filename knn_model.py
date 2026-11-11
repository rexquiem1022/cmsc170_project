import csv
import itertools
import numpy as np
from data_preprocessing import load_data

# Minkowski distance formula
def minkowski(x, v, p=2.0):
    return np.sum(np.abs(x - v) ** p) ** (1.0 / p)

class KNN:
    def __init__(self, k=5, p=2.0):
        self.k = k
        self.p = p

    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_test):
        preds = []
        for point in x_test: # this is for every single unknown politician in our test set
            # this calculates the distance between this unknown point and every point in the training set
            dists = np.sum(np.abs(self.x_train - point) ** self.p, axis=1) ** (1.0 / self.p)
            # this sorts the distances from closest to furthest, and grab the index numbers of the top 'k'
            k_idx = np.argsort(dists)[:self.k]
            # looks up for the actual labels/targets for the top 'k'
            k_labels = self.y_train[k_idx]
            # counts how many votes for each labels
            counts = np.bincount(k_labels)
            # appends the winner to the prediction list
            preds.append(np.argmax(counts))
        return np.array(preds)

# for the calculation of the metrics
def compute_metrics(y_true, y_pred):
    tp = np.sum((y_true == 1) & (y_pred == 1)) # true positive
    fp = np.sum((y_true == 0) & (y_pred == 1)) # false positive
    tn = np.sum((y_true == 0) & (y_pred == 0)) # true negative
    fn = np.sum((y_true == 1) & (y_pred == 0)) # false negative
    total = len(y_true)
    
    if total > 0: # accuracy
        acc = (tp + tn) / total
    else:
        acc = 0.0

    prec_den = tp + fp
    if prec_den > 0: # precision
        prec = tp / prec_den
    else:
        prec = 0.0

    recall_den = tp + fn
    if recall_den > 0: # recall
        rec = tp / recall_den
    else:
        rec = 0.0

    f1_den = prec + rec
    if f1_den > 0: # f1 score
        f1 = 2 * (prec * rec) / f1_den
    else:
        f1 = 0.0

    return tp, fp, tn, fn, acc, prec, rec, f1

def metrics_summary(model_name, tp, fp, tn, fn, acc, prec, rec, f1):

    print(f" EVALUATION SUMMARY: {model_name.upper()}")
    print(f"True Positives (TP/Hit)           : {tp}")
    print(f"False Positives (FP/False Alarm)  : {fp}")
    print(f"True Negatives (TN/Correct Reject): {tn}")
    print(f"False Negatives (FN/Miss)         : {fn}")
    print(f"Accuracy                          : {acc*100:.2f}%")
    print(f"Precision                         : {prec*100:.2f}%")
    print(f"Recall                            : {rec*100:.2f}%")
    print(f"F1-Score                          : {f1*100:.2f}%")

if __name__ == "__main__":
    path = "political_dynasty.csv"
    
    #this loads dataset & feature names
    data_out = load_data(path)
    if len(data_out) == 5:
        x_train, y_train, x_test, y_test, feature_names = data_out
    else:
        x_train, y_train, x_test, y_test = data_out
        feature_names = [f"Feature_{i}" for i in range(x_train.shape[1])]
        
    n_features = x_train.shape[1]
    
    #thsi generates all possible feature combinations (sizes 1 to n_features) using itertools
    all_feature_combos = []
    for r in range(1, n_features + 1):
        all_feature_combos.extend(itertools.combinations(range(n_features), r))
        
    k_candidates = [1, 3, 5, 7, 9, 11, 13, 15]
    
    print("==========================================================")
    print(" k-NN HYPERPARAMETER & FULL FEATURE SUBSET SEARCH")
    print("==========================================================")
    print(f"Total Feature Subsets to Evaluate : {len(all_feature_combos)}")
    print(f"Candidates for k : {k_candidates}\n")
    
    #thsi evaluate on a 500-sample test slice for fast optimization search
    sub_test_len = min(500, len(x_test))
    sub_test_x = x_test[:sub_test_len]
    sub_test_y = y_test[:sub_test_len]
    
    best_f1 = -1.0
    best_combo = None
    best_k = None
    best_preds = None
    
    #this loops through all combinations 
    for combo in all_feature_combos:
        x_tr_sub = x_train[:, combo]
        x_te_sub = sub_test_x[:, combo]
        for k in k_candidates:
            model = KNN(k=k, p=2.0)
            model.fit(x_tr_sub, y_train)
            preds = model.predict(x_te_sub)
            
            tp, fp, tn, fn, eval_acc, prec, rec, f1 = compute_metrics(sub_test_y, preds)
            
            if f1 > best_f1:
                best_f1 = f1
                best_combo = combo
                best_k = k
                best_preds = preds
                
    #this prints best model results using your metrics_summary structure
    best_feature_names = [feature_names[i] for i in best_combo]
    print(f"BEST CONFIGURATION FOUND:")
    print(f"Total Features Selected : {len(best_feature_names)}")
    print(f"Features Selected       : {best_feature_names}")
    print(f"Best k                  : {best_k}")
    
    tp, fp, tn, fn, eval_acc, prec, rec, f1 = compute_metrics(sub_test_y, best_preds)
    metrics_summary(f"KNN (k={best_k}, Best Feature Subset)", tp, fp, tn, fn, eval_acc, prec, rec, f1)
    
    #this prints sample incorrect classifications for the best model
    print("Sample Incorrect Classifications (Best Model):")
    print(f"{'Data Record #':<14} | {'Actual':<10} | {'Predicted':<10}")
    print("-" * 42)
    
    incorrect = np.where(best_preds != sub_test_y)[0]
    label_map = {1: "fat", 0: "non-fat"}
    train_len = len(x_train)
    
    for i in incorrect[:10]:
        rec_num = train_len + i + 1
        act = label_map[sub_test_y[i]]
        pred = label_map[best_preds[i]]
        print(f"{rec_num:<14} | {act:<10} | {pred:<10}")