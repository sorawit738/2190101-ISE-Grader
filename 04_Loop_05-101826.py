def filter_word(s):
    s = s.replace('\"', ' ')
    s = s.replace(")", ' ')
    s = s.replace("(", ' ')
    s = s.replace(",", ' ')
    s = s.replace(".", ' ')
    s = s.replace("\'", ' ')
    return s

def main():
    target = str(input())
    s = str(input())
    x = filter_word(s).split()

    count = 0

    for i in x:
        '''
        if i.startswith('"') or i.startswith('(') or i.startswith("'"):
            i = i[1:]
        if i.endswith('"') or i.endswith(')') or i.endswith("'") or i.endswith(',') or i.endswith('.'):
            i = i[:-1]
        '''
        if i == target:
            count += 1

    print(count)

main()