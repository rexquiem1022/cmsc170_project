import csv  
import numpy as np

def encode_list(lst):
    vals = sorted(list(set(lst)))
    mapping = {v: i for i, v in enumerate(vals)}
    return np.array([mapping[v] for v in lst], dtype=float)

def load_data(file_path):  
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
    y = np.array(y,dtype=int)

    return x,y

if __name__ == "__main__":  
    path = "political_dynasty.csv" 
    x, y = load_data(path)  
    print(x.shape, y.shape)  
