def my_gen():
    try:
        print('Creating context and yielding object')
        yield [1, 2, 3, 4]
    finally:
        print('exiting context and cleaning up')

gen = my_gen()

lst = next(gen)
print(lst)

# catching the StopIteration exception
try:
    next(gen)
except StopIteration:
    pass
# Encapsulate this functionality in a context manager class



def open_file(fname, mode):
    f = open(fname, mode)
    try:
        print('opening file...')
        yield f
    finally:
        print('closing file...')
        f.close()

class GeneratorContextManager:
    def __init__(self, gen, *args, **kwargs):
        self._gen = gen(*args, **kwargs)
    
    def __enter__(self):
        return next(self._gen)
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False

with GeneratorContextManager(my_gen) as obj:
    print(obj)

with GeneratorContextManager(open_file, 'ContextManagers/Data/test.txt', 'w') as obj:
    obj.writelines('testing...')