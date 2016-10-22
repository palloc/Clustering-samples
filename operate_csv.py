import csv
import math

def Normalize(data):
    counter = [0 for i in range(len(data[0]))]
    for i in range(len(data)):
        for j in range(len(data[i])):
            counter[j] += float(data[i][j]) / len(data)
    variance = [0 for i in range(len(counter))]

    for i in range(len(counter)):
        for j in range(len(data)):
            variance[i] += (float(data[j][i])-counter[i])**2 / len(data)

    s_diviation = map(math.sqrt, variance)
    for i in range(len(s_diviation)):
        for j in range(len(data)):
            data[j][i] = str((float(data[j][i])-counter[i]) / s_diviation[i])

    return data
        
    
with open("data_set/kddcup.data_10_percent", "rb") as r_file:
    with open("data_set/10_percent_kddcup.data", "w") as w_file:
        writer = csv.writer(w_file)
        temp = r_file.read().split("\n")
        data = []
        for i in temp:
            split_data = i.split(",")
            del split_data[1:4], split_data[16:18]
            #w_file.write(split_data[-1]+"\n")
            data.append(split_data[:-1])
        data.pop()
        data.pop()
#        data = Normalize(data)
        writer.writerows(data)

        
