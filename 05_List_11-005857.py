x = str(input())
digits = ['0','1','2','3','4','5','6','7','8','9']
check = [0] * 10
for i in range(len(x)):
    for j in range(len(digits)):
        if x[i] == digits[j]:
            check[j] = 1
count = 0
for m in range(len(check)):
    if check[m] == 0:
       count += 1
if count == 0:
    print('None')
else:
    s = ''
    for k in range(len(check)):
        if check[k] == 0:
            if len(s) == 0:
                s += digits[k]
            else:
                s += ',' + digits[k]
    print(s)