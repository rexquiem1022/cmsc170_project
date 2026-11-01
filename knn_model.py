import numpy as np
from data_preprocessing import load_data

def minkowski(x, v, p=2.0): 
    return np.sum(np.abs(x-v)**p)**(1.0 / p)  

class KNN: 
    def __init__(self, k=5, p=2.0): 
        self.k = k  
        self.p = p 

    def fit(self, x_train, y_train):  
        self.x_train = x_train  
        self.y_train = y_train  

    def predict(self, x_test):  
        preds = []  
        for point in x_test: 
            dists = np.sum(np.abs(self.x_train-point)**self.p, axis=1)**(1.0 / self.p) 
            k_idx = np.argsort(dists)[:self.k] 
            k_labels = self.y_train[k_idx] 
            counts = np.bincount(k_labels) 
            preds.append(np.argmax(counts))  
        return np.array(preds) 

def compute_metrics(y_true, y_pred):
    tp = np.sum((y_true==1) & (y_pred==1))
    fp = np.sum((y_true==0) & (y_pred==1))
    tn = np.sum((y_true==0) & (y_pred==0))
    fn = np.sum((y_true==1) & (y_pred==0))
    total = len(y_true)
    if total > 0:
        acc =(tp+tn)/total
    else:
        acc = 0.0

    prec_den = tp + fp
    if prec_den > 0:
        prec =tp/prec_den
    else:
        prec = 0.0

    recall_den = tp + fn
    if recall_den > 0:
        rec =tp/recall_den
    else:
        rec=0.0

    f1_den = prec + rec
    if f1_den>0:
        f1 = 2*(prec *rec)/f1_den
    else:
        f1 = 0.0

    return tp, fp, tn, fn, acc, prec, rec, f1

def metrics_summary(model_name, tp, fp, tn, fn,acc,prec, rec, f1): 

    print(f" EVALUATION SUMMARY: {model_name.upper()}") 
    print(f"True Positives (TP/Hit): {tp}") 
    print(f"False Positives (FP/False Alarm): {fp}") 
    print(f"True Negatives (TN/Correct Reject): {tn}")  
    print(f"False Negatives (FN/Miss): {fn}")  
    print(f"Accuracy: {acc*100:.2f}%") 
    print(f"Precision: {prec*100:.2f}%") 
    print(f"Recall: {rec*100:.2f}%")
    print(f"F1-Score: {f1*100:.2f}%")

if __name__ == "__main__":
    path = "political_dynasty.csv"
    x_train, y_train, x_test, y_test = load_data(path)

    model = KNN(k=5, p=2.0)
    model.fit(x_train, y_train)

    sub_test_x = x_test[:500]
    sub_test_y = y_test[:500]
    preds = model.predict(sub_test_x)

    correct = np.sum(preds==sub_test_y)
    total = len(sub_test_y)
    acc = (correct/total)*100

    print("KNN CLASSIFICATION RESULTS")
    print("k =",model.k)
    print("p =",model.p)
    print("Correct predictions:",correct)
    print("Incorrect predictions:",total-correct)
    print("Accuracy:", f"{acc:.2f}%\n")

    tp, fp, tn, fn, eval_acc, prec, rec, f1 = compute_metrics(sub_test_y, preds)
    metrics_summary("KNN", tp, fp, tn, fn, eval_acc, prec, rec, f1)

    print("Incorrect Classifications")
    print(f"{'Data Record #':<14} | {'Actual':<10} | {'Predicted':<10}")
    incorrect=np.where(preds != sub_test_y)[0]
    label_map={1: "fat", 0: "non-fat"}


    train_len = len(x_train)
    for i in incorrect[:15]:
        rec_num=train_len+i+1
        act =label_map[sub_test_y[i]]
        pred =label_map[preds[i]]
        print(f"{rec_num:<14} | {act:<10} | {pred:<10}")