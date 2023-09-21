x = int(input())

result = []
result.append(x)
while x != 1:
  if x % 2 == 0:
    x = int(x/2)
  else:
    x = (3*x) + 1
  result.append(x)

result2 = []
result2.extend(result[-15:])
i = 0
while i < len(result2):
  if i == len(result2) - 1:
    print(result2[i])
  else:
    print(result2[i], end="->")
  i += 1