from collections import namedtuple

def tuplify_dict(dicts):

    keys = {key for dict_ in dicts for key in dict_.keys()}
    Struct = namedtuple('Struct', sorted(keys), rename = True)
    Struct.__new__.__defaults__ = (None, ) * len(Struct._fields)
    return [Struct(**dict_) for dict_ in dicts]

data_list = [{'key1':3, 'key2':4},
             {'key1':1, 'key2':5},
             {'key1':7, 'key2':0, 'key3':18},
             {'key2':100}]

tuple_list = tuplify_dict(data_list)

print('tuple_list: ', tuple_list)
