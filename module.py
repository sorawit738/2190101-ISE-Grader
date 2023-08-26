def insertionSort(x):
    for i in range(len(x)):
        temp = x[i]
        j = i - 1
        while j >= 0 and x[j] > temp:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = temp
    return x
