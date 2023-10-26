s = str(input()).lower()
x = [*s]
d = {}

while len(x) > 0:
    most = max(set(x), key=x.count)
    if 97 <= ord(most) <= 122:
        d[most] = x.count(most)
    while x.count(most) > 0:
        x.remove(most)

d_lst = []

for e in d:
  d_lst.append([e, d[e]])

d_lst = sorted(d_lst)
d_lst = [[a[1], -a[0]] for a in sorted([[-e[1], e[0]] for e in d_lst])]

for keys in d_lst:
    print(keys[0], '->', keys[1])