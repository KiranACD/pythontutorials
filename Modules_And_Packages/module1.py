# Module1.py

print(f'----------------------------- Running {__name__} --------------------------------')

def pprint(header, d):
    print('\n\n-----------------------------------------')
    print(f'*********** {header} ***********')
    for key, value in d.items():
        print(key, value)
    print('-----------------------------------------\n\n')

pprint('module1.globals', globals())

print(f'----------------------------- End of {__name__} ---------------------------------')


