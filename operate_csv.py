import csv

with open("data_set/kddcup.data_10_percent", "rb") as r_file:
    with open("data_set/10_percent_kddcup.data", "w") as w_file:
        writer = csv.writer(w_file)
        temp = r_file.read().split("\n")
        data = []
        for i in temp:
            split_data = i.split(",")
            del split_data[1:4]
            data.append(split_data[:-1])
        writer.writerows(data)

        
            
    
