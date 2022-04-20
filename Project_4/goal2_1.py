from constants import paths, parsers, class_names, compress_fields, FileIterator
# from parse_utils import csv_parser
from goal1_1 import TupleCreator
import itertools
from collections import namedtuple
# for path in paths:
#     reader = csv_parser(path)
#     print(list(itertools.islice(reader, 5)))

# tuples = []
# for path, parser, class_name in zip(paths, parsers, class_names):
#     tuples.append(TupleCreator(path, parser, class_name))
#     for row in tuples[-1]:
#         print(row)
#         break
#     print('----------------------')
#     for row in tuples[-1]:
#         print(row)
#         break

class CombinedTupleCreator:

    def __init__(self, *, filter_key=None):
        self.tuples = []
        self.filter_key = filter_key
        self.compressed_fields = tuple(itertools.chain.from_iterable(compress_fields))
        self.populate_tuples()

    def yield_tuple_iterator(self):
        for path, parser, class_name in zip(paths, parsers, class_names):
            yield TupleCreator(path, parser, class_name)

    def populate_tuples(self):
        for t in self.yield_tuple_iterator():
            self.tuples.append(t)
        self.create_named_tuple()
    
    def create_named_tuple(self):

        self.headers = tuple(itertools.compress(tuple(itertools.chain.from_iterable((map(lambda x: x.headers, self.tuples)))),
                                          self.compressed_fields))
        
        self.Allinfo = namedtuple('Allinfo', self.headers)

    def __iter__(self):
        if self.filter_key:
            return self.yield_filtered_tuple()
        else:
            return self.compress_and_yield_tuple()

    def create_zipped_tuple(self):
        self.zipped_tuples = zip(*self.tuples)
    
    def chain_tuples(self):
        self.create_zipped_tuple()
        self.merged_iter = (itertools.chain.from_iterable(zipped_tuple) for zipped_tuple in self.zipped_tuples)

    def compress_and_yield_tuple(self):
        self.chain_tuples()
        for row in self.merged_iter:
            compressed_row = itertools.compress(row, self.compressed_fields)
            yield self.Allinfo(*compressed_row)    
    
    def yield_filtered_tuple(self):
        info_gen = self.compress_and_yield_tuple()
        yield from filter(self.filter_key, info_gen)

    