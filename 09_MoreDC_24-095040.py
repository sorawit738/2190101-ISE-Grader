l = str(input())
v = []

while l != 'q':
    x, y = l.split(', ')
    test = True
    for i in range(len(v)):
        if y in v[i]:
            index = i
            test = False
    if test:
        v.append([y, x])
    else:
        v[index].append(x)
    l = str(input())

types = []

for j in range(len(v)):
    types.append(v[j].pop(0))


for k in range(len(types)):
    s = ''
    for n in range(len(v[k])):
        if n == 0:
            s += types[k] + ': ' + v[k][n]
        else:
            s += ', ' + v[k][n]
    print(s)
