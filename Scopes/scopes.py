a = 10

def my_func1(n):
    c = n**2
    return c

def my_func2(n):
    print('Global variable a: ', a)
    c = a**2
    return c

def my_func3(n):
    a = 20
    print('a is a local variable = ', a)
    c = a**2
    return c

def my_func4(n):
    print('Printing out a and then giving it a local scope = ', a)
    a = 100

print('Only local variables n = {0} and c = {1}'.format(2, my_func1(2)))

print('Local variables are n = {0} and c = {1}'.format(2, my_func2(2)))

print('Local variables are n = {0} and c = {1}'.format(2, my_func3(2)))

print('Trying to print variable a and then giving it a local scope by assigning an object to it.')

try:
    my_func4(10)
except Exception as e:
    print(e)

print('Variable a = {0} outside the function scopes'.format(a))

def outer():
    x = 'hello'
    def inner1():
        x = 'python'
        def inner2():
            nonlocal x
            x = 'monty'
        print('x = {0} before calling the inner2 func'.format(x))
        inner2()
        print('x = {0} after calling the inner2 func'.format(x))
    
    inner1()
    print('x = {0} after calling the inner1 func'.format(x))

outer()