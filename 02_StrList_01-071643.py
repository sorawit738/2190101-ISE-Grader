def check_digit(a):
  digits = [0] * 13
  i = 11
  while a != 0:
    remainder = a % 10
    digits[i] = remainder
    i -= 1
    a = int(a/10)

  result = ((11)-(13*digits[0]+12*digits[1]+11*digits[2]+10*digits[3]+9*digits[4]+8*digits[5]+7*digits[6]+6*digits[7]+5*digits[8]+4*+digits[9]+3*digits[10]+2*digits[11]) % 11) % 10
  digits[12] = result
  
  return digits

def main():
  n = int(input())
  p = check_digit(n)
  print(str(p[0]) + " " + str(p[1]) + str(p[2]) + str(p[3]) + str(p[4]) + " " + str(p[5]) + str(p[6]) + str(p[7]) + str(p[8]) + str(p[9]) + " " + str(p[10]) + str(p[11]) + " " + str(p[12]))

if __name__ == "__main__":
    main()