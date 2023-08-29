d = int(input())
m = int(input())
y = int(input())

y -= 543

n = 28
if y % 400 == 0:
  n = 29
if y % 4 == 0 and y % 100 != 0:
  n = 29

if m == 1:
  x = d
elif m == 2:
  x = 31 + n + d
elif m == 3:
  x = 31 + n + d
elif m == 4:
  x = 31 + n + 31 + d
elif m == 5:
  x = 31 + n + 31 + 30 + d
elif m == 6:
  x = 31 + n + 31 + 30 + 31 + d
elif m == 7:
  x = 31 + n + 31 + 30 + 31 + 30 + d
elif m == 8:
  x = 31 + n + 31 + 30 + 31 + 30 + 31 + d
elif m == 9:
  x = 31 + n + 31 + 30 + 31 + 30 + 31 + 31 + d
elif m == 10:
  x = 31 + n + 31 + 30 + 31 + 30 + 31 + 31 + 30 + d
elif m == 11:
  x = 31 + n + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + d
elif m == 12:
  x = 31 + n + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + d

print(x)