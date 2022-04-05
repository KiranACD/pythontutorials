from functools import reduce
def _reduce(fn, sequence):
    result = sequence[0]
    for e in sequence[1:]:
        result = fn(result, e)
    return result

l = [1, 2, 9, 3, 4, 10, 12, 0]
print('Max of list l = {0} using the reduce function is...'.format(l))
print(_reduce(max, l))

print('Min of list l = {0} using the reduce function is...'.format(l))
print(_reduce(min, l))

print(reduce(lambda x, y: x + ' ' + y, ('python', 'is', 'awesome')))