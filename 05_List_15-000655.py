def partition(x, p, r):
    temp = x[r]
    i = p - 1
    for j in range(p, r):
        if x[j] <= temp:
            i += 1
            x[i], x[j] = x[j], x[i]
    x[r], x[i + 1] = x[i + 1], x[r]
    return i + 1

def quickSort(x, p, r):
    if p < r:
        q = partition(x, p, r)
        quickSort(x, p, q - 1)
        quickSort(x, q + 1, r)

def main():
  x = [int(i) for i in input().split()]
  #quickSort(x, 0, len(x) - 1)
  x.sort()
  result = [x[0]]
  check = x[0]
  count = 1
  for i in range(1,len(x)):
    if check != x[i]:
      count += 1
      check = x[i]
      if count <= 10:
        result.append(check)
  print(count)
  print(result)

main()