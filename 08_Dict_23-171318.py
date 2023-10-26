t1 = int(input())
d = {}

while t1 > 0:
  fname, sname, pnum = str(input()).split()
  d[fname + ' ' + sname] = pnum
  d[pnum] = fname + ' ' + sname
  t1 -= 1

t2 = int(input())

while t2 > 0:
  n = str(input())
  if n in d.keys():
    print(n, '-->', d[n])
  else:
    print(n, '--> Not found')
  t2 -= 1