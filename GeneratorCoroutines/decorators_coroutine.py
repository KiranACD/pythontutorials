def coroutine(gen_fn):
    def inner(*args, **kwargs):
        g = gen_fn(*args, **kwargs)
        next(g)
        return g
    return inner

@coroutine
def echo():
    while True:
        received = yield
        print(received)

@coroutine
def power_up(p):
    result = None
    while True:
        value = yield result
        try: # Including the try block to catch errors that we can silence.
            result = value**p
        except TypeError:
            result = None

echo = coroutine(echo)
e = echo()
e.send('hello')

squares = power_up(2)
cubes = power_up(3)

print(squares.send(2))
print(cubes.send(2))

squares.close()
cubes.close()