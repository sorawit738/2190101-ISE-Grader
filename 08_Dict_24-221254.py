def text2keys(text):
  d1 = {2:'a', 22:'b', 222:'c', 3:'d', 33:'e', 333:'f', 4:'g', 44:'h', 444:'i', 5:'j', 55:'k', 555:'l', 6:'m', 66:'n', 666:'o', 7:'p', 77:'q', 777:'r', 7777:'s', 8:'t', 88:'u', 888:'v', 9:'w', 99:'x', 999:'y', 9999:'z', 0:' '}
  d2 = {}
  for num in d1:
    d2[d1[num]] = num
  ans = ''
  for c in text.lower():
    if 97 <= ord(c) <= 122 or c == ' ':
      ans += str(d2[c]) + ' '
  return ans[:len(ans) - 1:]

def keys2text(keys):
  d1 = {2:'a', 22:'b', 222:'c', 3:'d', 33:'e', 333:'f', 4:'g', 44:'h', 444:'i', 5:'j', 55:'k', 555:'l', 6:'m', 66:'n', 666:'o', 7:'p', 77:'q', 777:'r', 7777:'s', 8:'t', 88:'u', 888:'v', 9:'w', 99:'x', 999:'y', 9999:'z', 0:' '}
  keys_list = keys.split()
  ans = ''
  for c in keys_list:
    ans += d1[int(c)]
  return ans

exec(input().strip())