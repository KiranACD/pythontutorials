import math
# ways to create dictionary
d1 = {'a':100, 'b':200}
d2 = dict(a=100, b=200)
d3 = dict([('a', 100), ['b', 200]])

d4 = dict(d1) #d4 is a shallow copy for d1

keys = ['a', 'b']
values = [100, 200, 3]
d5 = {k:v for k, v in zip(keys, values)}
d6 = dict.fromkeys('ab', 0)



print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
print(d6)

print('--------------------------------------------')

print(hash((1,2,3)), hash((1,2,3)))

def my_func(a, b, c):
    print(a, b, c)

print(hash(my_func))

def fn_add(a, b):
    return a+b

def fn_inv(a):
    return 1/a

def fn_mult(a, b):
    return a*b

funcs = {fn_add: (10, 20), fn_inv: (2, ), fn_mult: (2, 8)}

print('--------------------------------------------')

for f in funcs:
    print(f(*funcs[f]))

print('--------------------------------------------')
for f, args in funcs.items():
    print(f(*args))

print('--------------------------------------------')
# Grid of x-y cordinates

x_coords = (-2, -1, 0, 1, 2)
y_coords = (-2, -1, 0, 1, 2)

grid = [(x, y)
        for x in x_coords
        for y in y_coords]
grid_extended = [(x, y, math.hypot(x, y)) for x, y in grid]

grid_extended_dict = {(x,y):math.hypot(x, y) for x,y in grid}

print(grid)
print('--------------------------------------------')
print(grid_extended)
print('--------------------------------------------')
print(grid_extended_dict)
print('--------------------------------------------')

counters = dict.fromkeys('abc', 0)
print(counters)
print('--------------------------------------------')
