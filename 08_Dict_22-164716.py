t1 = int(input())
d = {}

while t1 > 0:
  type1, price = str(input()).split()
  d[type1] = float(price)
  t1 -= 1

t2 = int(input())
chosen = []

while t2 > 0:
  type2, amount = str(input()).split()
  chosen += [[type2, int(amount)]]
  t2 -= 1

new_d = {}
for e in chosen:
  if e[0] in d.keys():
    if e[0] in new_d:
      new_d[e[0]] += e[1] * d[e[0]]
    else:
      new_d[e[0]] = e[1] * d[e[0]]

if len(new_d) == 0:
  print('No ice cream sales')
else:
  sum = 0
  for i in new_d.values():
    sum += i
  
  top_sales = sorted([k for k, v in new_d.items() if v == max(new_d.values())])

  print('Total ice cream sales:', sum)
  print('Top sales:', end =' ')
  for m in range(len(top_sales)):
    if m == len(top_sales) - 1:
      print(top_sales[m])
    else:
      print(top_sales[m], end=', ')