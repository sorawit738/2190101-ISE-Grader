n = input()
a = int(n[3::7]) + int(n[7:28:5]) + 10000
k = int(a/10) % 1000
sum = 0
while k != 0:
  remainder = k % 10
  sum += remainder
  k = int(k/10)

last_digit = sum % 10

s_a = str(int(a/10))
i = s_a[len(s_a)-3:len(s_a)]

alphabets = ["a","b","c","d","e","f","g","h","i","j"]
print(i + alphabets[last_digit].upper()) 
# alphabets[(last_digit + 1) - 1] = alphabets[last_digit]