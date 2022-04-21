# Context Managers

## What is a context?

It is the state of things when running a section of the code. Consider this piece of code:

```
# module.py
f = open('test.txt', 'r')
print(f.readlines())
f.close()
```
When `print(f.readlines())` runs, it has a context in which it runs, which is the global scope. If the piece of code is in a functions, then the context in which is runs is the local scope. 

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
with CtxManager() as obj:
    do_something()
# done
```
is the same as writing this piece of code
```
mgr = CtxManager()
obj = mgr.__enter__()
try:
    do_something()
finally:
    mgr.__exit__()
```
The above example is oversimplified as there is no exception handling there.

### Use Cases

- Creating a resource (opening a file) and releasing the resource (closing the file)
  A.k.a Open-Close
- Lock - Release (like lock a thread)
- Change - Reset (change the state of class and then reset, or changing precision of decimals)
- Start - Stop (Timer, or writing data to a stream and stop)
- Enter - Exit



