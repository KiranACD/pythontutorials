from collections import namedtuple

Card = namedtuple('Card', 'rank suit')
SUITS_ = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
RANKS_ = tuple(range(2, 11)) + tuple('JQKA')

