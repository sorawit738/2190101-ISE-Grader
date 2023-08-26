import module
'''
def insertionSort(x):
    for i in range(len(x)):
        temp = x[i]
        j = i - 1
        while j >= 0 and x[j] > temp:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = temp
    return x
'''

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    arr = [a, b, c, d, e]
    print(module.insertionSort(arr)[2])

if __name__ == "__main__":
    main()