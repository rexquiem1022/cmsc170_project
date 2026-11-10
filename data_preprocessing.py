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
            municipalities.add(row.get('Municipality', '').strip())
            
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
                                                                     
if __name__ == "__main__":  
    path = "political_dynasty.csv" 
    print_dataset_statistics(path)
    x_train, y_train, x_test, y_test = load_data(path)  
    print("Train shape:",x_train.shape, "Test shape:", x_test.shape)
