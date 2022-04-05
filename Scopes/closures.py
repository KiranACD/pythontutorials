def outer():
    x = 'python'
    def inner():
        print('{0} rocks!'.format(x))
    
    return inner

fn = outer()
print('Inner closure free variables: ', fn.__code__.co_freevars)
print('Inner closure itself: ', fn.__closure__)

def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

fn1 = counter()

n = 5
for _ in range(n):
    print('Calling the inner function: ', _)
    print(fn1())


def incrementer(n):
    def counter(start):
        current = start
        def inc():
            nonlocal current
            current += n
            return current
        return inc
    return counter

incrementer1 = incrementer(1)
inc10 = incrementer1(10)
inc20 = incrementer1(20)
print('inc10 with incrementer1: ', inc10())
print('inc20 with incrementer1: ', inc20())
print('inc10 with incrementer1: ', inc10())
print('inc20 with incrementer1: ', inc20())

def create_adders(i):
    
    def adder(x):
        return x + i
    
    return adder

adders = []
for _ in range(5):
    adders.append(create_adders(_))

def create_adders1(n):
    adders = []
    for _ in range(n):
        def adder(x, y=_):
            return x + y
        adders.append(adder)
    return adders

adders = create_adders1(5)

print('adders[0](10): ', adders[0](10))
print('adders[1](10): ', adders[1](10))
print('adders[2](10): ', adders[2](10))
print('adders[3](10): ', adders[3](10))

print('Is this adder a closure? ', bool(adders[0].__closure__))