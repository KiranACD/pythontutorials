class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'

a = 1, 2, 3, 4, 5, 6
x, *_, y, z = a

print(f'first and last elements of tuple {a} is {x}, {y}, {z}')

try:
    a[0] = 3
except Exception as e:
    print(f'Error while trying to change first element of {a} is {e}')

b = (Point(1, 2), Point(10, 20))

print('The tuple itself cannot be changed. But if the first element of the tuple is a data type that is mutable, then that can be changed!')
print(b)
b[0].x = 100
print(b)

print('When you extend a tuple, a new tuple is created')
c = 1, 2, 3
print(c, id(c))
c = c + (4, 5)
print(c, id(c))