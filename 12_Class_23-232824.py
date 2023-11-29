class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.s_order = ('club', 'diamond', 'heart', 'spade')
        self.v_order = ('3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2')

    def __str__(self):
        return '(' + self.value + ' ' + self.suit + ')'

    def next1(self):
        if self.s_order.index(self.suit) < len(self.s_order) - 1:
            next_v, next_s = self.value, self.s_order[self.s_order.index(self.suit) + 1]
        else:
            if self.v_order.index(self.value) < len(self.v_order) - 1:
                next_v, next_s = self.v_order[self.v_order.index(self.value) + 1], self.s_order[0]
            else:
                next_v, next_s = self.v_order[0], self.s_order[0]

        return Card(next_v, next_s)

    def next2(self):
        self.value = self.next1().value
        self.suit = self.next1().suit

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))

for i in range(n):
    print(cards[i].next1())

print("----------")

for i in range(n):
    print(cards[i])

print("----------")

for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
