print('Is print callable? ', callable(print))

class Demo:
    def __init__(self, x):
        print('Initializing a counter class object with counter set at {0}...'.format(x))
        self.counter = x
    
    def __call__(self, x):
        print('Inrementing counter by {0}...'.format(x))
        self.counter += 1

demo = Demo(1)
print('Counter = {0}'.format(demo.counter))
demo(1)
print('Counter = {0}'.format(demo.counter))