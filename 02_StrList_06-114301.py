x = input()
y = input()
u = x[1:-1].split(", ")
v = y[1:-1].split(", ")
r = [float(e) for e in u]
o = [float(e) for e in v]
z = [(float(u[0])+float(v[0])), (float(u[1])+float(v[1])), (float(u[2])+float(v[2]))]
print(r, "+", o, "=", str(z))