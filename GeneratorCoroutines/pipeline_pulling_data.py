import csv
import itertools

def parse_file(fname):
    with open(fname) as f:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        next(f) # skip the header row
        next(f) # skip the data type decription row
        yield from csv.reader(f, dialect=dialect)

def filter_data(rows, contains):
    for row in rows:
        if contains in row[0]:
            yield row

# Make a generic pipeline of filters
def output(fname, *filter_words):
    data = parse_file(fname)
    for filter_word in filter_words:
        data = filter_data(data, filter_word)
    yield from data

fname = 'GeneratorCoroutines/Data/cars.csv'
# data = parse_file(fname)
# filtered_data = filter_data(data, 'Chevrolet')
# for row in itertools.islice(filtered_data, 5):
#     print(row)

results = output(fname, 'Chevrolet', 'Carlo')
for row in results:
    print(row)