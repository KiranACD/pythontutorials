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
def filter_data_name(gen_next, contains):
    while True:
        data_row = yield
        # print(contains, data_row)
        if contains in data_row[0]:
            gen_next.send(data_row)

@coroutine
def name_filter_handler(*filters):
    name = f"{'-'.join(filters)}.csv"
    data = save_data(name, headers)
    for i in range(len(filters)-1, -1, -1):
        print(filters[i])
        data = filter_data_name(data, filters[i])
    while True:
        data_row = yield
        data.send(data_row)
            
@coroutine
def process_pipeline(on_header, *filters):
    if on_header == 'name':
        name = name_filter_handler(*filters)
    while True:
        data = yield        
        name.send(data)

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
        if t[0] == 'name':
            broadcast_targets.append(name_filter_handler(*t[1:]))
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
    return ('name', fn_filters)

def get_mpg_tuple(f):
    # f = (val, eq) or (val, l) or (val, g)
    if f[1] == 'eq':
        fn = lambda x, y=f[0]: x[1] == y
    elif f[1] == 'l':
        fn = lambda x, y=f[0]: x[1] < y
    else:
        fn = lambda x, y=f[0]: x[1] > y
    
    return ('MPG', fn)



# with pipeline(('name', 'Chevrolet', 'Carlo', 'Landau')) as pipe:
#     data = data_parser()
#     for row in data:
#         pipe.send(row)

name_tuple = get_name_tuple('Chevrolet', 'Carlo')
rows = [['Chevrolet', 1, 'x'], ['Porche', 1, 'y']]
for row in rows:
    print(row)
    for fn in name_tuple[1]:
        print(fn)
        print(fn(row))
# print(name_tuple)


