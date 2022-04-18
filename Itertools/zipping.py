from itertools import zip_longest

l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4]
l3 = [1, 2, 3]

print(list(zip(l1, l2, l3)))

def integer(n):
    for i in range(n):
        yield i

def squares(n):
    for i in range(n):
        yield i**2

def cubes(n):
    for i in range(n):
        yield (i**3)

iter1 = integer(6)
iter2 = squares(5)
iter3 = cubes(4)

print(list(zip(iter1, iter2, iter3)))

iter1 = integer(6)
iter2 = squares(5)
iter3 = cubes(4)

print(list(zip_longest(iter1, iter2, iter3)))