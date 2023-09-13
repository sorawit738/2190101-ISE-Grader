a = float(input())
m = a
L = 0
U = 0

while m > 0:
    m = int(m / 10)
    U += 1

x = (U + L) / 2

while abs(a - 10**x) > 10**(-10) * max(a, 10**x):
    if 10**x > a:
        U = x
    else:
        L = x
    
    x = (U + L) / 2

print(round(x, 6))