def reverse(d):
  # d is a dict that has no repeated value
  # returns new dict that store key, value as value, key of d
  new_d = {}
  for keys in d:
    new_d[d[keys]] = keys
  return new_d
    
def keys(d, v):
  # returns a list of keys in d (can be in any order) that
  # have a value of v
  lst = []
  for keys in d:
    if d[keys] == v:
      lst += [keys]
  return lst
  
exec(input().strip())