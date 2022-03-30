# custom encoding
def from_base10(n, b):
    if b < 2:
        raise ValueError('Base b must be >= 2')
    if n < 0:
        raise ValueError('Number n must be >= 0')
    if n == 0:
        return [0]
    
    digits = []
    while n:
        digits.append(n%b)
        n = n//b
    digits = digits[::-1]

    return digits

def encoding(digits, digitmap):

    if max(digits) > len(digitmap):
        raise ValueError('digitmap is not long enough to encode digits')
    
    encoding = ''.join([digitmap[d] for d in digits])

    return encoding


if __name__ == '__main__':

    print('FF in base 16: ', int('FF', 16))

    try:
        print('B in base 12: ', int('B', 11))
    except ValueError as e:
        print('Error while representing B in base 11: ', e)
    
    DIGITMAP = '0123456789ABCDEFGHIJKLMNOPGRSTUVWXYZ'

    while True:
        n = int(input('Enter number: '))
        b = int(input('Enter base b: '))

        try:
            digits = from_base10(n, b)
            base_rep = encoding(digits, DIGITMAP)
            print(base_rep)
        except ValueError as e:
            print(e)
        
        x = input('Do you want to continue? [Y] or [N]: ')
        if x == 'Y':
            continue
        else:
            break
    
    print('Exiting the app')


        



