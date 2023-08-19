import math

def factorial(n):
  if n == 1:
    return 1
  return n*factorial(n-1)

def main():
  print(round((math.pi-((factorial(10))/math.pow(8, 8))+math.pow(math.log(9.7, math.e), ((7/math.sqrt(71))-math.sin((2*math.pi)/9))))/math.pow(1.2, 2.3**(1/3)), 6))

if __name__ == "__main__":
    main()
