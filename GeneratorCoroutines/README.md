## Concurrency vs Parallelism

These are different ways to achieve multitasking. Consider you have two tasks. 

Concurrency is when you excecute task1, then pause, execute task2, then pause and repeat the whole process till both tasks finish.

Parallelism is when you execute both task1 and task2 together, where task1 is being executed in one CPU core and task2 is being excuted in another CPU core.

## Cooperative vs Preemptive Multitasking

There is no coperation or premptiveness when you talk about parallellsim. However, it exists in concurrency. 

Let's say you have a corporative set of tasks, task1 and task2. Task1 runs and it does a voluntary yield. At this point, task2 starts running ans it yields voluntarily as well. The whole process repeats over and over. We can say task1 and task2 are coperating with each other. As the developer, you have complete control over when the tasks yield. You have to say when something will be yielded.  

On the other hand, we have preemptive multitasking. Again assume we have task1 and task2. At some point, when task1 is running, it gets suspended, but it is not voluntary. It is usually done by something that is controlling the tasks, like a scheduler. This is unlike the copoerative approach where you have to control the flow and there is nothing else controlling the tasks. Once task1 is suspended, task2 starts to run and it gets suspending after some arbitrary time and the whole process repeats.

This is the difference between cooperative and premptive multitasking. 

Coroutines fit under the cooperative multitasking type. Threading is in between. There some ways you can control certain things, but in some of them, you just can't

## Coroutines

Coroutines are cooperative routines. They run concurrently and not in parallel. You can think of routines as functions. Coroutines are functions that cooperate with each other, as opposed to a regular subroutine, which executes one/many tasks and exits, at which point control is given back to from where it was called. 

For e.g., consider this averager function and a running averages function.
```
def averager():
    total = 0
    count = 0
    # closure
    def inner(value):
        nonlocal total
        nonlocal count
        total += value
        count += 1
        return total/count
    return inner # returns the closure

def running_averages(iterable):
    # assigns the closure
    avg = averager()
    for value in iterable:
        running_avg = avg(value)
        print(running_avg)
```
- The running_averages receives an iterable 
- Assigns the inner closure from the averager
- Iterates over the iterable
- For each iteration, the inner subroutine is called. Inner is in control.
- A stack frame is created for inner. It does its work and in this case, a value is returned. The subroutine terminates at that point. Stack frame is destroyed.
- Now running_averages is back in control and receives the value and does some work with it. In this case, the running average is printed out.
- The whole process repeats over the whole iteration cycle.

Let us look at how this is different from a coroutine.

Consider the two functions again in pseudo-code 
```
def running_averager():
    total = 0
    count = 0
    running_average = None
    while True:
        wait for value
        receive new value
        calculate new average
        yield new average

def running_averages(iterable):
    create instance of running_averager
    start coroutine
    for value in iterable:
        send value to running_averager
        received value back
        print(received value)
```
- In the running_averages function, we receive an iterable.
- Create an instance of the running_averager, which is a coroutine and specifically a generator object.
- Start the coroutine. A stack frame for the running averager is created.
- Then it creates variables to store the total and count. Then it starts an infinite while loop and waits to receive a value. It suspends itself and give control back to the running averages method
- Back in the running averages function, we start the iteration over the iterable and sends a value to running_averager and waits to receive the result.
- Back at the running_averager, it receives the value, calculates the running average and yields it back to the running_averages and gives control back to it.
- We do something (in this case print) with the received value at the running_averages. 
- The coroutine is still active.

There are 2 ways to create coroutines in Python. 

- Generators that use an extended form of yield statement. A recent addition is asyncio.
- Native coroutines that use async and await.


### Abstract Data Structures

These data structures are going to be used in certain examples here.

#### Queue

A queue is a data structure that supports the first-in first-out (FIFO) addition/removal of item. Add items to the back of the queue and remove from front of the queue.

#### Stack

A stack is a data structure that supports the last-in first-out (LIFO) addition/removal of item. Add items to the top of the stack and remove them from the top of the stack.

They are called abstract because they can be implemented in many different ways.

#### Using lists

Stack
- lst.append(item) - appends item to the end of the list
- lst.pop() - removes and returns the last item of the list

