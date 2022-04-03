# using packing, unpacking to swap variables

a, b = 10, 20
print('a and b is {0} and {1} before swap'.format(a, b))
a, b = b, a
print('a and b is {0} and {1} after swap'.format(a, b))

print()
print('To create a tuple with a single value we can define t = 1, ')
t = 1, 
print('The tuple is {0} and type is {1}'.format(t, type(t)))

print()
print('Unordered storage of keys in sets and dictionaries')
s = {1, 2, 3}
n = 5
for _ in range(n):
    i, j, k = s
    print('i = {0}, j = {1}, k = {2}'.format(i, j, k))

print()
print('Unordered storage of keys in sets and dictionaries')
d = {'key1': 1, 'key2': 2, 'key3': 3}
n = 5
for _ in range(n):
    l, m, n = d
    print('l = {0}, m = {1}, n = {2}'.format(l, m, n))

ss = {'p', 'y', 't', 'h', 'o', 'n'}
s_string = 'python'
print('String python in set: ', ss)

# Using the * operator

s_0, *s_r = s_string
print('s[0] of "python" = {0}, rest of the string = {1}'.format(s_0, s_r))

print()
d = {'a': 1, 'b': 2, 'c': 4}
print('Dictionary d is: ', d)
e = {**d, 'a':10}
print('Dictionary e combined with d using e = {**d, "a":10}: ', e)

