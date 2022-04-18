from math import factorial
from itertools import islice
# Generators are not subscriptable. So regular method of slicing does not work.
# But, we can create our own slicing function. 

def factorials(n):
    for _ in range(n):
        yield factorial(_)

def slice_(iterable, start, stop):

    for _ in range(start):
        next(iterable)
    for _ in range(start, stop):
        yield next(iterable)

print(list(slice_(factorials(10), 3, 10)))

print(list(islice(factorials(10), 3, 10, 2)))

# This will give values upto the 5th factorial.
print(list(islice(factorials(10), 5)))