def gen_not_catch():
    try:
        while True:
            received = yield
            print(received)
    finally:
        print('exception must have happened')

def gen_catch_yield():
    
    while True:
        try:
            received = yield
            print(received)
        except ValueError:
            print('receivd a value error')

def gen_catch_silence():
    try:
        while True:
            received = yield
            print(received)
    except ValueError:
        print('receivd a value error') # silencing the ValueError, which is why StopIteration
    finally:
        print('exception must have happened')

def gen():
    while True:
        received = yield
        print(received)

def gen_catch_return():
    try:
        while True:
            received = yield
            print(received)
    except ValueError as e:
        print('ValueError received')
        return None

def gen_catch_raise_diff():
    try:
        while True:
            received = yield
            print(received)
    except ValueError as e:
        print('ValueError received')
        raise ZeroDivisionError('not really')

class CommitException(Exception):
    pass

class RollBackException(Exception):
    pass

def write_to_db():
    print('Opening db connection')
    print('start transaction')
    try:
        while True:
            try:
                data = yield
                print('writing data to database...', data)
            except CommitException:
                print('Commiting transaction...')
                print('opening next transaction')
            except RollBackException:
                print('aborting transaction')
                print('opening new transaction')
    finally:
        print('generator closing...')
        print('abort transaction...')
        print('closing db connction')


g_not_catch = gen_not_catch()
next(g_not_catch)
g_not_catch.send('hello')
try:
    g_not_catch.throw(ValueError, 'custom message')
except Exception as e:
    print('Error bubbled up!')
    print(e)

print('----------------------------------------')
g_catch_silence = gen_catch_silence()
next(g_catch_silence)
g_catch_silence.send('hello')
try:
    g_catch_silence.throw(ValueError, 'custom message')
except Exception as e:
    print('Error bubbled up!')
    print(e)

print('-----------------------------------------')
g_catch_yield = gen_catch_yield()
next(g_catch_yield)
g_catch_yield.send('hello')
try:
    g_catch_yield.throw(ValueError, 'custom message')
except Exception as e:
    print('Error bubbled up!')
    print(e)

print('-----------------------------------------')
g = gen()
next(g)
g.send('hello')
try:
    g.throw(ValueError, 'custom message')
except Exception as e:
    print('Error bubbled up!')
    print(e)

print('-----------------------------------------')

gen_catch_raise_diff = gen_catch_raise_diff()
next(gen_catch_raise_diff)
gen_catch_raise_diff.send('hello')
try:
    gen_catch_raise_diff.throw(ValueError, 'custom message')
except Exception as e:
    print('Error bubbled up!')
    print(e)

print('------------------------------------------')

sql = write_to_db()
next(sql)
sql.send(100)
sql.throw(CommitException)
sql.send(300)
sql.throw(RollBackException)
sql.close()