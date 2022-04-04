import inspect

def func(a, b=1, *args, x = 1, **kwargs):
    print(a, b)

class Demo:
    def demo_func(self, a, b):
        print(a, b)

demo = Demo()
print(dir(func))

print('Function name of func(a, b=1, *args, x = 1, **kwargs): ', func.__name__)
print('Default values of parameters of func(a, b=1, *args, x = 1, **kwargs): ', func.__defaults__)
print('Default values of keyword parameters of func(a, b=1, *args, x = 1, **kwargs): ', func.__kwdefaults__)

print('Variables in func(a, b=1, *args, x = 1, **kwargs): ', func.__code__.co_varnames)
print('Number of variables in func(a, b=1, *args, x = 1, **kwargs): ', func.__code__.co_argcount)


print('Is func(a, b=1, *args, x = 1, **kwargs) a method? ', inspect.ismethod(func))
print('Is func(a, b=1, *args, x = 1, **kwargs) a function? ', inspect.isfunction(func))
print('Is func(a, b=1, *args, x = 1, **kwargs) a routine? ', inspect.isroutine(func))

print('Is demo.demo_func(a, b) a method? ', inspect.ismethod(demo.demo_func))
print('Is demo.demo_func(a, b) a function? ', inspect.isfunction(demo.demo_func))
print('Is demo.demo_func(a, b) a routine? ', inspect.isroutine(demo.demo_func))

print('Source code of function func: ', inspect.getsource(func))
print('Module of function func: ', inspect.getmodule(func))
print('Module of function demo.demo_func: ', inspect.getmodule(demo.demo_func))

print('Signature of function func: ', inspect.signature(func))
print('Signature parameters of function func: ', inspect.signature(func).parameters)