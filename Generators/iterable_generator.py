
class Squares:
    def __init__(self, n):
        self.n = n
    
    def squares(self):
        for _ in range(self.n):
            yield _**2

    def __iter__(self):
        return self.squares() 

def squares(n):
        for _ in range(n):
            yield _**2

if __name__ == '__main__':

    print(list(Squares(5)))
    squ = Squares(3)
    print(next(squ))
    print(next(squ))
    sq = squares(3)
    print(next(sq))
    print(next(sq)) 