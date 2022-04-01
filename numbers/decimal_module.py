import decimal
from decimal import Decimal
import math

print('Decimal global context: ', decimal.getcontext())

# local contxt vs global context

x = Decimal('1.25')
y = Decimal('1.35')

with decimal.localcontext() as ctx:
    ctx.rounding = decimal.ROUND_HALF_UP
    print('Local context rounding 1.25 half up: ', round(x, 1))
    print('Local context rounding 1.35 half up: ', round(y, 1))

print('Global context rounding 1.25 half up: ', round(x, 1))
print('Global context rounding 1.35 half up: ', round(y, 1))

a = Decimal('0.1234')
b = Decimal('0.1234')

decimal.getcontext().prec = 6
c = a + b
print('sum of 0.1234 with itself when precision is 6: ', c)

with decimal.localcontext() as ctx:
    ctx.prec = 2
    d = a + b
    print('sum of 0.1234 with itself when precision is 2: ', d)

# Integer division and mod operator works differently with decimal object in case of negative numbers

i = -135
j = 4
i_d = Decimal('-135')
j_d = Decimal('4')

print('-135//4: ', i//j)
print('-135%4: ', i%j)
print('Decimal -135//4: ', i_d//j_d)
print('Decimal -135%4: ', i_d%j_d)

num = 2
dec_num = Decimal('2')

root_float = math.sqrt(num)
root_mixed = math.sqrt(dec_num)
root_dec = dec_num.sqrt()

print('Root of 2 in float: ', root_float)
print('Root of 2 in mixed: ', root_mixed)
print('Root of 2 in decimal: ', root_dec)

print('Square of root_float: ', root_float**2)
print('Square of root_mixed: ', root_mixed**2)
print('Square of root_dec: ', root_dec**2)