# Positional parmeters and default parameters

def my_func(a, b, c = 10):
    print('a = {0}, b = {1}, c = {2}'.format(a, b, c))

print('Calling my_func(1, 2, 3)')
my_func(1, 2, 3)

print('Calling my_func(1, 2)')
my_func(1, 2)

print('Calling my_func(1, 2, c = 20)')
my_func(1, 2, c = 20)

print('Calling my_func(b = 20, a = 30)')
my_func(b = 20, a = 30)

print('Calling my_func(c = 50, a = 5, b = 10)')
my_func(c = 50, a = 5, b = 10)