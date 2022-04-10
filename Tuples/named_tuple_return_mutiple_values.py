from collections import namedtuple
from random import randint, random
from collections import namedtuple

Colour = namedtuple('Colour', 'red green blue alpha')

def random_colour():

    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    alpha = round(random(), 2)

    return Colour(red, green, blue, alpha)

colour = random_colour()

print('Printing out colour.red')
print(colour.red)
print('Printing out colour')
print(colour)

