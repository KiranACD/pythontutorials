from decimal import Decimal

li = [1, 2, 3, 4]
tu = (1, 2, 3, 4)
st = 'python'
# Now supports ordering
se = {1, 2, 3, 4, 5, 6, 100, 102, 7, 8, 9}
d = {'a':1, 'b':2}

for c in st:
    print(c, end=' ')

print()

for e in se:
    print(e, end=' ')

print()
try:
    tu[0] = 100
except TypeError as e:
    print(e)

print(f'length of list {li} = {len(li)}')
print(f'length of tuple {tu} = {len(tu)}')
print(f'length of string {st} = {len(st)}')
print(f'length of dict {d} = {len(d)}')

# Cannot concatenate 2 different type of sequences
try:
    con = li + tu
except Exception as e:
    print(e)

s = "gnu's not unix"
print(list(enumerate(s)))

# Slicing
print(f'li = {li}, li[1:2] = {li[1:2]}')
print(f'tu = {tu}, tu[1:4] = {tu[1:4]}')
print(f'st = {st}, st[0:5:2] = {st[0:5:2]}')
print(f'st = {st}, st[::-1] = {st[::-1]}')

li_d = [Decimal(10.5)]
li_d1 = li_d * 2
li_d1[0] = Decimal('10.6')
print(li_d1)
