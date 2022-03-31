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

# Exploring the round function
print()
print('#----------------------------------------------------------------------------------------------------#')
print()

print('round(18.2): ', round(18.2), type(round(18.2))) # This should return an int
print('round(18.2, 0): ', round(18.2, 0), type(round(18.2, 0)))
print('round(18.2, -1): ', round(18.2, -1), type(round(18.2, -1)))
print('round(18.2, -2): ', round(18.2, -2))

# Bankers rounding rounds to the least significant even number in case of a tie
print('Bankers rounding round(2.5): ', round(2.5))
print('Bankers rounding round(3.5): ', round(3.5))

# To round away from 0 in case of a tie
def round_up(x):
    x = int(x + 0.5*math.copysign(1, x))
    return x

print('round away from 0 round_up(2.5): ', round_up(2.5))
print('round away from 0 round_up(-2.5): ', round_up(-2.5))