import sys
print(sys.hash_info.width)
print(list(map(hash, [1.1, 2.2, 3.3, 4.4])))
print(list(map(hash, ['hello', 'python', '!'])))
print(hash((1, 'a', 10.5)))