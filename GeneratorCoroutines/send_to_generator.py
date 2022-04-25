def echo():
    while True:
        received = yield
        print('You said: ', received)
        break

e = echo()
next(e)
try:
    e.send('hello!')
except:
    pass

def running_averager():
    total = 0
    count = 0
    running_average = None
    while True:
        value = yield running_average
        total += value
        count += 1
        running_average = total/count

def running_averages(iterable):
    averager = running_averager()
    next(averager)
    for value in iterable:
        avg = averager.send(value)
        print('Average: ', avg)

running_averages([1,2,3,4])