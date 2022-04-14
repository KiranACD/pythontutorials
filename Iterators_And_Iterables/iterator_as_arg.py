import os.path

def get_mpg(row):
    row = row.strip('\n').split(';')

    return row[0], float(row[1])

def get_perc_from_max(data):

    if iter(data) is data:
        data = list(data)
    
    max_val = 0
    for row in data:
        _, val = get_mpg(row)
        max_val = max(max_val, val)

    for row in data:
        car, mpg = get_mpg(row)
        print(f'Car: {car}, mpg: {mpg}, mpg % of max: {((mpg/max_val) * 100):.2f}')
    
file_name = 'cars.csv'
file_path = 'Iterators_And_Iterables/'
path = os.path.join(file_path, file_name)

f = open(path)
next(f)
next(f)
get_perc_from_max(f)
# for data in f:
#     print(data.strip('\n').split(';'))
f.close()