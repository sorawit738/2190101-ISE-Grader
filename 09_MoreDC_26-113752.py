n = int(input())
x = {}
order = []
while n > 0:
    id, c = str(input()).split(': ')
    order.append(int(id))
    c = c.split(', ')
    x[int(id)] = c
    n -= 1

temp = int(input())
p = []

for k in x.keys():
    for i in range(len(x[temp])):
        if k not in p and temp != k and x[temp][i] in x[k]:
            p.append(k)

if len(p) == 0:
    print('Not Found')
else:
    for b in order:
      if b in p :
          print(b)