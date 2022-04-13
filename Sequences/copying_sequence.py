from copy import copy, deepcopy

# deepcopy is used to copy any object that has mutiple layers of other object within it.
# ways to shallow copy

l1 = [1, 2, 3]
l2 = list(l1)
l3 = l1[:]
l4 = l1.copy()

l5 = [e for e in l1]

print(f'id l1 = {id(l1)}, id l2 = {id(l2)}, id l3 = {id(l3)}, id l4 = {id(l4)}, id l5 = {id(l5)}')

# for tuples, these ops will return same object?

print()
t1 = (1, 2, 3)
t2 = tuple(t1)
t3 = t1[:]
t4 = copy(t1)

print(f'id t1 = {id(t1)}, id t2 = {id(t2)}, id t3 = {id(t3)}, id l4 = {id(t4)}')

print()
a = [1, 2, 3]
b = [1, 2, 3]

print(f'id(a) = {id(a)}, id(b) = {id(b)}')
tuple_a = tuple(a)
tuple_b = tuple(a)

print(f'id(tuple_a) = {id(tuple_a)}, id(tuple_b) = {id(tuple_b)}')

print()

