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