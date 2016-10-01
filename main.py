import numpy as np
import math
from sklearn.cluster import KMeans


def Calcurate_W(data):
    # temp data
    temp = []
    W_ = []

    # calcurate distance
    for i in range(len(data)):
        for j in range(len(data)):
            temp.append(np.linalg.norm(data[i] - data[j]))
        W_.append(temp)
        temp = []

    W = np.array(W_)
    return W

def Calcurate_D(W):
    temp = np.sum(W, axis=1)
    D = np.diag(temp)
    return D

    
if __name__ == '__main__':
    data = np.loadtxt('data_set/test.csv', delimiter=',')
    W = Calcurate_W(data)
    D = Calcurate_D(W)

    L = D - W

    la, V = np.linalg.eig(L)

    print W
    print D
    print L
    print la
    print V
