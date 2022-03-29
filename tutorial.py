# demonstrating mutability and immutaility

a = 10
b = 10
c = a

print('a is b: ', a is b)
print('a == b: ', a == b)
print('c is b: ', c is b)

l = [1, 2, 3]
m = [1, 2, 3]

print('l is m: ', l is m)
print('l == m: ', l == m)

# integer and string interning.
# integer range = [-5, 256]
# string - that looks like identifier (contains _, letters and numbers only)

a = 10
b = 10
print('a (10) is b (10): ', a is b)

c = 10000
d = 10000
print('c (10000) is d (10000): ', c is d)
print('memory address: ', id(c), id(d))

e = 'hello world'
f = 'hello world'
print('check hello world interning: ', e is f)
