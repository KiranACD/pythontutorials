def my_func():
    a = 24*60
    b = (1,2)*5
    c = 'abc'*5
    d = 'ab'*11
    e = ['a', 'b']*3
    f = [1, 2]*5
    g = 'hello the quick brown fox' * 5

def my_func2(e):

    if e in [1, 2, 3]:
        pass
    
    if e in {1, 2, 3}:
        pass

if __name__ == '__main__':
    print('constants for my_func: ', my_func.__code__.co_consts)
    print('constants for my_func2: ', my_func2.__code__.co_consts)
