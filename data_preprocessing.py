import csv  
import numpy as np
from collections import Counter

# this converts text categories into numbers so that the model can easily process it
def encode_list(lst):
    vals = sorted(list(set(lst))) #this gets the unique values using set() 
    mapping = {v: i for i, v in enumerate(vals)} #this helps on creating a dictionary assigning an integer to the unique text value
    return np.array([mapping[v] for v in lst], dtype=float) #returned as numpy array adn replaces the list with the new list

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
                #this extracts the target variable 
                target = int(float(row.get('fat', 0))) 
                #extract features
                pos.append(row.get('Position', '').strip()) 
                party.append(row.get('Party', '').strip()) 
                reg.append(row.get('Region', '').strip()) 
                prov.append(row.get('Province', '').strip()) 
                y.append(target)  

     #converting test to integers
    e_pos = encode_list(pos)
    e_party = encode_list(party) 
    e_reg = encode_list(reg) 
    e_prov = encode_list(prov) 

    #this coombines the 4 separate 1D feature arrays into a single 2D matrix
    x = np.column_stack((e_pos, e_party, e_reg, e_prov))
    y = np.array(y, dtype=int)

    #min-max scaling for normalization
    x_min = x.min(axis=0)
    x_max = x.max(axis=0)
    denom = np.where((x_max - x_min) == 0, 1.0, x_max - x_min)
    x_scaled = (x - x_min)/denom    

    n =len(y)
    idx =np.random.permutation(n) #this generates a randomly shuffled list of index numbers from 0 to n
    train_len = int(n*split_ratio) #first 80% for training, remaining 20% for testing
    train_idx = idx[:train_len] 
    test_idx = idx[train_len:]

    x_train, y_train = x_scaled[train_idx], y[train_idx]
    x_test, y_test = x_scaled[test_idx], y[test_idx]

    return x_train, y_train, x_test, y_test

def print_dataset_statistics(file_path):
    y_counts = Counter()
    positions = set()
    parties = set()
    regions = set()
    provinces = set()
    total_records = 0

    with open(file_path, mode='r', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_records += 1
            target = int(float(row.get('fat', 0))) 
            y_counts[target] += 1
            
            positions.add(row.get('Position', '').strip())
            parties.add(row.get('Party', '').strip())
            regions.add(row.get('Region', '').strip())
            provinces.add(row.get('Province', '').strip())

    fat = y_counts[1]
    non_fat = y_counts[0]

    print(" EXPLORATORY DATA ANALYSIS (EDA) SUMMARY")
    print(f"Total Politicians (Records): {total_records}")
    print("TARGET VARIABLE DISTRIBUTION:")
    print(f"Fat Dynasties (1): {fat} records ({fat/total_records*100:.2f}%)")
    print(f"Non-Fat Dynasties (0): {non_fat} records ({non_fat/total_records*100:.2f}%)")
    print("FEATURE DIVERSITY (Unique Categories):")
    print(f"Unique Positions:{len(positions)}")
    print(f"Unique Parties:{len(parties)}")
    print(f"Unique Regions:{len(regions)}")
    print(f"Unique Provinces:{len(provinces)}")
                                                                     
if __name__ == "__main__":  
    path = "political_dynasty.csv" 
    print_dataset_statistics(path)
    x_train, y_train, x_test, y_test = load_data(path)  
    print("Train shape:",x_train.shape, "Test shape:", x_test.shape)
