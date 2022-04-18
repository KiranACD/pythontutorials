from itertools import takewhile, count, product, permutations, combinations, combinations_with_replacement, tee
from fractions import Fraction
from collections import namedtuple

def matrix1(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            yield f'{i} x {j} = {i*j}'

print(list(matrix1(4)))

def matrix2(n):
    for i, j in product(range(1, n+1), range(1, n+1)):
        yield (i, j, i*j)

def matrix3(n):
    return ((i, j, i*j) for i, j in product(range(1, n+1), range(1, n+1)))

print(list(matrix2(4)))
print(list(matrix3(4)))

def matrix4(n):
    return ((i, j, i*j) for i, j in product(*tee(range(1, n+1), 2)))

print(list(matrix4(4)))


def grid(min_val, max_val, step, *, num_dimensions = 2):
    axis = takewhile(lambda x: x<=max_val, count(min_val, step))
    axes = tee(axis, num_dimensions)
    return product(*axes)

print(list(grid(-1, 1, 0.5)))

sample_space = list(product(range(1, 7), range(1, 7)))

outcomes = list(filter(lambda x: x[0] + x[1] == 8, sample_space))

print(len(outcomes)/len(sample_space))
print(Fraction(len(outcomes), len(sample_space)))


suits = 'SHDC'
ranks = tuple(map(str, range(2, 11))) + tuple('JQKA')

Card = namedtuple('Card', 'rank suit')

deck = (Card(rank, suit) for rank, suit in product(ranks, suits))

sample_space = combinations(deck, 4)

total = 0
acceptable = 0

for outcome in sample_space:
    total += 1
    if all(map(lambda x: x.rank == 'A', outcome)):
        acceptable += 1
    
print(Fraction(acceptable, total))


