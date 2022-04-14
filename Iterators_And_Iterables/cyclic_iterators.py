
from itertools import cycle


class CyclicIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        result = self.lst[self.i % len(self.lst)]
        self.i += 1
        return result

    def __getitem__(self, s):
        return self.lst[s % len(self.lst)]


class CyclicIteratorGen:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(self.iterable)

    def __iter__(self):
        return self
    
    def __next__(self):
        # try:
        #     return next(self.iterator)
        # except StopIteration:
        #     self.iterator = iter(self.iterable)
        #     return next(self.iterator)
        
        try:
            item =  next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            item = next(self.iterator)
        finally:
            return item
    
    def __getitem__(self, s):
        if isinstance(self.iterable, set) or isinstance(self.iterable, dict):
            raise TypeError(f'Type {type(self.iterable)} not indexed.')
        else:
            return self.iterable[s % len(self.iterable)]
        





if __name__ == '__main__':

    c = CyclicIterator('NESW')
    for _ in range(10):
        print(c[_], end = ' ')
    
    print()

    c = CyclicIterator('NSWE')
    n = 10
    num_dir = [f'{i}{c[i-1]}' for i in range(1, n+1)]
    print(num_dir)

    c = CyclicIterator('NSWE')
    num_dir = [str(number) + direction for number, direction in zip(range(1, n+1), c)]
    print(num_dir)

    try:
        c = CyclicIteratorGen({'N', 'S', 'W', 'E'})
        n = 10
        num_dir = [f'{i}{c[i-1]}' for i in range(1, n+1)]
        print(num_dir)
    except Exception as e:
        print(e)
    
    c = CyclicIteratorGen({'N', 'S', 'W', 'E'})
    num_dir = [str(number) + direction for number, direction in zip(range(1, n+1), c)]
    print(num_dir)

