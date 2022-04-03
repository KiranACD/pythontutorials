def my_func1(a, b, c):
    print('a = {0}, b = {1}, c = {2}'.format(a, b, c))

def my_func2(a, b, *args):
    print('a = {0}, b = {1}, args={2}'.format(a, b, args))

def avg(*args):
    count = len(args)
    return count and sum(args)/count

l = [10, 20, 30]
print('Calling my_func1(*l)')
my_func1(*l)

print()
x, y = 1, 2
li = [1, 2, 3]
print('Calling my_func2(x, y, li)')
my_func2(x, y, li)

print()
print('Calling my_func2(x, y, *li)')
my_func2(x, y, *li)

print()
print('Getting average of list {0}'.format(li))
print(avg(*li))