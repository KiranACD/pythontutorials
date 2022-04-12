from functools import lru_cache

class Fib:
    def __init__(self, n):
        self.n = n
    
    def __len__(self):
        return self.n
    
    def __getitem__(self, value):

        if isinstance(value, int):
            if value < 0:
                value = self.n + value
            if value < 0 or value >= self.n:
                raise IndexError
            else:
                return Fib._fib(value)
        else:
            range_ = range(*value.indices(self.n))
            return [Fib._fib(i) for i in range_]
    
    @staticmethod
    @lru_cache(2**10)
    def _fib(n):
        if n < 2:
            return 1
        else:
            return Fib._fib(n-1) + Fib._fib(n-2)
