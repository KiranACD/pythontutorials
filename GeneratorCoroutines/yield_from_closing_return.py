from inspect import getgeneratorlocals, getgeneratorstate

def subgen():
    try:
        while True:
            received = yield
            print(received)
    finally:
        print('subgen closing...')

def delegator():
    s = subgen()
    yield from s
    yield 'delegtor subgen closed'
    print('delegator closing...')

def subgen_return():
    try:
        while True:
            received = yield
            print(received)
    except GeneratorExit:
        return 'subgen return value'
    except StopIteration:
        return 'subgen return value'
    finally:
        print('subgen closing...')
        return 'subgen return value'

def delegator1():
    s = subgen_return()
    result = yield from s
    print(result)
    yield result
    print('delegator closing...')

def gen():
    yield 1
    yield 2
    return 3

def dele():
    result = yield from gen()
    yield result

d = delegator()
next(d)
s = getgeneratorlocals(d)['s']
print(getgeneratorstate(d), getgeneratorstate(s))
print('-------------------------------------------------------------')

d.send('hello')
print('-------------------------------------------------------------')

s.close()
print(getgeneratorstate(d), getgeneratorstate(s))
print('-------------------------------------------------------------')

print(next(d))
print(getgeneratorstate(d), getgeneratorstate(s))
print('-------------------------------------------------------------')

try:
    next(d)
    print(getgeneratorstate(d), getgeneratorstate(s))
    print('-------------------------------------------------------------')
except:
    print(getgeneratorstate(d), getgeneratorstate(s))
    print('-------------------------------------------------------------')

d1 = delegator1()
next(d1)
s1 = getgeneratorlocals(d1)['s']
print(getgeneratorstate(d1), getgeneratorstate(s1))
print('-------------------------------------------------------------')

d1.send('hello')
print('-------------------------------------------------------------')

s1.close()
print(getgeneratorstate(d), getgeneratorstate(s))
print('-------------------------------------------------------------')

print(next(d1))
print(getgeneratorstate(d1), getgeneratorstate(s1))
print('-------------------------------------------------------------')

try:
    print(next(d1))
    print(getgeneratorstate(d1), getgeneratorstate(s1))
    print('-------------------------------------------------------------')
except:
    print(getgeneratorstate(d1), getgeneratorstate(s1))
    print('-------------------------------------------------------------')

d2 = dele()
print('1: ', next(d2))
print('2: ', next(d2))
print('3: ', next(d2))
print('4: ', next(d2))