def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    fullName = ['Robert', 'William', 'James', 'John', 'Margaret', 'Edward', 'Sarah', 'Andrew', 'Anthony', 'Deborah']
    nickame = ['Dick', 'Bill', 'Jim', 'Jack', 'Peggy', 'Ed', 'Sally', 'Andy', 'Tony', 'Debbie']
    t = int(input())
    lst = []
    while t > 0:
        x = str(input())
        lst += [x]
        t -= 1
    for i in range(len(lst)):
        if lst[i] in fullName:
            index = search(fullName, lst[i])
            print(nickame[index])
        elif lst[i] in nickame:
            index = search(nickame, lst[i])
            print(fullName[index])
        else:
            print('Not found')