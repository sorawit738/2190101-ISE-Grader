def average(arr):
  sum = 0
  for i in arr:
    sum += i
  return sum/len(arr)

if __name__ == "__main__":
  m = str(input())
  q = m.split()
  y = []
  infile = open(q[0], "r")
  for k in infile:
    x = k[0:2]
    if x == q[1][2:len(q[1])]:
      y += [float(k[11:])]
  infile.close()

  if len(y) == 0:
    print('No data')
  else:
    print(min(y), max(y), average(y))