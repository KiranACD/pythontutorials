class WriteAverage(Exception):
    pass

def averager(outfile):
    total = 0
    count = 0
    average = None
    with open(outfile, 'w') as f:
        f.write('count,average\n')
        while True:
            try:
                value = yield average
                total += value
                count += 1
                average = total/count
            except WriteAverage:
                if average is not None:
                    print('saving average to file: ', average)
                    f.write(f'{count},{average}\n')

avg = averager('GeneratorCoroutines/Data/sample.csv')
next(avg)

print(avg.send(1))
print(avg.send(2))
avg.throw(WriteAverage)
avg.close()