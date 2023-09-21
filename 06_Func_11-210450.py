n = input().split()

num1 = int(n[0],2)
num2 = int(n[1],2)
result = num1 + num2
result2 = bin(result)[2:]
print(result2)