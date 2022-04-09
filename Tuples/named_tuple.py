# Named tuple is a function that acts as a class factory and the function returns classes.
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

pt1 = Point(10, 20)

print('Point: ', pt1)

print('Is pt1 a tuple? ', isinstance(pt1, tuple))

print()

print('Since this inherits properties of the tuple, the equality method between two instances is already implemented.')
pt2 = Point(10, 20)
print('Is pt1 pt2? ', pt1 is pt2)
print('pt1 == pt2? ', pt1 == pt2)

print()

print('Converting pt2 to an ordered dict')
print(pt2._asdict())
