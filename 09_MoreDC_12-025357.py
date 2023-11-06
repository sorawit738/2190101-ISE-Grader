t = int(input())
if t == 0:
    print(0)
    print(0)
else:
    all_sets = []
    while t > 0:
        all_sets.append([int(e) for e in input().split()])
        t -= 1

    union = set([int(e) for e in [b for a in all_sets for b in a]])

    count2 = 0
    for i in set(all_sets[0]):
        count1 = 0
        for j in range(len(all_sets)):
            if i in all_sets[j]:
                count1 += 1
        if count1 == len(all_sets):
            count2 += 1

    print(len(union))
    print(count2)
