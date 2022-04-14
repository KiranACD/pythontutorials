import random
from time import sleep

# Returns a closure
def counter():
    i = 0

    def inc():
        nonlocal i
        i += 1
        return i
    
    return inc

def countdown(start = 10):
    def run():
        nonlocal start
        sleep(1)
        start -= 1
        return start
    return run 

class CallableIterator:
    
    def __init__(self, fn, sentinel):
        self.fn = fn
        self.sentinel = sentinel
        self.is_consumed = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_consumed:
            raise StopIteration
        result = self.fn()
        if result == self.sentinel:
            self.is_consumed = True 
            raise StopIteration
        else:
            return result

if __name__ == '__main__':

    cnt = counter()
    cnt_iterator = CallableIterator(cnt, 5)

    for c in cnt_iterator:
        print(c, end=', ')
    print()

    cdown = countdown(10)
    cdown_iterator = CallableIterator(cdown, -1)

    for c in cdown_iterator:
        print(c)
    print()

        
    
