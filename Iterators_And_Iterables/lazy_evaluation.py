import math

class Circle:
    def __init__(self, r):
        self.radius = r
        self._area = None
    
    def __repr__(self):
        return f'Circle(r = {self.radius})'

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None
    
    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * (self.radius ** 2)        
        return self._area
    

class Factorials:
    def __iter__(self):
        return self.FactIter()
    
    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0:
                return NotImplemented
            return math.factorial(s)
        elif isinstance(s, slice):
            start = s.start
            end = s.stop
            step = s.step
            if start == None:
                start = 0
            if step == None:
                step = 1
            if end == None or start < 0 or step < 0:
                return NotImplemented
            return [math.factorial(i) for i in range(start,end,step)]
        else:
            return NotImplemented

    
    class FactIter:
        def __init__(self):
            self.i = 0
        
        def __iter__(self):
            return self
        
        def __next__(self):
            result = math.factorial(self.i)
            self.i += 1
            return result
        
        
if __name__ == '__main__':

    
    for r in range(1, 11):
        circle = Circle(r)
        print(f'Area of {circle} =  {circle.area}')
    
    # fact here is an iterable. We are not going use a for loop over it because its iterator...
    # ...has not implemented the stop iteration.
    fact = Factorials()
    fact_iter = iter(fact)
    for _ in range(11):
        print(next(fact_iter), end = ', ')
    print()
    
    print(fact[5])
    print(fact[:5])
    print(fact[:])
    print(fact[5:2:-1])

