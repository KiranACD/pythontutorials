from constants import paths, parsers, class_names, FileIterator, group_key
import datetime
# from parse_utils import csv_parser
from goal1_1 import TupleCreator
from goal2_1 import CombinedTupleCreator
from goal4_1 import MakeGroups
import itertools
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

# allinfo = CombinedTupleCreator(filter_key = lambda x:x.last_updated >= datetime.datetime(2017, 3, 1))
# for info in allinfo:
#     print(info)
#     print('------------------------------------')
# print(list(itertools.islice(allinfo, 5)))
# print(allinfo.headers)
# allinfo.create_zipped_tuple()
# print(next(allinfo.zipped_tuples))

make_group = MakeGroups(group_key=lambda x: x.vehicle_make, filter_key=lambda x: (x.last_updated >= datetime.datetime(2017, 3, 1)) and
                                                                                 (x.gender == 'Male'))

for row in make_group:
    print(row)