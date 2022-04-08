# Monkey Patching

from fractions import Fraction

f = Fraction(2, 3)
print(f.numerator)
print(f.denominator)

Fraction.speak = lambda self, message: 'Fraction says {0}'.format(message)

print(f.speak('I can speak'))

Fraction.is_integral = lambda self: self.denominator == 1

f1 = Fraction(6, 3)
f2 = Fraction(7, 2)
print(f1.is_integral())
print(f2.is_integral())