import csv  
import numpy as np
from collections import Counter

# this converts text categories into numbers so that the model can easily process it
def encode_list(lst):
    vals = sorted(list(set(lst))) #this gets the unique values using set() 
    mapping = {v: i for i, v in enumerate(vals)} #this helps on creating a dictionary assigning an integer to the unique text value
    return np.array([mapping[v] for v in lst], dtype=float) #returned as numpy array adn replaces the list with the new list

def print_dataset_statistics(file_path):
    y_counts = Counter()
    positions = set()
    parties = set()
    regions = set()
    provinces = set()
    municipalities = set()
    total_records = 0
    
    with open(file_path, mode='r', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_records += 1
            target = int(float(row.get('fat', 0) or 0))
            y_counts[target] += 1
            positions.add(row.get('Position', '').strip())
            parties.add(row.get('Party', '').strip())
            regions.add(row.get('Region', '').strip())
            provinces.add(row.get('Province', '').strip())
            municipalities.add(row.get('Municipality.City', '').strip())
            
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
    print(f"Unique Municipalities: {len(municipalities)}")
                       

def undersample_5050(x, y, seed=42):
    np.random.seed(seed)
    fat_indices = np.where(y == 1)[0]
    non_fat_indices = np.where(y == 0)[0]
    
    n_fat = len(fat_indices)
    selected_non_fat = np.random.choice(non_fat_indices, size=n_fat, replace=False)
    
    balanced_indices = np.concatenate([fat_indices, selected_non_fat])
    np.random.shuffle(balanced_indices)
    
    return x[balanced_indices], y[balanced_indices]
                                              
def load_data(file_path, split_ratio=0.8, seed=42):
    np.random.seed(seed)
    pos, party, reg, prov, muni = [], [], [], [], []
    tenure = []
    y = []
    
    with open(file_path, mode='r', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # this extracts the target variable 
            target = int(float(row.get('fat', 0) or 0))
            y.append(target)
            
            # extract features
            pos.append(row.get('Position', '').strip())
            party.append(row.get('Party', '').strip())
            reg.append(row.get('Region', '').strip())
            prov.append(row.get('Province', '').strip())
            muni.append(row.get('Municipality', '').strip())
            
            raw_tenure = row.get('Tenure', row.get('tenure', 0.0))
            try:
                t_val = float(raw_tenure) if raw_tenure != '' else 0.0
            except ValueError:
                t_val = 0.0
            tenure.append(t_val)
            
    # converting text to integers
    e_pos = encode_list(pos)
    e_party = encode_list(party)
    e_reg = encode_list(reg)
    e_prov = encode_list(prov)
    e_muni = encode_list(muni)
    e_tenure = np.array(tenure, dtype=float)
    
    # Reliable Domain-Engineered Features
    exec_keywords = ["GOVERNOR", "MAYOR", "CONGRESSMAN", "REPRESENTATIVE", "HOUSE"]
    is_exec = np.array([1.0 if any(k in p.upper() for k in exec_keywords) else 0.0 for p in pos], dtype=float)
    
    loc_combined = [f"{pr}_{mu}" for pr, mu in zip(prov, muni)]
    e_loc_combined = encode_list(loc_combined)
    
    major_parties = ["PDP-LABAN", "LAKAS", "LIBERAL", "NACIONALISTA", "NPC", "UNA"]
    is_major_party = np.array([1.0 if any(mp in pt.upper() for mp in major_parties) else 0.0 for pt in party], dtype=float)
    
    # this combines the separate 1D feature arrays into a single 2D matrix
    x = np.column_stack((
        e_pos, e_party, e_reg, e_prov, e_muni, e_tenure, is_exec, e_loc_combined, is_major_party
    ))
    y = np.array(y, dtype=int)
    
    # min-max scaling for normalization
    x_min = x.min(axis=0)
    x_max = x.max(axis=0)
    denom = np.where((x_max - x_min) == 0, 1.0, x_max - x_min)
    x_scaled = (x - x_min) / denom
    
    # Perform 50:50 Undersampling FIRST
    x_balanced, y_balanced = undersample_5050(x_scaled, y, seed=seed)
    
    n = len(y_balanced)
    idx = np.random.permutation(n) # this generates a randomly shuffled list of index numbers from 0 to n
    train_len = int(n * split_ratio) # first 80% for training, remaining 20% for testing
    train_idx = idx[:train_len]
    test_idx = idx[train_len:]
    
    x_train, y_train = x_balanced[train_idx], y_balanced[train_idx]
    x_test, y_test = x_balanced[test_idx], y_balanced[test_idx]
    
    feature_names = [
        "Position", "Party", "Region", "Province", 
        "Municipality", "Tenure", "Is_Executive", 
        "Location_Combined", "Is_Major_Party"
    ]
    
    return x_train, y_train, x_test, y_test, feature_names

if __name__ == "__main__":
    path = "political_dynasty.csv"
    print_dataset_statistics(path)
    x_train, y_train, x_test, y_test, feature_names = load_data(path)
    print("Balanced Train shape:", x_train.shape, "Balanced Test shape:", x_test.shape)
    print("Total Valid Features:", len(feature_names))
