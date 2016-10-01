import numpy as np
import math
from sklearn.cluster import KMeans


def Calcurate_W(data):
    # temp data
    temp = []
    W_ = []

    for i in range(len(data)):
        for j in range(len(data)):
            temp.append(np.linalg.norm(data[i] - data[j]))
        W_.append(temp)
        temp = []

    W = np.array(W_)
    return W

if __name__ == '__main__':
    data = np.loadtxt('data_set/normalize.csv', delimiter=',')
    Calcurate_distance(data)
