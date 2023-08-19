import math

def lower_bound(n1):
    return math.sqrt(2*math.pi) * math.pow(n1, (n1+0.5)) * math.exp(-n1 + (1/((12*n1) + 1)))

def upper_bound(n2):
    return math.sqrt(2*math.pi) * math.pow(n2, (n2+0.5)) * math.exp(-n2 + (1/(12*n2)))

def main():
    num = int(input())
    print(lower_bound(num))
    print(upper_bound(num))

if __name__ == "__main__":
    main()