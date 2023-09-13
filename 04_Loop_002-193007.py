x = str(input())
d = x.split()

p = int(d[-1])
n = len(d)
i = j = 0
while j < n - 1:
    if int(d[j]) <= p:
        d[i], d[j] = d[j], d[i]
        i += 1
    j += 1

d[i], d[-1] = d[-1], d[i]

m = [int(i) for i in d]

print(m)