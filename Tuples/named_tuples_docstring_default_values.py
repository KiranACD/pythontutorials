from collections import namedtuple
from unicodedata import name

# How to change the docs
Point = namedtuple('Point', 'x y')
Point.__doc__ = '2D Cartesian co-ordinate'
Point.x.__doc__ = 'x co-ordinate'
Point.y.__doc__ = 'y co-ordinate'

Vector = namedtuple('Vector', 'x1 y1 x2 y2 x_origin y_origin')

print('Either create a prototype like vector_0')

vector_0 = Vector(0, 0, 0, 0, 0, 0)
print(vector_0)

print('Then use the ._replace to create a new instance from the vector_0 object')

v1 = vector_0._replace(x1 = 20, y1 = 10, x2 = 5, y2 = 2)

print(v1)

print()

print('Or use __default__ method')

Vector = namedtuple('Vector', 'x1 y1 x2 y2 x_origin y_origin')

Vector.__new__.__defaults__ = (0, 0)
v1 = Vector(20, 10, 5, 2)
print('Fields after setting default values for x_origin, y_origin')
print(Vector._fields)
print(v1)


