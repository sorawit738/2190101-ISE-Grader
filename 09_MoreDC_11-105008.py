l = int(input())
lst = []

while l > 0:
    s = str(input())
    count = 0
    s1 = ''
    for e in s:
        if ord(e) == 46:
            count += 1
        else: break
    s1 += ('.' * int(count/2)) + s[count::].strip()
    lst.append(s1)
    l -= 1

for e in lst:
    print(e)