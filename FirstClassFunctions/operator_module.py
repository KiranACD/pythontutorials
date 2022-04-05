import operator

a = 1
b = 2
print('{0} + {1} = {2}'.format(a, b, operator.add(a, b)))
print('{0} * {1} = {2}'.format(a, b, operator.mul(a, b)))
print('{0} / {1} = {2}'.format(a, b, operator.truediv(a, b)))
print('{0} // {1} = {2}'.format(a, b, operator.floordiv(a, b)))

print('Truthiness of [] is {0}'.format(operator.truth([])))

x = 'abc'
y = 'def'
print('Is {0} same as {1}? {2}'.format(x, y, operator.is_(x, y)))

l = [1, 2, 3]

print("Changing value at index {0} of list = {1} using operator.setitem to 100".format(2, l, operator.setitem(l, 2, 100)))

class Demo:
    def __init__(self):
        self.a = 10
        self.b = 20
    
    def test(self):
        return self.a + self.b
    
    def test2(self, c):
        return self.a + self.b + c

prop_a = operator.attrgetter('a')
demo = Demo()

print('Attribute a is: ', prop_a(demo))

prop_test = operator.attrgetter('test')

print('Result of test method is: ', prop_test(demo)())

prop_test_method = operator.methodcaller('test')

print('Result of test method using method caller is: ', prop_test_method(demo))

prop_test2_method = operator.methodcaller('test2', 100)

print('Result of test method using method caller is: ', prop_test2_method(demo))