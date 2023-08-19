def is_integer(n):
    if isinstance(n, int):
        return True
    elif isinstance(n, float) and n.is_integer():
        return True
    else:
        return False

x = input().split("/")
if len(x) != 3:
    print("Incorrect input.")
    print("Input have to be in the format: XX/XX/XXXX.")
elif is_integer(int(x[2])) == False:
    print("The year has to be an integer.") 
else:
    buddhistYear = int(x[2])
    christianYear = buddhistYear-543
    print(x[0]+"/"+x[1]+"/"+str(christianYear))