def row_number(t, e):
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j] == e:
                return i
    return -1

def flatten(t):
    int_lst = []
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j] != 0:
                int_lst += [t[i][j]]
    return int_lst

def inversions(x):
    count = 0
    for i in range(len(x) - 1):
        j = i + 1
        while j < len(x):
            if x[i] > x[j]:
                count += 1
            j += 1
    return count

def solvable(t):
    x = flatten(t)
    if len(t) % 2 == 0:
        if inversions(x) % 2 == 0:
            if row_number(t, 0) % 2 != 0:
                return True
        else:
            if row_number(t, 0) % 2 == 0:
                return True
    else:
        if inversions(x) % 2 == 0:
            return True
    return False

exec(input().strip())
