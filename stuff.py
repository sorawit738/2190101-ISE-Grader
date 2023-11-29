import numpy as np

def all_pair_distances(points):
    # points are array
    n = len(points)
    X = points[:, 0]
    Y = points[:, 1]
    dx = X - X.reshape(n, 1)
    dy = Y - Y.reshape(n, 1)
    D = (dx**2+dy**2)**0.5
    return D

def all_pair_distances2(points):
    # points are nested list, e.g., [[0,0],[0,3],[4,0]]
    n = len(points)
    D = [[0.0] * n for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            D[i][j] = D[j][i] = (dx**2+dy**2)**0.5

    return D

points = np.array([[0, 0], [0, 3], [4, 0]])

print(all_pair_distances(points))
print(all_pair_distances2([[0, 0], [0, 3], [4, 0]]))