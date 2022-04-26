from inspect import getgeneratorlocals, getgeneratorstate

def echo_receive():
    while True:
        received = yield
        print(received[::-1])

def delegator():
    e = echo_receive()
    yield from e

def echo_receive_send():
    output = None
    while True:
        received = yield output
        output = received[::-1]

def delegator1():
    e = echo_receive_send()
    yield from e

d = delegator()
next(d)
e = getgeneratorlocals(d)['e']

print(getgeneratorstate(d), getgeneratorstate(e))

d.send('stressed')
d.send('tons')

print('----------------------------------------------')

d1 = delegator1()
next(d1)
e1 = getgeneratorlocals(d1)['e']

print(getgeneratorstate(d1), getgeneratorstate(e1))

result1 = d1.send('stressed')
result2 = d1.send('tons')
print(result1, result2)

print('----------------------------------------------')

