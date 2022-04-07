from time import perf_counter
from functools import lru_cache

def memoize(fn):
    cache = {}
    def inner(*args, **kwargs):
        # print('memoize')
        if args not in cache:
            cache[args] = fn(*args, **kwargs)
        # print(cache)
        return cache[args]
    return inner

def fib(n):
    if n==0:
        return 0
    if n<3:
        return 1
    return fib(n-1) + fib(n-2)

@lru_cache()
def fib_lru(n):
    if n==0:
        return 0
    if n<3:
        return 1
    return fib_lru(n-1) + fib_lru(n-2)


if __name__ == '__main__':
    for _ in range(35, 40):
        start = perf_counter()
        print('fib({0}) = {1}'.format(_, fib(_)))
        end = perf_counter()
        print('Time taken = {0:.6f}'.format(end-start))
        print()