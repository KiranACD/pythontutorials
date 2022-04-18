from itertools import islice, count, cycle, takewhile, repeat
from collections import namedtuple

print(list(takewhile(lambda x: round(x, 2)<10.8, count(10.5, 0.1))))

def squares(n):
    for _ in range(n):
        yield (_**2)

sq = squares(5)
count = (item for item in range(20))
print([item for count, item in zip(count, cycle(sq))])

sq = squares(5)
print(list(islice(cycle(sq), 20)))
# count = 0
# for item in cycle(sq):
#     print(item)
#     count += 1
#     if count == 20:
#         break

Card = namedtuple('Card', 'suit rank')

suits = ['spades', 'hearts', 'diamonds', 'clubs']
ranks = tuple(str(item) for item in range(2, 11)) + tuple('JQKA')

def card_deck():
    for suit in suits:
        for rank in ranks:
            yield Card(suit, rank)

hands = [list() for _ in range(4)]
hand_cycle = cycle(hands)

for card in card_deck():
    next(hand_cycle).append(card)
print(hands)

g = repeat('python', 10)

print(list(g))
print(list(g))