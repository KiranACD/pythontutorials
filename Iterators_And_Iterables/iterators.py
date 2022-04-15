import random

# To restart iteration, create new object of the class
class Squares:
    def __init__(self, length):
        self._length = length
        self._numbers = [i for i in range(self._length)]
    
    def __len__(self):
        return self._length
    
    def __iter__(self):
        return self.SquaresIterator(self)
    
    # Implementing the sequence protocol
    def __getitem__(self, s):
        return self.__numbers[s] **2

    class SquaresIterator:

        def __init__(self, sq):
            self._sq = sq
            self._i = 0
        
        # The next and iter functions make this class an iterator.
        def __next__(self):

            if self._i >= len(self._sq):
                raise StopIteration
            
            else:
                result = self._sq._numbers[self._i] ** 2
                self._i += 1
                return result
        
        def __iter__(self):
            return self
    

class RandomNumbers:

    def __init__(self, length, *, range_min = 0, range_max = 10):
        self._length = length
        self._range_min = range_min
        self._range_max = range_max
    
    def __len__(self):
        return self._length
    
    def __iter__(self):
        return RandomNumbersIterator(self)

class RandomNumbersIterator:
    def __init__(self, rand):
        self._rand = rand
        self._num_requested = 0
    
    def __next__(self):
        if self._num_requested >= len(self._rand):
            raise StopIteration
        else:
            self._num_requested += 1
            return random.randint(self._rand._range_min, self._rand._range_max)
    
    def __iter__(self):
        return self

if __name__ == '__main__':

    squares = Squares(10)
    # square_iterator = SquaresIterator(numbers)

    for sq in squares:
        print(sq, end=', ')

    print()
    print()

    random_numbers = RandomNumbers(10)

    for num in random_numbers:
        print(num, end=', ')
    
    print()
    print(sorted(random_numbers))
    print()

