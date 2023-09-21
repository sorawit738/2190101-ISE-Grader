vowels = ['a', 'e', 'i', 'o', 'u', 'y']
s = str(input())
if s.lower()[-1] in ['s', 'x'] or s.lower()[len(s) - 2:] == 'ch':
    new_s = s + 'es'
elif s.lower()[-1] in vowels and s.lower()[len(s) - 2] not in vowels:
    new_s = s[0:-1:] + 'ies'
else:
    new_s = s + 's'

print(new_s)