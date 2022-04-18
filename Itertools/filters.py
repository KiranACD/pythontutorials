from itertools import filterfalse, compress, takewhile, dropwhile
from math import sin, pi

print(list(filter(lambda x: x<4, [1, 10, 2, 10, 3, 10])))

print(list(filterfalse(lambda x: x<4, [1, 10, 2, 10, 3, 10])))

data = ['a', 'b', 'c', 'd', 'e']
selectors = [True, False, 1, 0]

# return a lazy iterator
print(list(compress(data, selectors)))

# compress the same as 
print([item for item, selector in zip(data, selectors) if selector])


def gen_cubes(n):
    for _ in range(n):
        yield (_**3)

isodd = lambda x : x%2 == 1

print(list(filter(isodd, gen_cubes(10))))
print(list(filterfalse(isodd, gen_cubes(10))))

def sine_wave(n):
    start = 0
    end = 2*pi
    step = (end-start)/(n-1)

    for _ in range(n):
        yield round(sin(start), 2)
        start += step

print(list(takewhile(lambda x: x<0.9, sine_wave(15))))
print(list(dropwhile(lambda x: x<0.9, sine_wave(15))))
