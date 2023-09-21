x = [float(i) for i in input().split()]
count = 0
for j in range(1, len(x) - 1):
  if x[j] > x[j - 1] and x[j] > x[j + 1]:
    count += 1
    
print(count)