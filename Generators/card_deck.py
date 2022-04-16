from collections import namedtuple

Card = namedtuple('Card', 'rank suit')
SUITS_ = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
RANKS_ = tuple(range(2, 11)) + tuple('JQKA')

def card_gen():
    n = len(SUITS_) * len(RANKS_)
    for _ in range(n):
        suit = SUITS_[_//len(RANKS_)]
        rank = RANKS_[_%len(RANKS_)]
        card = Card(rank, suit)
        yield card

class CardGen:

    def __init__(self):
        self.suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
        self.ranks = tuple(range(2, 11)) + tuple('JQKA')
        self.ranks_len = len(self.ranks)
        self.Card = namedtuple('Card', 'rank suit')
    
    def card_gen(self):
        n = len(self.suits) * len(self.ranks)
        for _ in range(n):
            suit = self.suits[_//self.ranks_len]
            rank = self.ranks[_%self.ranks_len]
            card = self.Card(rank, suit)
            yield card

    def reversed_card_gen(self):
        for suit in reversed(self.suits):
            for rank in reversed(self.ranks):
                yield self.Card(rank, suit)

    def __reversed__(self):
        return self.reversed_card_gen()
        
    def __iter__(self):
        return self.card_gen()


if __name__ == '__main__':
    cards = card_gen()

    for card in cards:
        print(card)
    
    for card in reversed(CardGen()):
        print(card)