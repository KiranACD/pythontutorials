from collections import namedtuple

_SUITS = ('Spade', 'Hearts', 'Diamonds', 'Clubs')
_RANKS = tuple(range(2, 11)) + tuple('JQKA')

Card = namedtuple('Card', 'rank suit')

class CardDeck:
    def __init__(self):
        self.length = len(_RANKS) * len(_SUITS)
    
    def __len__(self):
        return self.length
    
    def __iter__(self):
        return self.CardDeckIterator(self.length)
    
    def __reversed__(self):
        return self.CardDeckIterator(self.length, reverse=True)
    
    class CardDeckIterator:
        def __init__(self, length, reverse=False):
            self.length = length
            self.i = 0
            self.reverse=reverse
            if self.reverse == True:
                self.i = self.length
        
        def __iter__(self):
            return self

        def __next__(self):
            
            if self.i >= self.length:
                raise StopIteration
            else:
                if self.reverse:
                    index = self.length - self.i - 1
                else:
                    index = self.i
                suit = _SUITS[index // len(_RANKS)]
                rank = _RANKS[index % len(_RANKS)]
                self.i += 1
                return Card(rank, suit)



if __name__ == '__main__':

    deck = CardDeck()
    for card in deck:
        print(card)        

