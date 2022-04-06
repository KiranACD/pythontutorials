from time import perf_counter

def timed(reps):
    def timed_inner(fn):
        def inner(*args, **kwargs):
            total_elapsed = 0
            for _ in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                total_elapsed += (perf_counter() - start)
            
            avg_elapsed = total_elapsed/reps
            print('Time taken to run: ', avg_elapsed)
            return result
        return inner
    return timed_inner

def fib_recruse(n):
    return 1 if n<3 else fib_recruse(n-2) + fib_recruse(n-1)

@timed(10)
def fib(n):
    return fib_recruse(n)

def enter_num():

    n = int(input('Enter n for the nth fib number: '))
    return n

if __name__ == '__main__':
    n = enter_num()
    print(fib(n))