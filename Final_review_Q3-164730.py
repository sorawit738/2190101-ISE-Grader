import numpy as np

def f1(d):
  x = len(d)//3
  y = len(d[0])//3
  dD = d[x:2*x, :y]
  dF = d[x:2*x, 2*y:]
  return dD - dF

a = np.array([int(x) for x in input().split()])
r,c = [int(x) for x in input().split()]
a = a.reshape(r,c)
print(f1(a))