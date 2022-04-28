from contextlib import contextmanager
import csv

# Config
input_file = 'Project_6/Data/cars.csv'
output_file_path = 'Project_6/Data/'

headers = ('Car', 'MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model', 'Origin')

converters = (str, float, int, float, float, float, float, int, str)

def file_reader(fname):
    global headers
    with open(fname) as f:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        reader = csv.reader(f, dialect=dialect)
        next(reader)
        next(reader)
        yield from reader

def data_parser():
    f = file_reader(input_file)
    for row in f:
        data_row = [converter(item) for converter, item in zip(converters, row)]
        yield data_row

def coroutine(fn):
    def inner(*args, **kwargs):
        gen = fn(*args, *kwargs)
        next(gen)
        return gen
    return inner

@coroutine
def save_data(fname, header):
    fname = output_file_path + fname
    with open(fname, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        while True:
            data = yield
            writer.writerow(data)

@coroutine
def filter_data(gen_next, filt):
    while True:
        data_row = yield
        # print(contains, data_row)
        if filt(data_row):
            gen_next.send(data_row)

@coroutine
def filter_handler(filters):
    name = f"{filters[0]}.csv"
    data = save_data(name, headers)
    for i in range(len(filters)-1, 0, -1):
        for f in filters[i]:
            data = filter_data(data, f)
    while True:
        data_row = yield
        data.send(data_row)

@coroutine
def broadcast(targets):
    while True:
        data_row = yield
        for target in targets:
            target.send(data_row)

@coroutine
def pipeline_coro(*tuples):
    broadcast_targets = []
    for t in tuples:        
        broadcast_targets.append(filter_handler(t))
    broadcaster = broadcast(broadcast_targets)
    while True:
        data_row = yield
        broadcaster.send(data_row)
    

@contextmanager    
def pipeline(*tuples):
    p = pipeline_coro(*tuples)
    try:
        yield p
    finally:
        p.close()

# ((name_tuple, MPG_tuple), (name_tuple, displacement_tuple)

def get_name_tuple(*filters):
    fn_filters = [lambda x, y=filt: y in x[0] for filt in filters]
    return tuple(fn_filters)

def get_mpg_tuple(*filters):
    # f = (val, eq) or (val, l) or (val, g)
    fn_filters = []
    for f in filters:
        if f[1] == 'eq':
            fn = lambda x, y=f[0]: x[1] == y
        elif f[1] == 'l':
            fn = lambda x, y=f[0]: x[1] < y
        else:
            fn = lambda x, y=f[0]: x[1] > y

        fn_filters.append(fn)
    return tuple(fn_filters)

t1 = ('Ford-mpg>20', get_name_tuple('Ford'), get_mpg_tuple((20, 'g')))

with pipeline(t1) as pipe:
    data = data_parser()
    for row in data:
        pipe.send(row)

# name_tuple = get_name_tuple('Chevrolet', 'Carlo')
# rows = [['Chevrolet', 1, 'x'], ['Porche', 1, 'y']]
# for row in rows:
#     print(row)
#     for fn in name_tuple[1]:
#         print(fn)
#         print(fn(row))
# # print(name_tuple)