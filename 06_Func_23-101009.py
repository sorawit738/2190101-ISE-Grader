def make_int_list(x):
    x = x.split()
    y = []
    for i in range(len(x)):
        y += [int(x[i])]
    return y

def is_odd(e):
    if e % 2 == 0:
        return False
    else:
        return True
    
def odd_list(alist):
    new_list = []
    for i in alist:
        if is_odd(i):
            new_list += [i]
    return new_list

def sum_square(alist):
    sum = 0
    for i in alist:
        sum += i**2
    return sum

exec(input().strip())