from random import uniform
from math import sqrt

def random_shot(radius):
    random_x = uniform(-radius, radius)
    random_y = uniform(-radius, radius)

    if ((random_x ** 2) + (random_y ** 2)) ** 0.5 <= radius:
        is_in_circle = True
    else:
        is_in_circle = False
    
    return (random_x, random_y), is_in_circle

if __name__ == '__main__':
    num = int(input('Enter the number of attempts: '))
    radius = int(input('Enter the radius of circle: '))

    count_inside = 0
    for _ in range(num):
        count_inside += random_shot(radius)[1]
    
    print(f'pi approximately = {(count_inside/num)*4}')
