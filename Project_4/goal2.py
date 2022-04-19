from collections import namedtuple
import itertools
import sys
import os.path
from goal1 import PersonalDetails, Employment, Vehicles, UpdateStatus

class AllInfo:
    def __init__(self, files):
        
        self.files = files
        self.create_tuple()
    
    def create_tuple(self):
        self.headers = [item 
                        for item in itertools.chain(*list(map(lambda x: x.headers, self.files)))
                        if item != 'ssn']
        self.headers.insert(0, 'ssn')
        self.Info = namedtuple('Info', self.headers)
    
    def __iter__(self):
        return self.get_info()
    
    def get_all_vals(self, group):
        values = []
        ssn = group[0][0]
        values.append(ssn)
        for items in group:
            n_tuple = list(items[1])[0]
            fields = n_tuple._fields
            n_tuple = zip(fields, n_tuple)
            for t in n_tuple:
                if t[0] != 'ssn':
                    values.append(t[1])
        print(values)
        return values

    def get_info(self):        
        groups = (itertools.groupby(file, key=lambda x: x.ssn) for file in self.files)
        zip_groups = zip(*groups)
        vals = (self.get_all_vals(g) for g in zip_groups)
        for val in vals:
            yield self.get_tuple(val)

    def get_tuple(self, val):
        return self.Info(*val)
    

if __name__ == '__main__':

    x = namedtuple('x', 'y z')
    x1 = x(1, 2)
    print(x1._fields)
    print([item for item in zip(x1._fields, x1) if item[0] != 'y'])   
    file_path = 'Project_4/'
    file_names = ['personal_info.csv','employment.csv', 'vehicles.csv', 'update_status.csv']

    paths = [os.path.join(file_path, item) for item in file_names]

    d = {paths[0]:PersonalDetails, paths[1]:Employment, paths[2]:Vehicles, paths[3]:UpdateStatus}

    files = tuple([d[key](key) for key in d])
    
    info = AllInfo(files)
    print(info.headers)
    print(list(itertools.islice(info, 5)))
    # print(info.groups)


