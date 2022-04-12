
li = [1, 2, 3, 4, 5, 6]

print(f'id of li {li} = {id(li)}')

print(f'Changing the frist element of li {li} to "a"')

li[0] = 'a'

print(f'id of li {li} after the change = {id(li)}')

print(f"Clearing the contents of {li} using li.clear()")
li.clear()

print(f'id of li after emptying = {id(li)}')

print('Appending the numbers back again...')
for _ in range(1, 7):
    li.append(_)

print(f'id of li {li} after filling it back up = {id(li)}')

print(f'Using li[0:2] = ("a","b","c","d")...')

li[0:2] = ('a', 'b', 'c', 'd')

print(f'id of li {li} after the change = {id(li)}')

print('li.pop(1)...')
result = li.pop(1)
print(f'id of li {li} after the pop = {id(li)}')

print('del li[1]')
del li[1]
print(f'id of li {li} after the del = {id(li)}')

print(f'li.insert(1, {result})')
li.insert(1, result)
print(f'id of li {li} after the inserts = {id(li)}')

print('l2 = li[:]')
l2 = li[:]
print(f'id of li {li} and id of l2 {l2}')

li.append([100, 200, 300])
print('l3 = li.copy()')
l3 = li.copy()
print('li[-1].append(1000)')
li[-1].append(1000)
print(f'li = {li} and l3 = {l3}')

print('This is called shallow copy, because objects inside th list share the same id.')