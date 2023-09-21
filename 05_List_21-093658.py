def findIndex(arr : list[str], target : str) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def inputStudentIdGrades():
    print("input student id grades")
    return


def inputUpgradeIds():
    print("inputUpgradeIds()")
    return


def displayOut():
    print("displayOut()")
    return

def main():
    ids = []
    grades = []
    uids = []
    g = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']
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
        uids += [i]

    i = 0
    while i < len(z):
        if z[i] != 'q':
            ids += [z[i]]
        i += 2

    j = 1
    while j < len(z):
        grades += [z[j]]
        j += 2

    for k in uids:
        index = findIndex(ids, k)
        if grades[index] != 'A':
            index2 = findIndex(g, grades[index]) + 1
            grades[index] = g[index2]

    for n in range(len(ids)):
        print(ids[n], grades[n])

main()