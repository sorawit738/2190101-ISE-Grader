num = int(input())

if num // 1000000000 == 0:
  if num // 1000000 == 0:
    if num // 1000 == 0:
      print(num)
    elif num/1000 > 10:
      print(str(int(round(num/1000, 0))) + "K")
    else:
      print(str(round(num/1000, 1)) + "K")
  elif num/1000000 > 10:
    print(str(int(round(num/1000000, 0))) + "M")
  else:
    print(str(round(num/1000000, 1)) + "M")
elif num/1000000000  > 10:
  print(str(int(round(num/1000000000, 0))) + "B")
else:
  print(str(round(num/1000000000, 1)) + "B")