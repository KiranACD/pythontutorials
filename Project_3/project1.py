
from collections import namedtuple, defaultdict
import os.path
import datetime

def open_file(file_path):
    with open(file_path) as f:
        for row in f:
            yield row

def violation_tuple(row_list):

    Violations = namedtuple('Violations', row_list)
    return Violations

class FileIterator:

    def __init__(self, file_path):
        self.file_path = file_path
    
    def __iter__(self):
        return self.open_file()
    
    def open_file(self):
        with open(self.file_path) as f:
            for row in f:
                yield row.strip('\n')

class TrafficViolations:

    def __init__(self, file_path):
        self.file = FileIterator(file_path)
        self.header_default = [None, None, '', '', None, None, '', None, '']
    
    def __iter__(self):
        return self.violations_gen()
    
    def get_headers(self, row):
        self.headers = row.split(',')
        for _ in range(len(self.headers)):
            self.headers[_] = self.headers[_].strip().replace(' ', '_').lower()

    def create_tuple(self):
        self.Violations = namedtuple('Violations', self.headers)

    @staticmethod
    def cast(item, *, default=None):
        item = item.strip()
        try:
            return int(item)
        except ValueError:
            try:
                return datetime.datetime.strptime(item, '%m/%d/%Y').date()
            except ValueError:
                if item:
                    return str(item)
                else:
                    return default

    def parse_row(self, row):
        row = row.split(',')
        n = len(row)
        if n > 9:
            print(n)
        
        row = [TrafficViolations.cast(item, default=default) for item, default in zip(row, self.header_default)]

        if all(item is not None for item in row):
            return row
        else:
            # print(list(zip(self.headers, row)))
            return None

    def get_tuple(self, row):
        return self.Violations(*row)

    def violations_gen(self):

        count = 0
        for row in self.file:
            if count == 0:
                self.get_headers(row)
                self.create_tuple()
                count += 1
                continue
            row = self.parse_row(row)
            if row:
                yield self.get_tuple(row)

if __name__ == '__main__':
    
    file_name = 'nyc_parking_tickets_extract.csv'

    file_path = 'Project_3/'

    path = os.path.join(file_path, file_name)

    violations = TrafficViolations(path)

    count = 0
    ticket_type = defaultdict(int)
    d = defaultdict(str)
    for v in violations:
        ticket_type[v.vehicle_make] += 1

    print(ticket_type)        

    # Summons number - INT
    # Plate Id - STR
    # Registration State - STR
    # Plate Type - STR
    # Issue Date - DATE
    # Violation Code - INT
    # Vehicle Body Type - STR
    # Vehicle Make - STR
    # Violation Description - STR

