from itertools import starmap, accumulate, chain
import operator
from functools import reduce
def squares(n):
    for i in range(n):
        print(i**2)
        yield i**2

def get_setbits(x):
    count = 0
    while x > 0:
        if x%2:
            count += 1
        x //= 2
        
    return count

powers = list(map(get_setbits, squares(10)))
print(powers)

l = [[1, 2], [3, 4], [5, 6]]

print(list(starmap(operator.mul, l)))

def mul(t):
    return t[0] * t[1]

l = [(1, 2), [2, 3], range(4, 6)]
l1 = [1, 2, 3, 4]

print(list(starmap(operator.mul, l)))
print(list(map(mul, l)))
print(reduce(operator.mul, l1, 10))

def running_reduce(fn, iterable, start = None):
    it = iter(iterable)
    if start is None:
        acc = next(it)
    else:
        acc = start
    yield acc
    for item in it:
        acc = fn(acc, item)
        yield acc

print(list(running_reduce(operator.mul, l1, 10)))

print(list(accumulate([1, 2, 3, 4], operator.mul)))

# to get an initial value

print(list(accumulate(chain((10,), [1, 2, 3, 4]), operator.mul)))