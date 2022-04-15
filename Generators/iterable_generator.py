
class Squares:
    def __init__(self, n):
        self.n = n
    
    def squares(self):
        for _ in range(self.n):
            yield _**2

    def __iter__(self):
        return self.squares() 

if __name__ == '__main__':

    print(list(Squares(5))) 