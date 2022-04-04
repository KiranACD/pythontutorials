l1 = [1, 3, 5, 2, 4]
print('Sorting list = {0}'.format(l1))
print(sorted(l1))

l2 = ['c', 'B', 'D', 'a']
print('Sorting list = {0}'.format(l2))
print(sorted(l2))

print('Case-insensitive sorting of list = {0}'.format(l2))
print(sorted(l2, key=lambda x: x.lower()))

import random

l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reps = 10
print('Shuffling list: {0}'.format(l3))
for _ in range(reps):
    l = [random.random() for i in range(len(l3))]
    print(sorted(l3, key = lambda x: l[x-1]))

l4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print('Shuffling list: {0}'.format(l4))
print(sorted(l4, key=lambda x: random.random()))


