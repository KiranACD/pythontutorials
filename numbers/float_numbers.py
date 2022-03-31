from fractions import Fraction
import math

a = '22/7'

try:
    print(float(a))
except ValueError as e:
    print('Error while printing float("22/7"): ', e)

a = Fraction(a)
print('Printing "22/7" after converting it to a fraction: ', float(a))

# Testing equality

b = 0.1 + 0.1 + 0.1
c = 0.3
print('Checking equality of (0.1+0.1+0.1) with 0.3: ', b == c)

a = 0.0000001
b = 0.0000002

print('Checking equality of 0.0000001 and 0.0000002 with math.isclose: ', math.isclose(a, b))
print('Checking equality of 0.0000001 and 0.0000002 with math.isclose and setting an absolute tolerance: ', math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-05))
