def multiply(a: float, b: float =1) -> float:
    '''
    Description: Multiplies 2 numbers a, b. If b is not provided, default of b = 1 is taken.

    Input : a, b
    output : a*b

    returns a*b
    '''

    return a * b

print('Printing out the documentation of multiply(a, b=1) using help(multiply)')
print(multiply.__doc__)
print(multiply.__annotations__)

