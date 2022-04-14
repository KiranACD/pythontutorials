import random

# To restart iteration, create new object of the class
class Squares:
    def __init__(self, length):
        self.i = 0
        self._length = length
    
    def __len__(self):
        return self._length

    # The next and iter functions make this class an iterator.
    def __next__(self):

        if self.i >= self._length:
            raise StopIteration
        
        else:
            result = self.i ** 2
            self.i += 1
            return result
    
    def __iter__(self):
        return self



class RandomNumbers:

    def __init__(self, length, *, range_min = 0, range_max = 10):
        self._length = length
        self._range_min = range_min
        self._range_max = range_max
        self.num_requested = 0
    
    def __len__(self):
        return self._length

    def __next__(self):
        if self.num_requested >= self._length:
            raise StopIteration
        else:
            self.num_requested += 1
            return random.randint(self._range_min, self._range_max)
    
    def __iter__(self):
        return self
            
            
        
if __name__ == '__main__':
    sq = Squares(10)
    while True:
        try:
            print(next(sq), end=', ')
        except StopIteration:
            print()
            print('Squares collection exhausted')
            break
        
    
    print()
    
    numbers = RandomNumbers(10)
    while True:
        try:
            print(next(numbers), end=', ')
        except:
            print()
            print('Random Numbers collection exhausted')
            break
    
    print()

    numbers = RandomNumbers(10)
    print(sorted(numbers, reverse=True))
    print()
