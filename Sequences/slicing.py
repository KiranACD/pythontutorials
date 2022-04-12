
s = slice(0, 2)
l = [1, 2, 3, 4, 5]
print(f'{s} of {l} is {l[s]}')

s = slice(8, -1, -1).indices(10)
print(f'For slice {s}, start = {s[0]}, end = {s[1]}')