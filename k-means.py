import numpy as np
import math
from sklearn.cluster import KMeans

if __name__ == '__main__':
    file = open('data_set/10_percent_kddcup.data')
    c_label = open('data_set/train_label.data')
    t_label = c_label.read().split('\n')
    t_data = file.read().split('\r\n')
    temp_data = []
    data = []
    test = [0 for i in range(23)]

    for i in t_data:
        temp_data.append(i.split(','))
    temp_data.pop()
    temp_data.pop()

    for i in temp_data:
        data.append(map(float, i))

    train_data = np.array(data)
    cluster_num = 23
    kmeans_model = KMeans(n_clusters=cluster_num, random_state=10).fit(train_data)

    labels = kmeans_model.labels_

    correct = 0.0
    f_to_a = 0.0
    a_to_f = 0.0
    for i in range(len(labels)):
        if t_label[i] == 'normal.':
            if labels[i] == 17:
                correct += 1.0
            else:
                a_to_f += 1.0
        else:
            if labels[i] != 17:
                correct += 1.0
            else:
                f_to_a += 1.0

    accuracy = correct / len(labels) * 100
    f_positive = a_to_f / len(labels) * 100
    f_negative = f_to_a/ len(labels) * 100
    print "accuracy = %3f %%" % accuracy
    print "false positive = %3f %%" % f_positive
    print "false negative = %3f %%" % f_negative
