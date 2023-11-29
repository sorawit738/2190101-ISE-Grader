import math
x, m, s = [float(e) for e in input().split()]
if x <= 0 or m == 0 or s <= 1:
  print('Invalid input')
else:
  r = ((2*math.pi)**-0.5) * (s**-1) * ((math.e)**(-(0.5)*((x-m)/s)**2))
  print(round(r, 2))