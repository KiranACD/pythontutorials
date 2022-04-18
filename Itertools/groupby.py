from itertools import groupby, islice
from collections import defaultdict
import os.path

file_name = 'cars_2014.csv'
file_path = 'Itertools/'
path = os.path.join(file_path, file_name)

make_dict = defaultdict(int)
with open(path) as f:
    for row in islice(f, 20):
        print(row, end='')

with open(path) as f:
    next(f)
    for row in f:
        row = row.strip('\n').split(',')
        make_dict[row[0]] += 1

print(make_dict)

data = (1, 2, 2, 2, 3)
print(list(groupby(data)))

it = groupby(data)
for key, sub_iter in it:
    print(key, list(sub_iter))

data = ((1, 'abc'), (1, 'bcd'), (2, 'pyt'), (2, 'yth'), (2, 'tho'), (3, 'hon'))

groups = groupby(data, key = lambda x: x[0])

for key, group in groups:
    print(key, list(group))

with open(path) as f:
    next(f)            
    make_groups = groupby(f, key=lambda x: x.split(',')[0])
    print(make_groups)
    make_count = ((key, sum(1 for i in group)) for key, group in make_groups)
    print(list(make_count))

