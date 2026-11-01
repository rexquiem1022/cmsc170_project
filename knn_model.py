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

    print("Incorrect Classifications")
    print(f"{'Data Record #':<14} | {'Actual':<10} | {'Predicted':<10}")
    incorrect = np.where(preds != sub_test_y)[0]
    label_map = {1: "fat", 0: "non-fat"}

    train_len = len(x_train)
    for i in incorrect[:15]:
        rec_num=train_len+i+1
        act =label_map[sub_test_y[i]]
        pred =label_map[preds[i]]
        print(f"{rec_num:<14} | {act:<10} | {pred:<10}")