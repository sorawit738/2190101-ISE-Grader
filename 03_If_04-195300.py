phone_nums = ['06', '08', '09']
num = str(input())

if num[0:2] in phone_nums and len(num):
  print('Mobile number')
else:
  print('Not a mobile number')