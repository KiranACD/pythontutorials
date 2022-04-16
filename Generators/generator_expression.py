
g = ((i**2) for i in range(5))

for item in g:
    print(item)

start = 1
stop = 10

mult_list = ((i*j for j in range(start, stop+1)) for i in range(start, stop+1))

for row in mult_list:
    for item in row:
        print(item, end = ', ')
    print()