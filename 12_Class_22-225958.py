class Card:
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.result = 0
        self.c_values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
        self.s_order = ('club', 'diamond', 'heart', 'spade')
        self.v_order = ('3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2')

    def __str__(self):
        return '(' + self.value + ' ' + self.suit + ')'

    def getScore(self):
        self.result += self.c_values.index(self.value) + 1
        if self.result > 10:
            r = self.result % 10
            self.result -= r
        return self.result

    def sum(self, other):
        return (self.result + other.result) % 10

    def __lt__(self, rhs):
        return (self.v_order.index(self.value), self.s_order.index(self.suit)) < (self.v_order.index(rhs.value), self.s_order.index(rhs.suit))

n = int(input())
cards = []

for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))

for i in range(n):
    print(cards[i].getScore())

print("----------")

for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))

print("----------")
cards.sort()

for i in range(n):
    print(cards[i])
