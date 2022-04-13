l1 = [1, 2, 3, 4]
l2 = [5, 6, 7]

print(f'list {l1} has id {id(l1)}')
print(f'list {l2} has id {id(l2)}')

l1 = l1 + l2

print(f'After l1 + l2, list {l1} has id {id(l1)}')

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7]

print(f'list {l1} has id {id(l1)}')
print(f'list {l2} has id {id(l2)}')

l1 += l2

print(f'After l1 += l2, list {l1} has id {id(l1)}')

t1 = (1, 2, 3, 4)
t2 = (5, 6, 7)

print()

print(f'list {t1} has id {id(t1)}')
print(f'list {t2} has id {id(t2)}')

t1 += t2

print(f'After t1 += t2, list {t1} has id {id(t1)}')

print()
l1 = [1, 2, 3, 4]

print(f'list {l1} has id {id(l1)}')

l1 = l1 * 2

print(f'After l1 * 2, list {l1} has id {id(l1)}')

l1 = [1, 2, 3, 4]

print(f'list {l1} has id {id(l1)}')

l1 *= 2

print(f'After l1 *= 2, list {l1} has id {id(l1)}')

l1 = [1, 2, 3, 4]
l1[0:4:2] = [10, 30]
print(l1)
