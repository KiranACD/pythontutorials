import os.path

def get_clean_data(file):
    with open(file, 'r', encoding='latin-1') as f:
        for row in f:
            yield row.strip('\n')

def brands(*files):
    for f_name in files:
        yield from get_clean_data(f_name)

def table(n):

    gen = ((i*j for j in range(1, n+1)) for i in range(1, n+1))

    return gen

def table_iterator(n):

    for row in table(n):
        yield from row

if __name__ == '__main__':

    file1 = 'car-brands-1.txt'
    file2 = 'car-brands-2.txt'
    file3 = 'car-brands-3.txt'

    file_path = 'Generators/'

    files = (os.path.join(file_path,file1), os.path.join(file_path,file2), os.path.join(file_path,file3))

    print(list(table_iterator(3)))

    print(list(brands(*files)))