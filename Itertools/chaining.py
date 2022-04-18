from itertools import chain, tee

def get_gens():
    print('yielding from 1st')
    l1 = (i**2 for i in range(4))
    print('yielding from 2nd')
    l2 = (i**2 for i in range(4, 8))
    print('yielding from 3rd')
    l3 = (i**2 for i in range(8, 12))
    return l1, l2, l3

for gen in get_gens():
    for item in gen:
        print(item, end=' ')

print()

def chain_iterables(*iterables):
    print(iterables)
    for iterable in iterables:
        yield from iterable

for item in chain_iterables(*get_gens()):
    print(item, end = ' ')

print()

for item in chain(*get_gens()):
    print(item, end = ' ')

print()

for item in chain.from_iterable(get_gens()):
    print(item, end = ' ')

print()

