import os.path
import csv
from parse_utils import csv_parser, string_parser, int_parser, date_parser

# csv reader config
delimiter = ','
quotechar = '"'

class FileIterator:

    def __init__(self, file_path, *, include_header=False, use_csv_reader=False, delimiter = delimiter, quotechar=quotechar):
        self.file_path = file_path
        self.use_csv_reader = use_csv_reader
        self.delimiter = delimiter
        self.quotechar = quotechar
        self.include_header = include_header

    def __iter__(self):
        if self.use_csv_reader:
            return self.open_csv_file()
        else:
            return self.open_file()
    
    def open_file(self):
        with open(self.file_path) as f:
            if not self.include_header:
                next(f)
            yield from f
    
    def open_csv_file(self):
        with open(self.file_path) as f:
            reader = csv.reader(f, delimiter = self.delimiter, quotechar=self.quotechar)
            if not self.include_header:
                next(f)
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

    def get_headers_csv(self):

        with open(self.file_path) as f:
            reader = csv.reader(f, delimiter = self.delimiter, quotechar=self.quotechar)
            f = next(reader)
            return f

# File names
file_path = 'Project_4/data'
file_names = ['personal_info.csv','employment.csv', 'vehicles.csv', 'update_status.csv']
paths = [os.path.join(file_path, item) for item in file_names]

# Parsers
personal_parser = (string_parser, string_parser, string_parser, string_parser, string_parser)
employment_parser = (string_parser, string_parser, string_parser, string_parser)
vehicle_parser = (string_parser, string_parser, string_parser, int_parser)
update_status_parser = (string_parser, date_parser, date_parser)
parsers = personal_parser, employment_parser, vehicle_parser, update_status_parser

# Tuple Names
personal_class_name = 'Personal'
employment_class_name = 'Employment'
vehicle_class_name = 'Vehicle'
update_status_class_name = 'UpdateStatus'
class_names = personal_class_name, employment_class_name, vehicle_class_name, update_status_class_name

# Field Inclusion/Exclusion
personal_fields_compress = [True, True, True, True, True]
employment_fields_compress = [True, True, True, False]
vehicle_fields_compress = [False, True, True, True]
update_status_fields_compress = [False, True, True]
compress_fields = (personal_fields_compress, employment_fields_compress, 
                   vehicle_fields_compress, update_status_fields_compress)

def group_key(item):
    return item.gender, item.vehicle_make 



