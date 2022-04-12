import sys
from dis import dis

print(dis(compile('(1, 2, 3, "a")', 'string', 'eval')))
print()
print(dis(compile('[1, 2, 3, "a"]', 'string', 'eval')))

from timeit import timeit

print('Timing creation of (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) vs [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
print()
print(timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)', number = 10000000))
print(timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]', number = 10000000))

print()
print('Timing creation of (1, 2, 3, 4, 5, 6, 7, 8, [9, 10]) vs [1, 2, 3, 4, 5, 6, 7, 8, [9, 10]]')
print()
print(timeit('(1, 2, 3, 4, 5, 6, 7, 8, [9, 10])', number = 10000000))

print(timeit('[1, 2, 3, 4, 5, 6, 7, 8, [9, 10]]', number = 10000000))

print()

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

l1 = list(l)
t1 = tuple(t)

print(f'id of l {l} = {id(l)} and id of l1 {l1} = {id(l1)}')

print(f'id of t {t} = {id(t)} and id of t1 {t1} = {id(t1)}')

l = list()
prev = sys.getsizeof(l)
for _ in range(10):
    c = list(range(_+1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{_+1} items: {size_c}, {delta}', end = '|| ')

print()

t = tuple()
prev = sys.getsizeof(t)
for _ in range(10):
    c = tuple(range(_+1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{_+1} items: {size_c}, {delta}', end = '|| ')

print()
print()

c = list()
prev = sys.getsizeof(0)
print(f'0 items: {prev}', end = '|| ')
for _ in range(10):
    c.append(_)
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{_+1} items: {size_c}, {delta}', end = '|| ')

print()