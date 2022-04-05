from functools import partial

def pow(base, exponent):
    return base**exponent

square = partial(pow, exponent=2)
cube = partial(pow, exponent=3)

print('Square of 5 using square partial function = {0}'.format(square(5)))
print('Cube of 5 using cube partial function = {0}'.format(cube(5)))

origin = (0, 0)

points = [(1, 2), (2, 0), (3, 2), (-3, -4), (10, 20), (10, 0)]

distance = lambda a, b: (a[0] - b[0])**2 + (a[1] - b[1])**2

f = partial(distance, origin)

print('Sorting points = {0} based on distance from origin\nwe get points = {1}'.format(points, sorted(points, key=f)))