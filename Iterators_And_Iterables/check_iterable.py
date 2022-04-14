
def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

class SimpleIterator:
    def __init__(self):
        pass
    def __iter__(self):
        return None

if __name__ == '__main__':

    s = SimpleIterator()
    
    # Try and ask for forgiveness later
    try:
        for i in s:
            print(i)
    except TypeError:
        print('Error: Object is not iterable.')

    # Get mission first, then do it
    if is_iterable(s):
        for i in s:
            print(i)
    else:
        print('Error: Object is not iterable.')
