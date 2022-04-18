from itertools import tee

# to copy iterators

def squares(n):
    for _ in range(n):
        yield (_**2)

gen = squares(5)

iters = tee(gen, 3)

l = [1, 2, 3, 4]

lists = tee(l, 2)

print(lists[0])
print(lists[1])
print(lists[0])

