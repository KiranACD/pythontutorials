from collections import namedtuple
from constants import FileIterator, paths, delimiter, quotechar


class TupleCreator:
    def __init__(self, path, parser, name, *, use_csv_reader=True):
        self.path = path
        self.name = name
        self.parser = parser
        self.file_iter = FileIterator(self.path, use_csv_reader=use_csv_reader, delimiter=delimiter, quotechar=quotechar)
        self.create_tuple()

    def get_headers(self):
        self.headers = self.file_iter.get_headers_csv()

    def create_tuple(self):
        self.get_headers()
        self.Tuple = namedtuple(self.name, self.headers)

    def __iter__(self):
        return self.data_gen()

    def data_gen(self):
        for row in self.file_iter:
           data = (parse_fn(value) for value, parse_fn in zip(row, self.parser))
           yield self.Tuple(*data)

# for path in paths:
#     file = FileIterator(path, include_header=True)
#     file = iter(file)
#     print(next(file))
#     print(next(file))
#     print('---------------------------')