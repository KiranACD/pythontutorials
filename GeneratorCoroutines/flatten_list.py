def flatten_print(curr_item):
    if isinstance(curr_item, list):
        for item in curr_item:
            flatten_print(item)
    else:
        print(curr_item)

def flatten_to_list(curr_item, output):
    if isinstance(curr_item, list):
        for item in curr_item:
            flatten_to_list(item, output)
    else:
        output.append(curr_item)

def flatten_gen(curr_item):
    if isinstance(curr_item, list):
        for item in curr_item:
            yield from flatten_gen(item)
    else:
        yield curr_item

def is_iterable(item, *, str_is_iterable=True):
    try:
        iter(item)
    except:
        return False
    else:
        if isinstance(item, str):
            if str_is_iterable and len(item) > 1:
                return True
            else:
                return False
        else:
            return True

def flatten_iterable(curr_item, *, str_is_iterable=False):
    if is_iterable(curr_item, str_is_iterable=str_is_iterable):
        for item in curr_item:
            yield from flatten_iterable(item)
    else:
        yield(curr_item)

l = [1, 2, [3], [4, 5], [6, 7, 8]]
flatten_print(l)

print('------------------------------------------')

output = []
flatten_to_list(l, output)
print(output)

print('------------------------------------------')

for item in flatten_gen(l):
    print(item)

print('------------------------------------------')

print(list(flatten_gen(l)))

print('------------------------------------------')

l1 = [1, 2, 3, (4, 5), {6, 7, 8}, (9, 10, [11, 12])]
print(list(flatten_iterable(l1)))

print('------------------------------------------')

l1 = [1, 2, 3, (4, 5), {6, 7, 8}, (9, 10, [11, 12]), 'abc']
print(list(flatten_iterable(l1)))
