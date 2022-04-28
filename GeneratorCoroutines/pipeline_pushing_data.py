
def coroutine(coro):
    def inner(*args, **kwargs):
        gen = coro(*args, **kwargs)
        next(gen) # prime the gen
        return gen
    return inner

# Create data consumer generator that will print what it receives. It can be later changed...
# ...to print to file

@coroutine
def handle_data():
    while True:
        received = yield
        print(received)


@coroutine
def power_up(n, next_gen):
    while True:
        received = yield
        output = received**n
        next_gen.send(output)

@coroutine
def filter_data(next_gen):
    while True:
        received = yield
        if received%2 == 0:
            next_gen.send(received)

print_data = handle_data()
filtered_data = filter_data(print_data)
gen2 = power_up(3, filtered_data)
gen1 = power_up(2, gen2)
for i in range(1, 15):
    gen1.send(i)