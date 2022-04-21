
try:
    10/2
except ZeroDivisionError:
    print('Zero division error')
finally:
    print('Done')

try:
    10/0
except ZeroDivisionError:
    print('Zero division error')
finally:
    print('Done')

def my_func():
    try:
        10/0
    except ZeroDivisionError:
        print('Zero division error')
        return
    finally:
        print('Done')

my_func()

try:
    print('Opening file...')
    f = open('file.txt', 'w')
    a = 1/0
except:
    print('Exception occured')
finally:
    print('Closing file...')
    f.close()

with open('test.txt', 'w') as file:
    print('inside with: file closed?', file.closed)

print('after with: file closed?', file.closed)

class MyContext:

    def __init__(self):
        self.obj = None
    
    def __enter__(self):
        print('entering context...')
        self.obj = 'the return obj'
        return self.obj
    
    def __exit__(self, exc_type, exc_value, exc_traceb):
        print('exiting context...')
        if exc_type:
            print(f'Error occurred: {exc_type}, {exc_value}')
        return False


# with MyContext() as obj: # can define ctx = MyContext() and the write with ctx as obj:
#     print('Entering with block')
#     raise ValueError('Lo, Behold! A ValueError') # On seeing this Python calls the __exit # method first

# print(obj) # obj available after the context has closed. 

class Resource:
    def __init__(self, name):
        self.name = name
        self.state = None

class ResourceManager:
    def __init__(self, name):
        self.name = name
        self.resource = None
    
    def __enter__(self):
        print('Entering context...')
        self.resource = Resource(self.name)
        self.resource.state = 'created'
        return self.resource
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        print('exiting context')
        self.resource.state = 'destroyed'
        if exc_type:
            print('error occurred')
        return False
    

# with ResourceManager('Spam') as res:
#     print(f'{res.name} = {res.state}')

# print(f'{res.name} = {res.state}')

class File:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
    
    def __enter__(self):
        print('opening file...')
        self.file = open(self.name, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        print('closing file...')
        self.file.close()
        return False

with File('ContextManagers/test.txt', 'w') as f:
    f.write('This is a late parrot!')   

with File('ContextManagers/test.txt', 'r') as f:
    print(f.readlines())