def knows(R, x, y):
    k = False
    if y in R[x]:
        k = True
    return k

def is_celeb(R, x):
    count = 0
    for e in R.keys():
        if e == x:
            for a in R[e]:
                if a != x:
                    return False
            continue
        if x in R[e]:
            count += 1
    if count == len(R) - 1 or count == len(R):
        return True
    return False

def find_celeb(R):
    lst = []
    for k in R.keys():
        lst.append(k)
    for v in R.values():
        for b in v:
            lst.append(b)
    s = set(lst)
    for a in s:
        if is_celeb(R, a):
            return a
    return None

def read_relations():
    R = dict()
    while True:
        d = input().split()
        if len(d) == 1:
            break
        if d[0] not in R:
            R[d[0]] = {d[1]}
        else:
            R[d[0]].add(d[1])
    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None:
        print('Not Found')
    else:
        print(c)

exec(input().strip())