
class MyClass:

    def __init__(self, name, val):
        self.name = name
        self.val = val
    
    def __repr__(self):
        return f'MyClass({self.name}, {self.val})'
    
    def __lt__(self, other):
        return self.val < other.val
    
s = { 10, 2, 3, 2, 1, 0, 9, 11}

print(sorted(s))

d = {'a': 100, 'b': 50, 'c': 10}

print(sorted(d, key = lambda x: d[x]))

t = ('This', 'parrot', 'is', 'a', 'blue', 'one')

def sort_key(s):
    return len(s)

sorted(t, key=sort_key)

c1 = MyClass('c1', 20)
c2 = MyClass('c2', 10)
c3 = MyClass('c3', 20)
c4 = MyClass('c4', 10)

print(sorted([c1, c2, c3, c4]))
