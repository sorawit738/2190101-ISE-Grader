import numpy as np

def toCelsius(f):
    return (f - 32) * (5 / 9)

def BMI(wh):
    return wh[:,0] / (((wh[:,1]) / 100) ** 2)

def distanceTo(p, Points):
    return ((Points - p)[:, 0] ** 2 + (Points - p)[:,1] ** 2) ** 0.5

exec(input().strip())
