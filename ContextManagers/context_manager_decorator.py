from multiprocessing import context


class GenContextManager:
    def __init__(self, gen):
        self.gen = gen
    
    def __enter__(self):
        print('calling next to get the yielded value from generator')
        return next(self.gen)

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('calling next to perform clean up in generator')
    
        try:
            next(self.gen)
        except StopIteration:
            pass
        return False

def context_manager_dec(gen_fn):
    def helper(*args, **kwargs):
        gen = gen_fn(*args, **kwargs)
        return GenContextManager(gen)
    return helper

@context_manager_dec
def open_file(fname, mode='r'):
    print('opening file...')
    f = open(fname, mode)
    try:
        yield f
    finally:
        print('closing file...')
        f.close()

with open_file('ContextManagers/Data/test3.txt', 'r') as f:
    print(f.readlines())
