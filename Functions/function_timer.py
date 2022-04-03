import time

def time_it(fn, *args, reps = 5, **kwargs):

    start = time.perf_counter()
    for _ in range(reps):
        fn(*args, **kwargs)
    end = time.perf_counter()

    return (end-start)/reps

def powers_of_n(n, *, start = 0, end):

    values = []
    for _ in range(start, end):
        values.append(n**_)
    return values

n = 2
print('Time taken to compute powers of {0} is {1}'.format(n, time_it(powers_of_n, 2, start = 0, end = 10000, reps = 5)))