from collections import namedtuple
import csv

# Goal1: Yield named tuples with field names based on the header row
class DataIterator:
    def __init__(self, fname, name):
        self.fname = fname
        self.name = name
        self._f = open(self.fname)
        self.get_headers()
        self.create_named_tuple()
    
    def get_headers(self):
        self.sniff_dialect()
        self.reader = csv.reader(self._f, dialect=self.dialect)
        self.headers = next(self.reader)
        print(self.headers)

    def sniff_dialect(self):
        sample = self._f.read(2000)
        self.dialect = csv.Sniffer().sniff(sample)
        self._f.seek(0)

    def __iter__(self):
        return self.send_named_tuple()

    def create_named_tuple(self):
        self.Tuple = namedtuple(self.name, self.headers)

    def send_named_tuple(self):
        for row in self.reader:
            yield self.Tuple(*row)

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        self._f.close()
        return False

fname = 'Project_5/Data/personal_info.csv' 
name = 'Personal'
with DataIterator(fname, name) as data:
    for row in data:
        print(row)


