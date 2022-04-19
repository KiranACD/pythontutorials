import os.path
import datetime
from collections import defaultdict
from goal1 import PersonalDetails, Employment, Vehicles, UpdateStatus
from goal3 import AllInfo

file_path = 'Project_4/'
file_names = ['personal_info.csv','employment.csv', 'vehicles.csv', 'update_status.csv']

paths = [os.path.join(file_path, item) for item in file_names]

d = {paths[0]:PersonalDetails, paths[1]:Employment, paths[2]:Vehicles, paths[3]:UpdateStatus}

files = tuple([d[key](key) for key in d])

info = AllInfo(files, stale_date=datetime.date(2017, 3, 1))

car_makes_male = defaultdict(int)
car_makes_female = defaultdict(int)

d = {'Male':car_makes_male, 'Female':car_makes_female}

for i in info:
    d[i.gender][i.vehicle_make] += 1

print(d)
    

