import math

def mosteller(w1, h1):
  return (math.sqrt(w1*h1))/60

def haycock(w2, h2):
  return 0.024265*math.pow(w2, 0.5378)*math.pow(h2, 0.3964)

def boyd(w3, h3):
  return 0.0333*math.pow(w3, (0.6157-0.0188*math.log(w3, 10)))*math.pow(h3, 0.3)

def main():
  W = float(input())
  H = float(input())
  print(mosteller(W, H))
  print(haycock(W, H))
  print(boyd(W, H))

if __name__ == "__main__":
    main()