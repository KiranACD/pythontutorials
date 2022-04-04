def factorial(n, cache={}):
    if n<1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('Calculating {0}!'.format(n))
        result = n*factorial(n-1)
        cache[n] = result
        return result

while(True):
    try:
        num = int(input('Enter the number (Hit "n" when you want to stop): '))
        print(factorial(num))
    except:
        break

print('Done!')