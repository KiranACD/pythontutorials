from time import perf_counter
import time


class Timer:
    def __init__(self):
        self.start = perf_counter()
        print('Timer started!')
    
    def __call__(self):
        return perf_counter() - self.start

t = Timer()
time.sleep(5)
print(t())

def timer():
    start = perf_counter()
    print('Timer started!')
    def poll():
        return perf_counter() - start
    return poll

t1 = timer()
time.sleep(5)
print(t1())