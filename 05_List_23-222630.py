def findIndex(arr : list[float], target : float) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def partition(x : list[float], p : int, r : int) -> int:
    temp = x[r]
    i = p - 1
    for j in range(p, r):
        if x[j] <= temp:
            i += 1
            x[i], x[j] = x[j], x[i]
    x[r], x[i + 1] = x[i + 1], x[r]
    return i + 1

def quickSort(x : list[float], p : int, r : int) -> None:
    if p < r:
        q = partition(x, p, r)
        quickSort(x, p, q - 1)
        quickSort(x, q + 1, r)

if __name__ == "__main__":
    t = float(input())
    if t >= 3:
        x = []
        y = []
        while t > 0:
            a, b = [float(e) for e in input().split()]
            x += [a]
            y += [b]
            t -= 1
        d_squared = []
        for j in range(len(x)):
            d_squared += [(x[j]**2) + (y[j]**2)]
        d_squared2 = d_squared.copy()
        quickSort(d_squared2, 0, len(d_squared2) - 1)
        index = findIndex(d_squared, d_squared2[2])
        print('#', end='')
        print(index + 1, end='')
        print(':', '(', end='')
        print(x[index], end=', ')
        print(y[index], end=')')