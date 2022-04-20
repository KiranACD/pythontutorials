from goal2_1 import CombinedTupleCreator
import itertools

class MakeGroups:

    def __init__(self, group_key, *, filter_key=None):
        self.allinfo = CombinedTupleCreator()
        self.group_key = group_key
        self.filter_key = filter_key

    def __iter__(self):
        return self.show_group()
        
    def filter_data(self):
        data = filter(self.filter_key, self.allinfo)
        yield from data

    def sort_data(self):
        if self.filter_key:
            data = self.filter_data()
        else:
            data = self.allinfo
        self.sorted_data = sorted(data, key=self.group_key)
    
    def get_group(self):
        self.sort_data()
        self.groups = itertools.groupby(self.sorted_data, key=self.group_key)

    def show_group(self):
        self.get_group()
        for row in self.groups:
            yield (row[0], len(list(row[1])))
            print('-----------------------------------') 
