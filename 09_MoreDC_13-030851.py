t = int(input())
wins = []
loss = []
result = []

while t > 0:
    w, l = input().split()
    wins.append(w)
    loss.append(l)
    t -= 1

for ws in wins:
    if ws not in loss:
        result.append(ws)

print(sorted(list(set(result))))
