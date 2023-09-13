x = str(input())
if x == 'q':
  print('No Data')
else:
  s = [x]
  i = 0
  while s[i] != 'q':
    x = str(input())
    s.append(x)
    i += 1
    
  sum = 0
  for j in range(len(s) - 1):
    sum += float(s[j])
  print(round(sum/(len(s) - 1), 2))