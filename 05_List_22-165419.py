ids = []
grades = []
uids = []
g = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']

def findIndex(arr : list[str], target : str) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def findMinIndex(arr : list[str]) -> int:
    min = arr[0]
    for i in range(1, len(arr)):
        if min > arr[i]:
            min = arr[i]
    return findIndex(arr, min)

def inputStudentIdGrades() -> None:
    z = []
    test = True
    while test:
        y = input()
        if y == 'q':
            test = False
        y = y.split()
        z += y
    s = str(input())
    s = s.split()
    for i in s:
        uids.append(i)

    i = 0
    while i < len(z):
        if z[i] != 'q':
            ids.append(z[i])
        i += 2

    j = 1
    while j < len(z):
        grades.append(z[j])
        j += 2

def inputUpgradeIds() -> None:
    for k in uids:
        index = findIndex(ids, k)
        if grades[index] != 'A':
            index2 = findIndex(g, grades[index]) + 1
            grades[index] = g[index2]


def displayOut() -> None:
    i = len(ids) - 1
    while i >= 0:
        minIndex = findMinIndex(ids)
        print(ids[minIndex], grades[minIndex])
        ids.pop(minIndex)
        grades.pop(minIndex)
        i -= 1

if __name__ == "__main__":
    inputStudentIdGrades()
    inputUpgradeIds()
    displayOut()