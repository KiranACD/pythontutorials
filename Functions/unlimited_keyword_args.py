def func(*, d, **kwargs):
    print('d = {0}, kwargs = {1}'.format(d, kwargs))

print('Calling func(d = 10, e = 11, f = 12)')
func(d = 10, e = 11, f = 12)

def func2(**kwargs):
    print('kwargs = {0}'.format(kwargs))

print('Calling func2(10)')
try:
    func2(10)
except TypeError as e:
    print(e)

print('Calling func2(a = 1)')
func2(a = 10)

def func3(*args, **kwargs):
    print('args = {0}, kwargs = {1}'.format(args, kwargs))

print('func3(*args, **kwargs)')
print('Calling func3(a = 10, b = 11)')
func3(a = 10, b = 11)
