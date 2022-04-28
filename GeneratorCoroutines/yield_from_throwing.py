class CloseCoroutine(Exception):
    pass

class IgnoreMe(Exception):
    pass

def echo():
    try:
        while True:
            received = yield
            print(received)
    except CloseCoroutine:
        return 'coro was closed'
    except GeneratorExit:
        print('gen closed')

def echo_():
    output = None
    try:
        while True:
            try:
                received = yield output
                print(received)
            except IgnoreMe:
                output = 'Ignore me'
            else:
                output = None
    except CloseCoroutine:
        return 'coro was closed'
    except GeneratorExit:
        print('gen closed')
    

def delegator():
    result = yield from echo()
    print(result)
    yield result
    print('Delegator closing')

def delegator1():
    try:
        result = yield from echo_()
        print(result)
        yield result
        print('Delegator closing')
    except CloseCoroutine:
        print('delegator caught CloseCoroutine')        

# d = delegator()
# next(d)
# print(d.throw(GeneratorExit))
# # print(d.throw(CloseCoroutine))

d1 = delegator1()
next(d1)
d1.send('python')
print(d1.throw(IgnoreMe))
d1.send('rocks')
print(d1.throw(CloseCoroutine))
#       print(next(d1))
