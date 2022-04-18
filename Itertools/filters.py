from itertools import filterfalse, compress

print(list(filter(lambda x: x<4, [1, 10, 2, 10, 3, 10])))

print(list(filterfalse(lambda x: x<4, [1, 10, 2, 10, 3, 10])))

data = ['a', 'b', 'c', 'd', 'e']
selectors = [True, False, 1, 0]

# return a lazy iterator
print(list(compress(data, selectors)))

def gen_cubes(n):
    for _ in range(n):
        yield (_**3)

isodd = lambda x : x%2 == 1

print(list(filter(isodd, gen_cubes(10))))
print(list(filterfalse(isodd, gen_cubes(10))))

