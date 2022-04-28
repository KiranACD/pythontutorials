import csv
from contextlib import contextmanager
# Config
input_file = 'GeneratorCoroutines/Data/car_data.csv'
output_file_path = 'GeneratorCoroutines/Data/'

idx_make = 0
idx_model = 1
idx_year = 2
idx_vin = 3
idx_colour = 4

headers = ('make', 'model', 'year', 'vin', 'colour')

converters = (str, str, int, str, str)

def file_reader(fname):
    with open(fname) as f:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        reader = csv.reader(f, dialect=dialect)
        yield from reader

def data_parser():
    data = file_reader(input_file)
    next(data)
    for row in data:
        parsed_row = [converter(item) for converter, item in zip(converters, row)]
        yield parsed_row

def coroutine(fn):
    def inner(*args, **kwargs):
        gen = fn(*args, **kwargs)
        next(gen)
        return gen
    return inner

@coroutine
def save_data(fname, headers):
    fname = output_file_path + fname
    with open(fname, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        while True:
            data_row = yield
            writer.writerow(data_row)

@coroutine
def filter_data(filter_predicate, target):
    while True:
        data_row = yield
        if filter_predicate(data_row):
            target.send(data_row)

@coroutine
def broadcast(targets):
    while True:
        data_row = yield
        for target in targets:
            target.send(data_row)

@coroutine
def process_data():
    out_pink_cars = save_data('pink_cars.csv', headers)
    out_ford_green = save_data('ford_green.csv', headers)
    out_older = save_data('older.csv', headers)

    filter_pink_cars = filter_data(lambda d: d[idx_colour].lower() == 'pink', out_pink_cars)

    def pred_ford_green(d):
        return d[idx_make].lower() == 'ford' and d[idx_colour].lower() == 'green'
    
    filter_ford_green = filter_data(pred_ford_green, out_ford_green)

    filter_older = filter_data(lambda d: d[idx_year] <= 2010, out_older)

    filters = (filter_pink_cars, filter_ford_green, filter_older)

    broadcaster = broadcast(filters)

    while True:
        row = yield
        broadcaster.send(row)

# Putting it into a function automatically closes the pipe.
def run():
    pipe = process_data()
    for row in data_parser():
        pipe.send(row)
    
# Lets use a context manager
@contextmanager
def pipeline():
    p = process_data()
    try:
        yield p
    finally:
        p.close()

with pipeline() as pipe:
    data = data_parser()
    for row in data:
        pipe.send(row)

    







