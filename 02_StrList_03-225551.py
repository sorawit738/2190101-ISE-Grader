months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
s = input().split("/")
print(months[int(s[1])-1] + " " + s[0] + ", " + s[2])