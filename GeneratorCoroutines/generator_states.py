from inspect import getgeneratorstate

def gen(s):
    for c in s:
        print(getgeneratorstate(g))
        yield c

g = gen('abc')
print(getgeneratorstate(g))
print(next(g))
print(getgeneratorstate(g))
print(next(g))
print(getgeneratorstate(g))
print(next(g))
print(getgeneratorstate(g))
# When you run it once more, the iteration is over and it raises a StopIteration exception.
try:
    print(next(g))
except Exception as e:
    print('StopIteration')
    print(getgeneratorstate(g))