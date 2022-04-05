import random
c = {}

def counter_fn(fn, c):
    count = 0
    def counter(*args, **kwargs):
        nonlocal count
        count += 1
        c[fn.__name__] = count
        return fn(*args, **kwargs)
    return counter

def add(a, b):
    return a+b

def mult(a, b):
    return a*b

def fact(a):
    return 1 if a<2 else a*fact(a-1)

add = counter_fn(add, c)
mult = counter_fn(mult, c)
fact = counter_fn(fact, c)

n = 20
answers = []
for _ in range(n):
    a = random.randint(0, 100)
    b = random.randint(0, 10)
    if _%2 == 0:
        answers.append((a, b, 'add', add(a, b)))
    if _%3 == 0:
        answers.append((a, b, 'mult', mult(a, b)))
    if _%4 == 0:
        answers.append((b, 'fact', fact(b)))

print(c)
print(answers)