import numpy as np

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