Queue
- lst.insert(0, item) - insert item at the front of the list
- lst.pop() - removes and returns the last item of the list

Inserting an item to the front of a list is inefficient. So we will use the deque data structure from the collections module. As it is a double ended queue, we can add/remove items to/from both front and back of a collection efficiently.

```
from collections import deque

dq = deque()
dq = deque(iterable)
dq = deque(maxlen=n)

dq.append(item)
dq.appendleft(item)
dq.pop()
dq.popleft()
dq.clear()
len(dq)
```
An example of a coroutine where we are going to use the deque structure. Consider a producer and consumer kind of pattern. The producer adds data to the queue and the consumer grabs data from the queue and performs some work on the data.

We can implement them using subroutines by doing the following steps

- create and unlimited deque
- run producer to insert all elements into deque
- run consumer to remove and process all elements in deque

Here is a producer and a consumer
```
def produce_elements(dq):
    for i in range(1, 100000):
        dq.appendleft(i)

def consume_elements(dq):
    while dq:
        item = dq.pop()
        print('processing item', item)

def coordinator():
    dq = deque()
    producer = produce_elements(dq)
    consume_elements(dq)
```
We can implement them using generators by doing the following steps

- create a limited size deque
- coordinator creates an instance of producer generator
- coordinator creates an instance of consumer generator
- producer runs till maxlen reached. Yields control back to caller
- consumer runs till all elements consumed. Yields control back to caller

Repeat till the producer is done or controller decided to stop.

```
def produce_elements(dq, n):
    for i in range(1, n):
        dq.appendleft(i)
        if len(dq) == dq.maxlen:
            yield # suspends

def consume_elements(dq):
    while True:
        while q:
            item = dq.pop()
            # process item
        yield # suspends

def coordinator():
    dq = deque(maxlen=10)
    producer = produce_elements(dq, 100000)
    consumer = consume_elements(dq)
        while True:
            try:
                next(producer)
            except StopIteration: # yield does not stop iteration
                break
            finally:
                next(consumer)
```

### Generator States

Let's look at a generator implementation.
```
def my_gen(fname):
    f = open(fname)
    try:
        for row in f:
            yield row.split(',')
    finally:
        f.close()

# Create Generator
rows = my_gen(fname) # Generator is created. Nothing starts running yet.

# Run Generator
next(rows) # This runs until it sees the yield statement and then suspends.
           # Or, the generator exists, either from the try block due to error or
           # the iteration finishes. Then the generator is closed.
```

#### Inspecting a generator's state

The four states are:

- GEN_CREATED
- GEN_RUNNING
- GEN_SUSPENDED
- GEN_CLOSED

```
from inspect import getgeneratorstate
g = my_gen(fname)
getgeneratorstate(g) # This returns GEN_CREATED
row = next(g) # This returns GEN_SUSPENDED
lst(g) # This iterates through the generator until it is done. 
getgenerator(g) # This return GEN_CLOSED

# If you call getgenerator(g) from inside the generator when it is running, you get GEN_RUNNING
```
It is difficult to get the GEN_RUNNING state because the generator code does not know what the generator object is. However, when we create the generator state, g becomes a global variable. So when we call `getgeneratorstate(g)` from inside the genrator code, then it returns GEN_RUNNING.

### Sending Data to Generators

So far, we saw:

- how yield can produce values. Use next() to get the produced values.
- After a value is yielded, the generator is suspended.

Can we send data to the generator upon resumption?

Until now, we have been using yield as a statement. But yield is an expression which returns a value. So we can write `received = yield`. 

Where is the value going to come from? It is going to come from outside the generator.
So we can actually write `received = yield 'hello'`

For e.g.
```
def gen_echo():
    while True:
        received = yield
        print('You said: ', received)
        break

echo = gen_echo() # GEN_CREATED
next(echo) # GEN_SUSPENDED
echo.send('hello') # This works only when gen is suspended
```
As the send method works only when the generator is suspended, we have to prime the generator to get it into the GEN_SUSPENDED state.

Lets revist the averager generator function that we used earlier to describe cooperative coroutines.
```
def running_averager()
    total = 0
    count = 0
    running_average = None
    while True:
        value = yield running_average
        total += value
        count += 1
        running_average = total/count

averager = running_averager()
next(averager)
averager.send(10) # yields the running_average = 10 
averager.send(20) # yields the running_average = 15
averager.send(30) # yields the running_average = 20
```

