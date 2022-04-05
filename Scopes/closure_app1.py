class Averager:
    def __init__(self):
        self.numbers = []
    def add(self, num):
        self.numbers.append(num)
        return sum(self.numbers)/len(self.numbers)

avg = Averager()
print(avg.add(10))
print(avg.add(20))
print(avg.add(30))

def averager():
    numbers = []
    def add(num):
        numbers.append(num)
        return sum(numbers)/len(numbers)
    return add

avg_fn = averager()
print(avg_fn(10))
print(avg_fn(20))
print(avg_fn(30))

def averager_():
    total = 0
    count = 0
    def add(num):
        nonlocal total
        nonlocal count
        total += num
        count += 1
        return total/count
    return add

avg_fn_ = averager_()
print(avg_fn_(10))
print(avg_fn_(20))
print(avg_fn_(30))
