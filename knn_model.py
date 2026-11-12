import csv
import itertools
import numpy as np
from data_preprocessing import load_data

# Minkowski distance formula
def minkowski(x, v, p=2.0):
    return np.sum(np.abs(x - v) ** p) ** (1.0 / p)

class KNN: 
    def __init__(self, p=2.0): 
        # We removed k from here because we will pass a list of k's directly
        self.p = p 

    def fit(self, x_train, y_train):  
        self.x_train = x_train  
        self.y_train = y_train  

    def predict_multiple_k(self, x_test, k_candidates):  
        #this returns a dictionary of predictions for every k at the same time
        all_preds = {k: [] for k in k_candidates} 
        max_k = max(k_candidates)

        for point in x_test: 
            dists = np.sum(np.abs(self.x_train - point) ** self.p, axis=1) 
            
            #this sorts distances once and grab the max amount of neighbors we could possibly need
            k_idx_max = np.argsort(dists)[:max_k] 
            
            #this instantly distribute the votes for every k candidate without recalculating distance
            for k in k_candidates:
                k_labels = self.y_train[k_idx_max[:k]] 
                counts = np.bincount(k_labels) 
                all_preds[k].append(np.argmax(counts))  
                
        #thusi converts all prediction lists to numpy arrays
        return {k: np.array(preds) for k, preds in all_preds.items()}

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
    
    #thsi evaluate on a 5000 sample test slice for fast optimization search
    sub_test_len = min(1000, len(x_test))
    sub_test_x = x_test[:sub_test_len]
    sub_test_y = y_test[:sub_test_len]
    
    #this stores every single result here to sort them later
    all_results = []
    
    #this loops through ALL combinations
    for i, combo in enumerate(all_feature_combos):
        
        # Prints an update to your console every 50 combinations
        if i % 50 == 0:
            print(f"Testing combination {i} out of {len(all_feature_combos)}...")
            
        x_tr_sub = x_train[:, combo]
        x_te_sub = sub_test_x[:, combo]
        
        #this nitializes and fit the model once per feature combination
        model = KNN(p=2.0)
        model.fit(x_tr_sub, y_train)
        
        #this gets predictions for all k candidates 
        preds_dict = model.predict_multiple_k(x_te_sub, k_candidates)
        
        for k in k_candidates:
            preds = preds_dict[k]
            tp, fp, tn, fn, eval_acc, prec, rec, f1 = compute_metrics(sub_test_y, preds)
            
            #this saves the result details to our list
            all_results.append({
                'f1': f1,
                'combo': combo,
                'k': k,
                'preds': preds,
                'metrics': (tp, fp, tn, fn, eval_acc, prec, rec, f1)
            })
                
    print(f"Testing combination {len(all_feature_combos)} out of {len(all_feature_combos)}... DONE!\n")
    
    #this sorts all results by F1-Score in descending order (highest to lowest)
    all_results.sort(key=lambda x: x['f1'], reverse=True)
    
    #this grabs the top 3
    top_3_results = all_results[:3]
    
    print("==========================================================")
    print(" TOP 3 CONFIGURATIONS FOUND")
    print("==========================================================")
    
    for rank, res in enumerate(top_3_results, 1):
        combo = res['combo']
        k = res['k']
        tp, fp, tn, fn, eval_acc, prec, rec, f1 = res['metrics']
        
        selected_feature_names = [feature_names[i] for i in combo]
        
        print(f"\n--- RANK {rank} ---")
        print(f"Total Features Selected : {len(selected_feature_names)}")
        print(f"Features Selected       : {selected_feature_names}")
        print(f"Best k                  : {k}")
        metrics_summary(f"RANK {rank} MODEL", tp, fp, tn, fn, eval_acc, prec, rec, f1)
    
    #this pulls the predictions from the absolute best model (Rank 1) to show incorrect samples
    best_res = top_3_results[0]
    best_preds = best_res['preds']
    
    #this prints sample incorrect classifications for the best model
    print("Sample Incorrect Classifications (Absolute Best Model):")
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