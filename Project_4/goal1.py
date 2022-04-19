import csv
import os.path
import itertools
from collections import namedtuple
import datetime

class FileIterator:

    def __init__(self, file_path, *, use_csv_reader=False, delimiter = ',', has_quotes=False):
        self.file_path = file_path
        self.use_csv_reader = use_csv_reader
        self.delimiter = delimiter
        self.has_quotes = has_quotes

    def __iter__(self):
        if self.use_csv_reader:
            return self.open_file()
        else:
            return self.open_csv_file()
    
    def open_file(self):
        with open(self.file_path) as f:
            for row in f:
                yield row.strip('\n')
    
    def open_csv_file(self):
        with open(self.file_path) as f:
            reader = csv.reader(f, delimiter = ',', quotechar='"')
            yield from reader
    
    def remove_quotes(self, row):
        st = []
        n = len(row)
        row = list(row)
        for _ in range(n):
            if row[_] == '"':
                if len(st) == 0:
                    st.append(row[_])
                    row[_] = ''
                else:
                    st.pop(-1)
                    row[_] = ''
            elif row[_] == ',':
                if st:
                    row[_] = ''
        return ''.join(row)

class PersonalDetails:
    def __init__(self, path):
        self.file_iter = FileIterator(path, use_csv_reader=True, delimiter=',', has_quotes=True)
        self.headers = list(itertools.islice(self.file_iter, 0, 1))[0].split(',')
        self.create_tuple()

    def create_tuple(self):
        self.Identity = namedtuple('Identity', self.headers) #'ssn first_name last_name gender language')

    def parse_row(self, row):
        row = row.split(',')
        return row

    def get_tuple(self, row):
        row = self.parse_row(row)
        return self.Identity(*row)
    
    def __iter__(self):
        it = iter(self.file_iter)
        next(it)
        return (self.get_tuple(row) for row in it)

class Employment:
    def __init__(self, path):
        self.file_iter = FileIterator(path, use_csv_reader=True, delimiter=',', has_quotes=True)
        self.headers = list(itertools.islice(self.file_iter, 0, 1))[0].split(',')
        self.create_tuple()
    
    def create_tuple(self):
        self.Job = namedtuple('Job', self.headers)
    
    def cast_item(self, item, *, default = None):
        item.strip()
        try:
            return int(item)
        except ValueError:
            try:
                return datetime.datetime.strptime(item, '%M/%d/%Y').date()
            except ValueError:
                if item:
                    return str(item)
                else:
                    return default

    def parse_row(self, row):
        row = self.file_iter.remove_quotes(row)
        row = row.split(',')
        row = [self.cast_item(item) for item in row]
        if not all(row):
            print(row)
        return row if all(row) else None

    def __iter__(self):
        return self.get_employment_tuple()
    
    def get_employment_tuple(self):
        it = iter(self.file_iter)
        next(it)
        for row in it:
            row = self.parse_row(row)
            if row:
                yield self.Job(*row)

class Vehicles:
    def __init__(self, path):
        self.file_iter = FileIterator(path, use_csv_reader=True, delimiter=',', has_quotes=True)
        self.headers = list(itertools.islice(self.file_iter, 1))[0].split(',')
        self.create_tuple()
    
    def create_tuple(self):
        self.Vehicle = namedtuple('Vehicle', self.headers)
    
    def cast_row(self, item, *, default=None):
        item = item.strip()
        try:
            return int(item)
        except ValueError:
            try:
                return datetime.datetime.strptime(item, '%M/%d/%Y').date()
            except ValueError:
                if item:
                    return str(item)
                else:
                    return default
    
    def parse_row(self, row):
        row = self.file_iter.remove_quotes(row)
        row = row.split(',')
        row = [self.cast_row(item) for item in row]
        if not all(row):
            print(row)
        return row if all(row) else None

    def __iter__(self):
        return self.get_vehicle_tuple()
    
    def get_vehicle_tuple(self):
        it = iter(self.file_iter)
        next(it)
        for row in it:
            row = self.parse_row(row)
            if row:
                yield self.Vehicle(*row)

class UpdateStatus:
    def __init__(self, path):
        self.file_iter = FileIterator(path, use_csv_reader=True, delimiter=',', has_quotes=True)
        self.headers = list(itertools.islice(self.file_iter, 1))[0].split(',')
        self.create_tuple()
    
    def create_tuple(self):
        self.Status = namedtuple('Status', self.headers)
    
    def get_datetime(self, item):
        date = list(item)
        for _ in range(len(date)):
            if date[_] == 'T' or date[_] == 'Z':
                date[_] = ' '
        
        date = ''.join(date)
        date = date.strip()
        return datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

    def cast_row(self, item, *, default=None):
        item = item.strip()
        try:
            return int(item)
        except ValueError:
            try:
                return self.get_datetime(item)
            except ValueError:
                if item:
                    return str(item)
                else:
                    return default
    
    def parse_row(self, row):
        row = self.file_iter.remove_quotes(row)
        row = row.split(',')
        row = [self.cast_row(item) for item in row]
        if not all(row):
            print(row)
        return row if all(row) else None

    def __iter__(self):
        return self.get_tuple()

    def get_tuple(self):
        it = iter(self.file_iter)
        next(it)
        for row in it:
            row = self.parse_row(row)
            if row:
                yield self.Status(*row)

if __name__ == '__main__':

    file_name1 = 'personal_info.csv'
    file_path1 = 'Project_4/'
    path1 = os.path.join(file_path1, file_name1)

    person = PersonalDetails(path1)

    # print(list(itertools.islice(person, 5)))

    file_name2 = 'employment.csv'
    file_path2 = 'Project_4/'
    path2 = os.path.join(file_path2, file_name2)

    employment = Employment(path2)

    list(employment)

    file_name3 = 'vehicles.csv'
    file_path3 = 'Project_4/'
    path3 = os.path.join(file_path3, file_name3)

    vehicle = Vehicles(path3)

    # for v in vehicle:
    #     print(v)

    file_name4 = 'update_status.csv'
    file_path4 = 'Project_4/'
    path4 = os.path.join(file_path4, file_name4)

    status = UpdateStatus(path4)

    # list(status)

    for s in status:
        print(s)