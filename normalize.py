import numpy as np
import math


def softmax(u):
    e = np.exp(u)
    return e / np.sum(e)

data = np.loadtxt("data_set/normalize.csv", delimiter=",")

for i in range(len(data)):
    temp = softmax(data)
    print temp
