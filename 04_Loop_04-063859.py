x = str(input())

if '(' in x or ')' in x or '[' in x or ']' in x:
  y = []
  new_x = ''
  for i in range(len(x)):
    y.append(x[i])
  for j in range(len(y)):
    if y[j] == '(':
      y[j] = '['
    elif y[j] == '[':
      y[j] = '('
    elif y[j] == ')':
      y[j] = ']'
    elif y[j] == ']':
      y[j] = ')'
  for elements in y:
    new_x += '{}'.format(elements)
  print(new_x)

else:
  print(x)