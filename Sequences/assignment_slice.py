

l = [1, 2, 3, 4, 5]
print(f'{l} has id {id(l)}')

l[0:3] = 'python'

print("l[0:3] = 'python'")
print(f'{l} now has id {id(l)}')

l[0:3] = []

print("l[0:3] = []")
print(f'{l} now has id {id(l)}')

l[1:1] = 'python'

print("l[1:1] = 'python'")
print(f'{l} now has id {id(l)}')

l[0:7:2] = 'abcd'
print("l[0:7:2] = 'abcd'")
print(f'{l} now has id {id(l)}')