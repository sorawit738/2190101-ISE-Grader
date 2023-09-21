t = int(input())
result = []
for i in range(t):
  n = int(input())
  result.append(n)
  
new_list = [int(j) for j in input().split()]
result.extend(new_list)
m = 0
while m != -1:
  m = int(input())
  if m != -1:
    result.append(m)

new_list2 = []
for k in range(len(result)):
  if k % 2 == 0:
    new_list2.append(result[k])
  else:
    new_list2.insert(0, result[k])

print(new_list2)