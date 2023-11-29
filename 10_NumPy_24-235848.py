import numpy as np

def peak_indexes(x):
    temp = np.sign(np.diff(x))
    temp2 = np.diff(temp)
    results = np.arange(1,len(x)-1)
    return results[temp2 < -1]
def main():
    a = np.array([float(e) for e in input().split()])
    position = peak_indexes(np.array(a))
    if len(position) > 0:
        print(", ".join([str(e) for e in position]))
    else:
        print("No peaks")

exec(input().strip())