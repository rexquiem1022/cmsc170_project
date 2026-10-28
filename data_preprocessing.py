import csv  
 
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


    return pos, party, reg, prov, y 

if __name__ == "__main__":  
    path = "political_dynasty.csv" 
    pos, party, reg, prov, y = load_data(path)  
    print(len(y))  
