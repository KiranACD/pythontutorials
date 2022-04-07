from time import perf_counter
from functools import lru_cache
from memoization import memoize

class Timer:
    def __init__(self, reps):
        self.reps = reps
    
    def __call__(self, fn):
        def inner(*args, **kwargs):
            print('Running Timer')
            total_elapsed = 0
            for _ in range(self.reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                total_elapsed += perf_counter() - start
            
            average = total_elapsed/self.reps
            print('Average time taken = {0} after running {1} reps'.format(average, self.reps))
            return result
        return inner

@memoize
def fib(n):

    if n == 0:
        return 0

    elif n < 3:
        return 1
    
    else:
        return fib(n-2) + fib(n-1)

@Timer(10)
def fib_recursive(n):
    # print('Running fib')
    return fib(n)

for _ in range(35, 40):

    print('fib({0}) = {1}'.format(_, fib_recursive(_)))
    print()