# Mandatory keyword arguments

def func(a, b, *args, d):
    print('a = {0}, b = {1}, args = {2} d = {3}'.format(a, b, args, d))

print('Calling func(1, 2, "x", "y", d = 100)')
func(1, 2, 'x', 'y', d=100)

print()
print('Calling func(1, 2, d = 100)')
func(1, 2, d=100)

print()
print('Calling func(1, 2, 100)')
try:
    func(1, 2, 100)
except TypeError as e:
    print(e)

# Forcing no positional arguments - '*' indicates end of positional arguments

def func2(*, d):
    print('d = {0}'.format(d))

print()
print('Calling func2(d=100)')
func2(d = 100)

print()
print('Calling func2(100)')
try:
    func2(100)
except TypeError as e:
    print(e)
