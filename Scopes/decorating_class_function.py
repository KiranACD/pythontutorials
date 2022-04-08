# Monkey patching with a function
# complete ordering also done using total_ordering from functools
from datetime import datetime
from multiprocessing.sharedctypes import Value

def dec_class(cls):
    cls.speak = lambda self, message: '{0} says : {1}'.format(self.__class__.__name__, message)
    return cls
    

def info(self):
    results = []
    results.append('time: {0}'.format(datetime.now()))
    results.append('Class: {0}'.format(self.__class__.__name__))
    results.append('id: {0}'.format(hex(id(self))))

    for k, v in vars(self).items():
        results.append('{0}: {1}'.format(k, v))
    
    return results

def debug_info(cls):    

    cls.debug = info

    return cls

@dec_class
@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    
    def say_hi(self):
        return 'Hello there!'

@debug_info
class Automobile:
    def __init__(self, make, model, year, top_speed):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._speed = 0

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, new_speed):
        if new_speed > self.top_speed:
            raise ValueError('Speed cannot exceed top speed')
        else:
            self._speed = new_speed

def complete_ordering(cls):
    if '__eq__' in dir(cls) and '__lt__' in dir(cls):
        cls.__le__ = lambda self, other: self < other or self == other
        cls.__gt__ = lambda self, other: not (self < other) and not (self == other)
        cls.__ge__ = lambda self, other: not (self < other)
    
    return cls

@debug_info
@complete_ordering
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __repr__(self):
        return '{0}({1}, {2})'.format(self.__class__.__name__, self.x, self.y)
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False
    
    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented


if __name__ == '__main__':
    p = Person('John', 1939)
    # Person = dec_class(Person)
    print(p.speak('This works'))
    print(p.debug())

    my_car = Automobile('Ford', 'Model T', 1908, 45)
    
    print(my_car.debug())

    my_car.speed = 40

    print(my_car.debug())

    p1 = Point(0, 0)
    p2 = Point(1, 2)
    p3 = Point(1, 2)
    p4 = Point(20, 25)

    print('p1<p2: ', p1<p2)
    print('p2==p3: ', p2==p3)
    print('p4>=p3: ', p4>=p3)
    print(p4.debug())
    print(p4)

