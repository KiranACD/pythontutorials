from contextlib import contextmanager
from time import perf_counter, sleep
import sys

@contextmanager
def timer():
    stats = dict()
    start = perf_counter()
    stats['start'] = start
    try:
        yield stats
    finally:
        end = perf_counter()
        stats['end'] = end
        stats['elapsed'] = end - start

@contextmanager
def out_to_file(fname):
    current_stdout = sys.stdout
    file = open(fname, 'w')
    sys.stdout = file
    try:
        yield None
    finally:
        file.close()
        sys.stdout = current_stdout    

@contextmanager
def open_file(fname, mode='r'):
    f = open(fname, mode)
    try:
        yield f
    finally:
        f.close()

with timer() as stats:
    sleep(2)

print(stats)

with out_to_file('ContextManagers/Data/test4.py'):
    print('NCIS', end='')

with open_file('ContextManagers/Data/test4.py') as f:
    print(f.readlines())