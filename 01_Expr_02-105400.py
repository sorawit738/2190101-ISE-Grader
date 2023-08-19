import math

def first_root(a1, b1, c1):
  return (-b1-math.sqrt(math.pow(b1,2)-(4*a1*c1)))/(2*a1)

def second_root(a2, b2, c2):
  return (-b2+math.sqrt(math.pow(b2,2)-(4*a2*c2)))/(2*a2)

def main():
  a = float(input())
  b = float(input())
  c = float(input())
  print(round(first_root(a, b, c), 3))
  print(round(second_root(a, b, c), 3))


if __name__ == "__main__":
    main()
  