### Closing Generators

Consider this generator function to read files:
```
def read_file(fname):
    f = open(fname)
    try:
        for row in f:
            yield row
    finally:
        f.close()

rows = read_file('test.txt')
for _ in range(10):
    next(rows)
```
We read only 10 rows of the file, so the generator never closes the file and hence it remains open. How do we close the file without iterating through the entire file?

We want to be able to go from GEN_SUSPENDED to GEN_CLOSED from the caller. Generators have a close method. So when we run `rows.close()`, the `finally` block executes and the file is closed.

The only way for the program to exit out of the loop and reach the `finally` block is when an exception occurs. A `GeneratorExit` exception is triggered inside the generator. This is similar to the StopIteration exception. These exceptions are used to control the flow of things.

You can catch the `GeneratorExit` exception like this:
```
def gen():
    try:
        yield 1
        yield 2
    except GeneratorExit:
        print('Generator close called')
    finally:
        print('Clean up here')

g = gen()
next(g)
g.close()
```
Python's expectations when `close()` is called.

- a GeneratorExit eception bubbles up
```
def parse_file(fname):
    f = open(fname, 'r')
    try:
        reader = csv.reader(f)
        for row in reader:
            yield row
    finally:
        f.close()

parser = parse_file(fname)
for row in itertools.islice(parser, 10)
    print(row)
```
We let the `GeneratorExit` exception bubble up, and Python will silence it.
- the generator exits cleanly (returns)
```
def parse_file(fname):
    f = open(fname, 'r')
    try:
        reader = csv.reader(f)
        for row in reader:
            try:
                yield row
            except GeneratorExit:
                print('ignoring GeneratorExit')
                return # Exiting hhe generator cleanly
    finally:
        f.close()

parser = parse_file(fname)
for row in itertools.islice(parser, 10)
    print(row)
```

The exception that happens is silenced by Python, which means the caller will not see the exception. It is perfecty okay to not catch the `GeneratorExit` exception. It will be silenced by Python like the `StopIteration` exception.

You can catch the `GeneratorExit` exception and raise another exception and that can be seen by the caller.

You cannot catch the `GeneratorExit` exception, then ignore it and continue to yield values. In this case, Python will raise a `RuntimeError: generator ignored GeneratorExit`.
For e.g.
```
def parse_file(fname):
    f = open(fname, 'r')
    try:
        reader = csv.reader(f)
        for row in reader:
            try:
                yield row
            except GeneratorExit:
                print('ignoring GeneratorExit')
    finally:
        f.close()
```
Since coroutines are generator functions, it is okay to close a coroutine as well. For e.g., consider a coroutine that receives data to write to a database

- coroutine opens a transaction when it is primed
- coroutine receives data to write to the database
- coroutine commits the transaction when `close()` is called (`GeneratorExit`)
- coroutine aborts (rolls back) transaction if some other exception occurs

In the Python 3.8 version, at the end of a loop iterating over a generator, the `GeneratorExit` is automatically called. We dont need to call the `close` method.
```
def parse_file(fname):
    f = open(fname, 'r')
    try:
        reader = csv.reader(f)
        for row in reader:
            yield row
    finally:
        f.close()

parser = parse_file(fname)
for row in itertools.islice(parser, 10)
    print(row)
# End of loop, file is closed
```

Catching other exceptions that occur in the generator function
```
def save_to_db():
    print('starting new transaction')
    while True:
        try:        
            data = yield
            print('sending data to database: ', eval(data)) # eval used to create an exception
                                                            # we can catch 
        except Exception:
            print('aborting transaction') # Doing this leaves the generator in a 
                                          # suspended state
        except GeneratorExit:
            print('committing transaction')
            raise # Letting the generator exeption bubble back up
```
Once the abort takes place, we need to do two things:

- Abort the transaction and rollback
- Close the generator/coroutine

It would be safer to have a `finally` block there too.
```
def save_to_db():
    print('starting new transaction')
    is_abort = False
    try:
        while True:        
            data = yield
            print('sending data to database: ', eval(data))
    except Exception as ex:
        is_abort = True
        raise
    finally:
        if is_abort:
            print('rollback transaction')
        else:
            print('commit transaction')
```

