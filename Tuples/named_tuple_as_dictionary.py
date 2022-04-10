from collections import namedtuple
from tkinter import N

data_dict = {'key1':100, 'key2':200, 'key3':300}

Data = namedtuple('Data', data_dict.keys())

d1 = Data(*data_dict.values())

d2 = Data(**data_dict)

print('d1: ', d1)
print('d2: ', d2)
key_name = 'key3'
print('Using getattr to get the value of key3 using key_name')
print(getattr(d1, key_name, None))

data_list = [{'key1':3, 'key2':4},
             {'key1':1, 'key2':5},
             {'key1':7, 'key2':0, 'key3':18},
             {'key2':100}]

keys = set()

keys = {key for dict_ in data_list for key in dict_.keys()}

Struct = namedtuple('Struct', sorted(keys))

print('fields in the Struct named tuple: ', Struct._fields)

Struct.__new__.__defaults__ = (None, ) * len(Struct._fields)

s1 = Struct(key3 = 10)
print('s1: ', s1)

tuple_list = []
for dict_ in data_list:
    tuple_list.append(Struct(**dict_))
print('Tuple list from dict list: ', tuple_list)

