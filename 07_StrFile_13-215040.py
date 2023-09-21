def filter_word(s):
    s = s.replace('\"', ' ')
    s = s.replace(")", ' ')
    s = s.replace("(", ' ')
    s = s.replace(",", ' ')
    s = s.replace(".", ' ')
    s = s.replace("\'", ' ')
    s = s.replace("-", ' ')
    s = s.replace(">", ' ')
    s = s.replace("<", ' ')
    s = s.replace(";", ' ')
    s = s.replace(":", ' ')
    return s

if __name__ == "__main__":
    s = str(input())
    s = filter_word(s).split()
    new_s = ''
    for i in range(len(s)):
        if i == 0:
            new_s += s[i].lower()
        else:
            new_s += s[i].title()

    print(new_s)