
from timeit import timeit


def fib_rec(n):
    if n < 2 :
        return 1

    return fib_rec(n-1) + fib_rec(n-2)

def fib_iter(n):
    fib0 = 1
    fib1 = 1

    for _ in range(n-1):
        fib0, fib1 = fib1, fib0+fib1
    
    return fib1

class FibIter:
    def __init__(self, n):
        self.n = n
        self.i = 0
    
    def fib_iter(self):
        fib_0 = 1
        fib_1 = 1
        for _ in range(self.i - 1):
            fib_0, fib_1 = fib_1, fib_0 + fib_1
        return fib_1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        else:
            result = self.fib_iter()
            self.i += 1
            return result

def fib_gen(n):
    fib_0 = 1
    yield fib_0
    fib_1 = 1
    yield fib_1
    for _ in range(n-2):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        yield fib_1
    

if __name__ == '__main__':

    fib = FibIter(7)
    print([fib_iter(i) for i in range(7)])
    print([num for num in fib])
    gen = fib_gen(7)
    print([num for num in gen])

    print(timeit('list(FibIter(5000))', globals=globals(), number = 1))
    print(timeit('list(fib_gen(5000))', globals=globals(), number = 1))

    
