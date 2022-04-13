import dis
from math import factorial

squares = [i**2 for i in range(1, 101)]

print(squares)

squares = [i**2 for i in range(1, 101) if i%2 == 0]

print(squares)

print()

compiled_code = compile('[i**2 for i in (1, 2, 3)]', filename='string', mode='eval')

print(dis.dis(compiled_code))

print()

# i is a free variable in this closure
table = [[(i*j) for j in range(1, 11)] for i in range(1, 11)]

for t in table:
    print(t)

print()

def combo(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

size = 10
binomial = [[combo(n, k) for k in range(n+1)] for n in range(1, size+1)]

for t in binomial:
    print(t)

print()

funcs = [lambda x, p=i: x**p for i in range(5)]

print(funcs[1](10))