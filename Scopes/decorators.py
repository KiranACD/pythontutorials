from functools import wraps

c = {}
def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('function_name: ', fn.__name__, 'count: ', count)
        return fn(*args, **kwargs)
    
    return inner

def add(a, b):
    '''
    return a+b
    '''
    return a+b

x = id(add)
add = counter(add)
y = id(add)
print('Id of add before decorating = {0} and id of add after decorating = {1}'.format(x,y))

@counter
def my_func(a: str, b: int)-> str:
    '''
    returns a string a multiplied b times
    '''
    return a*b

print('string {0} mutiplied {1} times = {2}'.format('abc', 3, my_func('abc', 3)))



