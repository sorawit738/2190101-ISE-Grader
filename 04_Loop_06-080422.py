h = int(input())
b = 2*h - 1

if h >= 2:
  mid = ((b + 1) // 2) - 1
  for i in range(h):
    y = [' '] * b
    new_y = ''
    if i == h - 1:
      for j in range(len(y)):
        y[j] = '*'
      for elements in y:
        new_y += '{}'.format(elements)
      print(new_y)
    elif i == 0:
      y[mid] = '*'
      for elements in y:
        new_y += '{}'.format(elements)
      print(new_y)
    else:
      y[mid + i] = '*'
      y[mid - i] = '*'
      for elements in y:
        new_y += '{}'.format(elements)
      print(new_y)