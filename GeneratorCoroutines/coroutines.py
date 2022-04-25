from collections import deque

def produce_elements(dq):
    for i in range(1, 36):
        dq.appendleft(i)

def consume_elements(dq):
    while dq:
        item = dq.pop()
        print('processing item: ', item)

def coordinator():
    dq = deque()
    produce_elements(dq)
    consume_elements(dq)


def produce_elements(dq, n):
    for i in range(1, n):
        dq.appendleft(i)
        if len(dq) == dq.maxlen:
            print('queue full - yielding control')
            yield

def consume_elements(dq):
    while True:
        while dq:
            item = dq.pop()
            print('processing: ', item)
        print('queue empty - yielding control')
        yield

def coordinator_():
    dq = deque(maxlen = 10)
    producer = produce_elements(dq, 50)
    consumer = consume_elements(dq)
    while True:
        try:
            print('producing')
            next(producer)
        except StopIteration:
            break
        finally:
            print('consuming...')
            next(consumer)

coordinator_()


# coordinator()
