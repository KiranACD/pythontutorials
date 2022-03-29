import time
import sys

def compare_using_equality(n):
    a = 'this is a long string' * 200
    b = 'this is a long string' * 200
    print('memory address in equality: ', id(a), id(b))
    for _ in range(n):
        if a == b:
            pass

def compare_using_interning(n):
    a = sys.intern('this is a long string' * 200)
    b = sys.intern('this is a long string' * 200)
    print('memory address in interning: ', id(a), id(b))
    for _ in range(n):
        if a == b:
            pass

if __name__ == '__main__':
    start = time.perf_counter()
    compare_using_equality(10000000)
    end = time.perf_counter()
    print('time using equality: ', end-start)

    start = time.perf_counter()
    compare_using_interning(10000000)
    end = time.perf_counter()
    print('time using equality: ', end-start)
    
