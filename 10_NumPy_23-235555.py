import numpy as np

def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight, data):
    a = data.shape[0]
    id = data[:, 0]
    scores = np.sum(data[:,1:],axis=0)/a
    mean = np.dot(scores, weight) / 3
    mean2 = np.sum(np.dot(data[:, 1:], weight).reshape((a, 1)), axis= 1) / 3
    if len(id[mean2 < mean]) == 0:
        print('None')
    else:
        print(', '.join([str(e) for e in id[mean2 < mean]]))
    pass

exec(input().strip())