### Sending Exceptions to Generators

We have seen ways to:

- `gen.send(data)` - sends data to coroutine
- `gen.close()` - sends (throws) a `GeneratorExit` exception to coroutine

We can also send (throw) any exception to the coroutine.

`gen.throw(exception)` - the exception is raised at the point where the coroutine is suspended.

How is `gen.throw()` handled?

- generator does not catch the exception (does nothing). The exception propogates to the caller.
- generator catches the exception and does something like:
    - yield a value (ignore the exception) 
    - exits (returns)
    - raise a different exception that will propogate back up to the caller

#### Catch and Yield

- generator catches the exception
- handles and silences the exception and yields a value
- yielded value is the return value of the `gen.throw()` method
```
def gen():
    while True:
        try:
            received = yield
            print(received)
        except ValueError:
            print('silencing ValueError') # The loop continues from back here
                                          # So the gen.throw() will return what is yielded.
```
#### Catch and Exit

- generator catches the exception
- generator exits (returns)

Caller receives the `StopIteration` exception. This is the same as calling `next()` or `send()` to a generator that returns instead of yielding. The generator is now closed.

gen.thow() sends exception while gen.send() sends data.
```
def gen():
    while True:
        try:
            received = yield
            print(received)
        except ValueError:
            print('silencing ValueError') 
            return None # StopIteration exception seen by the caller, not the ValueError
```
#### Catch and Raise Different Exception

- generator catches the exception
- generator handles it and raises another exception
- new exception propogates to the caller. Generator is now closed.
```
def gen():
    while True:
        try:
            received = yield
            print(received)
        except ValueError:
            print('silencing ValueError') 
            raise CustomException # seen by the caller
```
What happens when we call `gen.throw(GeneratorExit())`. To answer this, we need to revisit what happens when we call `gen.close()`. Python expects the `GeneratorExit` or `StopIteration` exceptions to propogate and silences it for the caller. However, when `gen.throw(GeneratorExit())` is called, `GeneratorExit` exception is raised inside the caller context (if the generator lets it). If you then want to silence it:

```
def gen():
    try:
        while True:
            received = yield
            print(received)
    finally:
        print('closing down')

try:
    g = gen()
    g.throw(GeneratorExit()) # This will propogate a GeneratorExit back to the caller.
except GeneratorExit:
    pass
```
However, if we catch the `GeneratorExit` exception in generator function, when we excute `g.throw(GeneratorExit()), it will be caught in thee generator function, but the StopIteration exception is raised at the caller. 

We can also use custom exception type to control the flow. For e.g.

```
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

sql = write_to_db()
next(sql)
sql.send(100)
sql.throw(CommitException)
sql.send(300)
sql.throw(RollBackException)
sql.close()
```
### Using Decorators to Prime Coroutines

We have to prime a coroutine before using it. It is repetitive and the pattern is the same everytime.
```
g = gen()
next(g) # can also do g.send(None)
```
Creating a function to auto prime coroutines:
```
def prime(gen_fn):
    g = gen_fn()
    next(g)
    return g

def echo():
    while True:
        received = yield
        print(received)

echo_gen = prime(echo)
echo_gen.send('hello')
```
We still have to call the prime function to prime the coroutine before using it. We can use a decorator to auto prime a coroutine for us when we create an instance of it.
```
def coroutine(gen_fn):
    def prime(*args, **kwargs):
        g = gen_fn(*args, **kwargs)
        next(g) # or g.send(None)
        return g
    return prime

@coroutine
def echo():
    while True:
        received = yield
        print(received)
```
In case an error occurs inside the generator function, the exception will bubble up and propogate to the caller who will see the exception. The generator will be close. If we want to silence any error, then we will have to catch it in the coroutine and silence it. 

### Yield From

#### 2-way Communication

Lets consider a generator function called subgen:
```
def subgen():
    for i in range(10):
        yield i
```
We can consume the data from subgen in another generator this way:
```
def delegator():
    for value in subgen():
        yield value
```
or we could use yield from:
```
def delegator():
    yield from subgen()
