def maxList(a) -> int:
    max = a[0]
    for i in a:
        if max < i:
            max = i
    return max

def minList(a) -> int:
    min = a[0]
    for i in a:
        if min > i:
            min = i
    return min

def main():
    t = int(input())
    m = t
    x = []
    y = []
    while m > 0:
        n = input().split()
        x.append(int(n[0]))
        y.append(int(n[1]))
        m -= 1

    r = [] * t
    b = [] * t
    command = input()
    if command == 'Zig-Zag':
        j = 1
        i = 0
        while j < t:
            r.append(y[j])
            b.append(x[j])
            j += 2
        while i < t:
            r.append(x[i])
            b.append(y[i])
            i += 2
    elif command == 'Zag-Zig':
        j = 1
        i = 0
        while j < t:
            b.append(y[j])
            r.append(x[j])
            j += 2
        while i < t:
            b.append(x[i])
            r.append(y[i])
            i += 2
    
    print(minList(r), maxList(b))

main()