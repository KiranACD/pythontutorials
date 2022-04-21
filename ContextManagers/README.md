# Context Managers

## What is a context?

It is the state of things when running a section of the code. Consider this piece of code:

```
# module.py
f = open('test.txt', 'r')
print(f.readlines())
f.close()
```
When `print(f.readlines())` runs, it has a context in which it runs, which is the global scope. If the piece of code is in a function, then the context in which is runs is the local scope. 

## Managing the context

```
f = open('test.txt', 'r')
perform_work(f)
f.close()
```
If there is an exception before we close the file, the file remains open. We need to manage the context that perform_work(f) needs without causing disruption.

We can write it like this
```
f = open('test.txt', 'r')
try:
    perform_work(f)
finally:
    f.close()
```
But adding try/finally everytime will get cumbersome and, not to mention, you could forget it.

This is where context managers come in.

## Context Managers

- create a context (minimal amount of code needed for a block of code)
    - open the file
- execute the code that uses variables from the context
    - read the file
- automatically clean up the context when we are done with it
    - close the file

Example
```
with open('test.txt', 'r') as f: # Enters the context
    print(f.readlines()) # work inside the context

# exits the context
```
Context managers manage data within our scope. It useful for anything that needs an Enter/Exit or Start/Stop, Set/Reset
For e.g.,

- open/close file
- start db transaction / commit or abort transaction
- set decimal precision to 3 / reset back to original precision

### try/except/finally

Making a small detour, finally block always runs, even when the return statement of a function is in the try or except block. This is useful for writing code that should execute no matter what happens. As we saw earlier, it can get cumbersome.

### Motivations

Thought process explained in [PEP 343](https://peps.python.org/pep-0343/)

### Pattern

- create object
- do some work with object
- clean up object after use automatically

```
with context as obj_name: # with open(file) as f:  Here context is created by open(file)
                                                    # Return object which is f
    # file is open
    read(file)

# close the file automatically
```
### Context management protocol

Classes implement the context manager protocol by implementing two methods:
- __enter__ - setup and optionally return an object
- __exit__  - teardown/cleanup

This
```
with CtxManager() as obj: # instance of the class is created but there is no associated
                          # symbol. 
    do_something()
# done
```
is the same as writing this piece of code
```
mgr = CtxManager()
obj = mgr.__enter__() # Return value from enter is assigned to obj
try:
    do_something()
finally:
    mgr.__exit__()
```
The above example is oversimplified as there is no exception handling there.

What happens if an exception occurs inside the with block? The __exit__ method is called.

### Use Cases

- Creating a resource (opening a file) and releasing the resource (closing the file)
  A.k.a Open-Close. Another example is open a socket, operate on socket, close socket
- Lock - Release (like lock a thread)
- Change - Reset (change the state of class and then reset, or changing precision of decimals)
```
class precision:
    def __init__(self, prec):
        self.prec = prec
        self.current_prec = decimal.getcontext().prec

    def __enter__(self):
        decimal.getcontext().prec = self.prec
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        decimal.getcontext().prec = self.current_prec

with precision(3):
    print(decimal.Decimal(1) / decimal.Decimal(3))
```
- Start - Stop (Timer, or writing data to a stream and stop, start db transaction, perform db operations, commit or rollback transaction)
- Enter - Exit
- Wacky stuff
```
with tag('p'):
    print('some text', end='')

with tag('p'):
    print('some', end='')
    with tag('b'):
        print('bold', end='')
    print('text', end='')
```
Another example:
```
with ListMaker(title='Items', prefix='-', indent=3, stdout='myfile.txt') as lm:
    lm.print('Item1')
    with lm:
        lm.print('item 1a')
        lm.print('item 1b')
    lm.print('Item2')
    with lm:
        lm.print('item 2a')
        lm.print('item 2b')
```
The output, written into myfile.txt will look like
```
Items
    - Item1
        - item 1a
        - item 1b
    - Item2
        - item 2a
        - item 2b
```

### Scope of with block

The with block is not like a function or a comprehension. It does not have its own local scope. The scope of anything in the with block is in the same scope as the with statement itself.

```
with open(file) as f:
    row = next(f) # Both f and row are in the global scope
print(f)
print(row)
```
However, the file will be closed when we come out of the with block.

### The __enter__ method

`def __enter__(self):` - signature
This method should perform what you want to be done when you enter a context. It can optionally return an object. It can also return None.

### The __exit__ method

This should always run even if an exception occurs in the `with` block. But, should it be able identify if an exception occured? Yes. And it needs to know whether to let the exception propogate or whether to silence it.

For example
```
with Context() as obj:
    raise ValueError # some error
print('done')
```
- Scenario 1

__exit__ method receives the error, performs some clean up and silences the error. No exception seen.

- Scenario 2

__exit__ method receives the error, performs the clean up ad lets the error propogate. ValueError is seen.

It needs three arguments:

- the exception type that occured(if any, None otherwise)
- the exception value that occurred(if any, None otherwise)
- the traceback object if an exception occurred(if any, None otherwise)

Return True or False. If True, silence any raised exception. If False, do not silence a raised exception.

What __exit__method needs to look like
```
def __exit__(self, exc_type, exc_value, exc_trace):
    do_cleanup()
    return True # or False
```

### Caveat with lazy iterators

Consider this piece of code:
```
import csv

def read_data():
    with open('file.csv') as f:
        return csv.reader(f, delimiter=',', quotechar='"')

reader = read_data()
for row in reader:
    print(row)
```
What do you think will happen? It is going to raise an exception as the file has been closed. 
This is why we cannot return a file iterator from a context managers and hence we need to write it as:
```
import csv

def read_data():
    with open('file.csv') as f:
        yield from csv.reader(f, delimiter=',', quotechar='"')

reader = read_data()
for row in reader:
    print(row)
```

Of course, we could return a list from the read_data() function instead of an iterator, but that defeats the purpose of using a lazy iterator.

### Combining iterator protocol and context manager protocol

```
class DataIterator:
    def __init__(self, fname):
        self._fname = fname
        self._f = None
    
    def __iter__(self):
        return self
    
    def __next__(self):
        row = next(self._f)
        return row.strip('\n').split(',')
    
    def __enter__(self):
        self._f = open(self._fname)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if not self._f.closed:
            self._f.close()
    
        return False

# Implement it like this
with DataIterator('data_file.csv') as data:
    for row in data:
        print(row)
```
### Mimic context manager pattern using a generator

```
def open_file(fname, mode):
    f = open(fname, mode)
    try:
        yield f
    finally:
        f.close()

ctx = open_file('file.txt', 'r)
f = next(ctx) # Opens file and yields it
next(ctx # closes the file)
```
The better way of writig the above function:
```
ctx = open_file('file.txt', 'r'):
f = next(ctx)
try:
    do_work_with_file()
finally:
    try:
        next(ctx)
    except StopIteration:
        pass
```
How it works in general is:
```
def gen(args):
    #  do set up work here

    try:
        yield object
    finally:
        # clean up object here

ctx = gen(args)
obj = next(ctx)

try:
    do_with obj()
finally:
    try:
        next(ctx)
    finally:
        try:
            next(ctx)
        except StopIteration:
            pass
```
This is still clunky. 