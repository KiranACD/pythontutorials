from contextlib import contextmanager
from collections import namedtuple
import csv

def sniff_dialect(f):
    sample = f.read(2000)
    dialect = csv.Sniffer().sniff(sample)
    f.seek(0)
    return dialect

def get_header(f):
    dialect = sniff_dialect(f)
    reader = csv.reader(f, dialect)
    header = next(reader)
    return header, reader

def create_tuple(name, header):
    return namedtuple(name, header)

@contextmanager
def read_data(fname, name):
    f = open(fname)
    header, reader = get_header(f)
    ntuple = create_tuple(name, header)
    yield (ntuple(*row) for row in reader)

fname = 'Project_5/Data/cars.csv' 
name = 'Car'
with read_data(fname, name) as data:
    for row in data:
        print(row)