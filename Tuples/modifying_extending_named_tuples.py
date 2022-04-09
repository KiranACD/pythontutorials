from collections import namedtuple

Stock = namedtuple('Stock', 'symbol year month day open high low close')

djia = Stock('DJIA', 2018, 1, 25, 26313, 26458, 26260, 26393)

print(djia)
print('Replacing the day, high and close')
djia = djia._replace(day= 26, high = 26459, close = 26392)
print(djia)

print()

print('To add a new field "prev close" to the Stock class')

print('Current field: ', Stock._fields)

new_fields = Stock._fields + ('previous_close', )
Stockext = namedtuple('Stockext', new_fields)
print('Created a new class called Stockext')
print('New fields: ', Stockext._fields)

djiaext = Stockext(*djia, 26000)
djiaext = Stockext._make(djia + (26000, ))

print('New instance djiaext')
print(djiaext)