```
With either definition we can consume the generators this way:
```
d = delegator()
next(d)
```
We send the `next` request to the delegator. The delegator passes along the request to subgen because of the `yield from`. The subgen yields a value and passes it to delegator which passes it back to the caller. 

This is a 2-way communication. This means we can use `gen.send()`, `gen.close()` and `gen.throw()` too. 

Let us take a look at how the delegator behaves when subgen returns. Lets assume these functions:
```
def subgen():
    yield 1
    yield 2

def delegator():
    yield from subgen()
    yield 'subgen closed'
```
First we create an instance `d = delegator()`. Then

- We call `next(d)` and the delegator passes the request to `subgen` which yields 1 and passes it to delegator, which then passes it back to the caller. The delegator then suspends itself at the yield from statement.
- We call `next(d)` again and the same process repeats and we get 2.
- When we call `next(d)` again, the delegator passes the request to subgen, but the subgen now returns None. This means a `StopIteration` exception which python silences and we move to the next line in delegator function and it yields 'subgen closed'. The generator subgen is now closed.
- When we call `next(d)` then the delegator function returns None and `StopIteration` exception is raised at the caller.

#### Send data to coroutine

Lets send data to the coroutine using `yield from`. Consider the two functions:
```
def delegator():
    yield from coro()

def coro():
    while True:
        received = yield
        print(received)
```
First we create an instance `d = delegator`. We can prime the delegator using `next(d)`. When we do this, the `yield from` will automatically prime the coroutine when necessary.

Now that the coroutine and delegator is primed we can run `d.send('python')` and 'python' will be printed to the console.

We have to remember that the delegator control remains at the `yield from` till the coro generator closes.

We can create multiple delegators, effectively establishing a pipeline.
```
def coro():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from coro()

def gen1():
    yield from gen1()

d = gen1()
```
#### Flatten List

Suppose we want to flatten a list of lists to a single list. We have to use a recursive approach.
```
def flatten_print(curr_item):
    if isinstance(curr_item, list):
        for item in curr_item:
            flatten_print(item)
    else:
        print(curr_item)

def flatten_to_list(curr_item, output):
    if isinstance(curr_item, list):
        for item in curr_item:
            flatten_to_list(item, output)
    else:
        output.append(curr_item)

```
First one prints the items one-by-one to the console. The second one appends it to the output

However, in the second approach, we are passing the output around and appending values into it. If we are working with a large list, we will occupy a significant chunk of memory which might not be desirable. 

Lets use generators to avoid storing the list in memory.

```
def is_iterable(item, *, str_is_iterable=True):
    try:
        iter(item)
    except:
        return False
    else:
        if isinstance(item, str):
            if str_is_iterable and len(item) > 1:
                return True
            else:
                return False
        else:
            return True

def flatten_iterable(curr_item, *, str_is_iterable=False):
    if is_iterable(curr_item, str_is_iterable=str_is_iterable):
        for item in curr_item:
            yield from flatten_iterable(item)
    else:
        yield(curr_item)
```
#### Closing the delegator and subgenerator

Consider
```
def delegator():
    yield from subgen()

def subgen():
    yield 1
    yield 2

d = delegator()
```
When the caller calls `next(d)`, a conduit is established between delegator and subgen. The delegator is effectively paused at the yield from till the subgen closes. Once subgen closes, delegator runs the rest of its code.

We can get the handle of subgen from delegator and close it seperately. Then, the delegator continues with the rest of the code. When we execute `next(d)` then the delegator will yield if there is any subsequent yield statement or it will propogate the StopIteration exception back to the caller once it runs out of yield statments.

When we run `d.close()`, it gets transmitted to the subgenerator and it closes. It will immediately close the delegator too. The StopIteration exception is silenced by python in this case.

#### Returning from a subgenerator

When we return from a generator, we get a StopIteration exception. If there is a return value, then it is embedded in the StopIteration exception. We can extract it by:
```
try:
    next(g)
except StopIteration as e:
    print(e.value)
```
Python does this for us, so we dont have to. We can write as follows:
```
def subgen():
    yield 1
    yield 2
    return 3

def delegator():
    result = yield from subgen() # result get the return value from subgen

d = delegator()
next(d) # estabishes connection and prints 1
next(d) # prints 2
next(d) # prints 3
next(d) # StopItertion exception at the caller
```

