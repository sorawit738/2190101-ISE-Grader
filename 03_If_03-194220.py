a = input().split()
x = [float(e) for e in a]

#sort the array
for i in range(1, len(x)):
  temp = x[i]
  j = i - 1
  while j >= 0 and x[j] > temp:
    x[j + 1] = x[j]
    j -= 1
  x[j + 1] = temp

y = round(((x[1] + x[2])/2), 2)
print(y)