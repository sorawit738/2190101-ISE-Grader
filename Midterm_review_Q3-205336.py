#write method "search".
def show(d):
  for e in d:
    print(e)

def search(m, keyword, power):
  result1 = list()
  # search for keyword in name or ability
  for monster in m:
    if keyword == "-":
      result1 = m
      break

    if (keyword in monster[0]) or (keyword in monster[1]):
      result1.append(monster)

  result2 = list()
  for monster in result1:
    if power == "-":
      result2 = result1
      break
    if int(power) == monster[2]:
      result2.append(monster)

  return result2


m1 = ["green giant", "sacrifice a monster: draw a card", 5]
m2 = ["blue giant", "tap: draw a card, then discard a card" , 3]
m3 = ["blue drake", "discard a card: return to hand", 1]
m4 = ["green drake", "sacrifice a land: destroy target giant", 3]
m5 = ["black wurm", "sacrifice a permanent: destroy target permanent", 3]
m = [m1,m2,m3,m4,m5]

exec(input())