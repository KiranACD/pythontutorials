from time import perf_counter
import time
import datetime
from functools import wraps, reduce
from Logger import logger

def timed(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end-start

        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k,v) in kwargs.items()]
        args_str = ','.join(args_ + kwargs_)

        print('{0}({1}) took {2:.6f}s to run'.format(fn.__name__, args_str, elapsed))

        return result
    return inner

def fib_rec(n):
    if n==0:
        return 0
    if n<=2:
        return 1

    return fib_rec(n-1) + fib_rec(n-2)

@logger
@timed
def fib_recursive(n):
    return fib_rec(n)

@logger
@timed
def fib_loop(n):
    if n==0:
        return 0
    fib_1 = 0
    fib_2 = 1
    for _ in range(2, n+1):
        fib_1, fib_2 = fib_2, fib_1+fib_2
    return fib_2

@logger
@timed
def fib_reduce(n):
    if n==0:
        return 0
    initial = (0, 1)
    iter = range(2, n+1)
    fib = reduce(lambda fib, n: (fib[1], fib[0] + fib[1]), iter, initial)
    return fib[1]

for n in range(35, 40):
    print('Iteration: ', n)
    print('Recursion_fib = {0}'.format(fib_recursive(n)))
    print('Loop_fib = {0}'.format(fib_loop(n)))
    print('Reduce_fib = {0}'.format(fib_reduce(n)))
    print()
