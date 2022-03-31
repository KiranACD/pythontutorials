from fractions import Fraction

# approximating irrational number using float and hence expressing them in fraction

print('Fraction reprsentation of sqrt(2): ', Fraction(2**0.5))

a = 0.125
b = 0.3
c = 0.1

print('Fraction representation of 0.125: ', Fraction(a))
print('Fraction representation of 0.3: ', Fraction(b))

print('25 digits of 0.3: ', format(b, '0.25f'))
print('25 digits of 0.1: ', format(c, '0.25f'))