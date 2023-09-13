s1 = str(input())
s2 = str(input())

if len(s1) != len(s2):
    print('Incomplete answer')
else:
    count = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            count += 1
    print(count)