from inspect import getgeneratorstate
import csv
import itertools

# Custom Exception
class TransactionAborted(Exception):
    pass

def parse_file(fname):
    print('opening file...')
    f = open(fname, 'r')
    try:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        reader = csv.reader(f, dialect=dialect)
        for row in reader:
            yield row
    except GeneratorExit:
        print('Generator is closed for business!')
    finally:
        print('closing the file')
        f.close()

def save_to_db():
    print('starting new transaction')
    is_abort = False
    try:
        while True:        
            data = yield
            print('sending data to database: ', str(data))
    except Exception as ex:
        is_abort = True
        raise TransactionAborted(str(ex))
    finally:
        if is_abort:
            print('rollback transaction')
        else:
            print('commit transaction')
    

# at the end of the loop the generator is closed automatically
parser = parse_file('GeneratorCoroutines/Data/cars.csv')
for row in itertools.islice(parser, 10):
    print(row)