import csv  
import numpy as np

def encode_list(lst):
    vals = sorted(list(set(lst)))
    mapping = {v: i for i, v in enumerate(vals)}
    return np.array([mapping[v] for v in lst], dtype=float)

def load_data(file_path, split_ratio=0.8, seed=42): 

    np.random.seed(seed)

    pos = []  
    party = []  
    reg = []  
    prov = []  
    y = []  

    with open(file_path, mode='r', encoding='utf-8', errors='ignore') as f:  
        reader = csv.DictReader(f) 
        for row in reader:  
                target = int(float(row.get('fat', 0))) 
                pos.append(row.get('Position', '').strip()) 
                party.append(row.get('Party', '').strip()) 
                reg.append(row.get('Region', '').strip()) 
                prov.append(row.get('Province', '').strip()) 
                y.append(target)  

    e_pos = encode_list(pos)
    e_party = encode_list(party) 
    e_reg = encode_list(reg) 
    e_prov = encode_list(prov) 

    x = np.column_stack((e_pos, e_party, e_reg, e_prov))
    y = np.array(y, dtype=int)

    x_min = x.min(axis=0)
    x_max = x.max(axis=0)
    denom = np.where((x_max - x_min) == 0, 1.0, x_max - x_min)
    x_scaled = (x - x_min)/denom    

    n =len(y)
    idx =np.random.permutation(n)
    train_len = int(n*split_ratio)
    train_idx = idx[:train_len] 
    test_idx = idx[train_len:]

    x_train, y_train = x_scaled[train_idx], y[train_idx]
    x_test, y_test = x_scaled[test_idx], y[test_idx]

    return x_train, y_train, x_test, y_test
                                                                                        
if __name__ == "__main__":  
    path = "political_dynasty.csv" 
    x_train, y_train, x_test, y_test = load_data(path)  
    print("Train shape:",x_train.shape, "Test shape:", x_test.shape)
