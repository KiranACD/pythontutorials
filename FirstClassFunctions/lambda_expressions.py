def apply_func(x, fn):
    return fn(x)

print(apply_func(2, lambda x: x**2))

f = lambda x, y=10: x+y

print(f(10))

g = lambda x, *args, y, **kwargs: (x, *args, y, {**kwargs})

print(g(1, 'x', 'y', y = 10, a = 100, b = 200))