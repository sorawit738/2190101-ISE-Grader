def insertionSort(x):
    for i in range(len(x)):
        temp = x[i]
        j = i - 1
        while j >= 0 and x[j] > temp:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = temp
    return x

def selectionSort(x):
    for i in range(len(x)):
        position = i
        for j in range((i + 1), len(x)):
            if x[j] < x[position]:
                position = j
        x[i], x[position] = x[position], x[i]
    return x

def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left = [0] * (n1)
    right = [0] * (n2)
    for i in range(n1):
        left[i] = arr[p + i]
    for j in range(n2):
        right[j] = arr[q + 1 + j]

    i, j, k = 0, 0, p
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1

def mergeSort(arr, p, r):
    if p < r:
        q = int(p + (r - p) / 2)
        mergeSort(arr, p, q)
        mergeSort(arr, q + 1, r)
        merge(arr, p, q, r)

def partition(x, p, r):
    temp = x[r]
    i = p - 1
    for j in range(p, r):
        if x[j] <= temp:
            i += 1
            x[i], x[j] = x[j], x[i]
    x[r], x[i + 1] = x[i + 1], x[r]
    return i + 1

def quickSort(x, p, r):
    if p < r:
        q = partition(x, p, r)
        quickSort(x, p, q - 1)
        quickSort(x, q + 1, r)