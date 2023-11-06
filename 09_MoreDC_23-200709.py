def sec_to_min(v):
    remainder = v % 60
    v2 = int((v - remainder) / 60)
    if len(str(remainder)) == 1 and remainder >= 10:
        result = str(v2) + ':' + str(remainder) + '0'
    elif len(str(remainder)) == 1 and remainder < 10:
        result = str(v2) + ':' + '0' + str(remainder)
    else:
        result = str(v2) + ':' + str(remainder)
    return result

t = int(input())
gt = []

while t > 0:
    sname, name, genre, time = str(input()).split(', ')
    temp = time.split(':')
    stime = (int(temp[0]) * 60) + int(temp[1])
    test = True
    for i in range(len(gt)):
        if genre in gt[i]:
            index = i
            test = False
    if test:
        gt.append([genre, stime])
    else:
        gt[index][1] += stime
    t -= 1

gt = [[a[1], -a[0]] for a in sorted([[-b[1], b[0]] for b in gt])]
while len(gt) > 3:
    gt.pop(len(gt) - 1)

for e in gt:
    print(e[0], '-->', sec_to_min(e[1]))
