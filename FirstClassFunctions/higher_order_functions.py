l = [2, 3, 4]

sq = lambda x: x**2

print('Apply sq function to list = {0} using the map function'.format(l))
print(list(map(sq, l)))

l1 = [1, 2 ,3]
l2 = [10, 20, 30]

print('Adding l1 = {0} and l2 = {1} using the map function'.format(l1, l2))
print(list(map(lambda x, y: x + y, l1, l2)))

l3 = [0, 1, 2, 3, 4, 5]
print('Keep all elements of the list l3 = {0} that are truthy'.format(l3))
print(list(filter(None, l3)))

print('Keep all elements of the list l3 = {0} that are even'.format(l3))
print(list(filter(lambda x: x%2==0, l3)))

print('Zipping up l1 = {0} and l3 = {1}'.format(l1, l3))
print(list(zip(l1, l3)))
