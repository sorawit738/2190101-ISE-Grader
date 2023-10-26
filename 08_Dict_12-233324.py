t1 = int(input())
names = {}

while t1 > 0:
    s1 = str(input()).split()
    names[s1[0]] = s1[1]
    names[s1[1]] = s1[0]
    t1 -= 1

t2 = int(input())
s2 = []

while t2 > 0:
    s2 += [str(input())]
    t2 -= 1

for z in s2:
    if z in names:
        print(names[z])
    else:
        print("Not found")