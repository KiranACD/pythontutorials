import sys
print(sys.path)

import math
print(math)

import fractions
print(fractions)

print(globals())

# print(sys.modules)
print(sys.modules['math'])
print(fractions.__file__)
print(fractions.__dict__['__file__'])

print('Python looks for modules in the paths shown in sys.path')
print(sys.path)