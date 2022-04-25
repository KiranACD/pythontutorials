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
