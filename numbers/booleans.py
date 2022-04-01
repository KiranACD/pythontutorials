
print('Is bool a subclass of int? ', issubclass(bool, int))

print('Truthyness of any number, lets say 100 and -1: ', bool(100), bool(-1))
print('None object type always evaluates to: ', bool(None))

print('An object also evaluates to False when it is an empty list or dictionary or tuple: ', bool([]), bool({}), bool(()))
