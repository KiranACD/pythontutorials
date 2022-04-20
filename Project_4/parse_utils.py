import csv
import datetime


def csv_parser(path, *, delimiter = ',', quotechar = '"'):
    with open(path) as f:
        reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
        yield from reader

def string_parser(item, *, default=None):
    try:
        item = str(item).strip()
    except ValueError:
        return None
    if item:
        return str(item)
    else:
        return default

def int_parser(item):
    try:
        return int(item)
    except ValueError:
        return None

def date_parser(item, *, format = '%Y-%m-%dT%H:%M:%SZ'):
    try:
        return datetime.datetime.strptime(item, format)
    except ValueError as e:
        return None

    


