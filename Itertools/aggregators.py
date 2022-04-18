import os.path
import sys
from numbers import Number


def squares(n):
    for i in range(n):
        yield i**2

print(min(squares(4)))

print(max(squares(4)))

print(bool([None]))

# Exhausted iterators also return True because they do not implement the __len__ or __bool__

class Seq:
    def __init__(self, n):
        self.n = n
    
    def __bool__(self):
        return False
    
    def __len__(sef):
        return self.n

    def __getitem__(self, s):
        pass


s = Seq(5)

print(bool(s))

print(any([0, '', None]))
print(any([1, '', None]))
print(all([[1, 1, 1, 1]]))
print(all([11, 1, 1, 0]))

l1 = [10, 20, 30, 40, 0]
l2 = [10, 20, 30, 40, 'k']
print(f'Are all items of {l1} numbers?', all([isinstance(item, Number) for item in l1]))
print(f'Are all items of {l2} numbers?', all([isinstance(item, Number) for item in l2]))

l3 = ['s', 'r', None, 3]
print(f'Is any item of {l3} number?', any([isinstance(item, Number) for item in l3]))

file_name = 'car-brands-1.txt'
file_path = 'Generators/'

path = os.path.join(file_path, file_name)

with open(path, encoding='latin-1') as f:
    result = all(map(lambda x: len(x)>3, f))

print(result)
