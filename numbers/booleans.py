import string

print('Is bool a subclass of int? ', issubclass(bool, int))

print('Truthyness of any number, lets say 100 and -1: ', bool(100), bool(-1))
print('None object type always evaluates to: ', bool(None))

print('An object also evaluates to False when it is an empty list or dictionary or tuple: ', bool([]), bool({}), bool(()))

# default object always evaluates to true except for some exceptions. Truthyness of objects

a = ''
if a:
    print('String is not empty')
else:
    print('String is empty')

while True:
    name = input('Enter you name (eg: Bruce Lee): ')
    print(name[0])
    print(name)
    if name and name[0] not in string.digits and name[0] in string.ascii_uppercase and len(name.split())>1:
        print('The name is valid')
        break
    else:
        print('The name is not valid. Try again!')

# To avoid division by 0

while True:
    print('Now we divide a/b')
    a = int(input('Enter number a: '))
    b = int(input('Enter number b: '))
    c = int(b and a/b)
    print('a/b: ', c)
    if not(b):
        print('Check the answer when we entered 0 for the denominator')
        print('Try again!')
    else:
        print('Done!')
        break


