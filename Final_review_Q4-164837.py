import numpy as np
def f2(a):
  # !!! YOUR CODE HERE !!!
  return a[::2,1::2].reshape(1,-1)

# main
a = np.array([x for x in input().split()])
r,c = [int(x) for x in input().split()]
a = a.reshape(r,c)
print(f2(a))