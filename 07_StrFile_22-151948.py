s1 = str(input())
s2 = str(input())
lsts1 = list(s1.lower())
lsts2 = list(s2.lower())
lsts1.sort()
lsts2.sort()
i = len(lsts1) - 1
j = len(lsts2) - 1
while i >= 0:
    if lsts1[i] == ' ':
        lsts1.pop(i)
    i -= 1
while j >= 0:
    if lsts2[j] == ' ':
        lsts2.pop(j)
    j -= 1
if lsts1 == lsts2:
    print('YES')
else:
    print('NO')