import os.path
from collections import namedtuple

s = 'I sleep all night, and i work all day'

iter_s = iter(s)

print(next(iter_s))
print(iter_s.__next__())

print()

file_name = 'cars.csv'
file_path = 'Iterators_And_Iterables/'
rel_file_path = os.path.join(file_path, file_name)
path = os.path.abspath(rel_file_path)

cars = []

def cast(data_type, value):
    if data_type == 'DOUBLE':
        return float(value)
    elif data_type == 'INT':
        return int(value)
    else:
        return str(value)

def cast_row(data_types, data_row):

    return (cast(data_type, value) for data_type, value in zip(data_types, data_row))

# with open(rel_file_path) as file:
#     row_index = 0
#     for line in file:
#         if row_index == 0:
#             headers = line.strip('\n').split(';')
#             Car = namedtuple('Car', headers)
#         elif row_index == 1:
#             data_types = line.strip('\n').split(';')
#             print(data_types)
#         else:
#             data = line.strip('\n').split(';')
#             data = cast_row(data_types, data)
#             car = Car(*data)
#             cars.append(car)

#         row_index += 1

with open(rel_file_path) as file:
    # file is an iterable
    iter_file = iter(file)
    headers = next(iter_file).strip('\n').split(';')
    Car = namedtuple('Car', headers)
    data_types = next(iter_file)
    
    cars = [Car(*cast_row(data_types, line.strip('\n').split(';'))) for line in iter_file]
    # for line in iter_file:
    #     data = line.strip('\n').split(';')
    #     data = cast_row(data_types, data)
    #     car = Car(*data)
    #     cars.append(car)

print(cars)