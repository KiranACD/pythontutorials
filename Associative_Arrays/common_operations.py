from itertools import chain
import string


d = dict(zip('abc', range(1, 4)))
print(d)
print('----------------------------------------------')
print(len(d))
print('----------------------------------------------')
print(d['a'])
print('----------------------------------------------')
dvalue = 'N/A'
print(d.get('python', dvalue))
print('----------------------------------------------')

text = 'the quick brown fox jumps over the lazy dog'
counts = dict()
for c in text:
    key = c.lower().strip()
    if key:
        counts[key] = counts.get(key, 0) + 1
print(counts)

print('----------------------------------------------')

d = dict.fromkeys('abcd', 0)

print(d)
print('----------------------------------------------')

print(d.pop('b'))
print('----------------------------------------------')
print(d.pop('b', 'N/A'))
print('----------------------------------------------')
print(d.popitem())
print('----------------------------------------------')
def insert_if_not_present(d, key, value):
    if key not in d:
        d[key] = value
        return value
    else:
        return d[key]

print(insert_if_not_present(d, 'z', 100))
print('----------------------------------------------')
print(insert_if_not_present(d, 'a', 100))
print('----------------------------------------------')
print(d.setdefault('a', 100))
print('----------------------------------------------')
print(d.setdefault('e', 100))
print('----------------------------------------------')

text2 = 'The quick brown fox, looks around, and then, jumps over the lazy dog! That\'s graceful!%!%!%'

categories = {}
for c in text2:
    if c != ' ':
        if c in string.ascii_lowercase:
            key = 'lower'
        elif c in string.ascii_uppercase:
            key = 'upper'
        else:
            key = 'other'
        if key not in categories:
            categories[key] = set()
        
        categories[key].add(c)

for cat in categories:
    print(f'{cat}: ', ''.join(categories[cat]))

print('----------------------------------------------')

text2 = 'The quick brown fox, looks around, and then, jumps over the lazy dog! That\'s graceful!%!%!%'

categories = {}
for c in text2:
    if c != ' ':
        if c in string.ascii_lowercase:
            key = 'lower'
        elif c in string.ascii_uppercase:
            key = 'upper'
        else:
            key = 'other'
        
        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'{cat}: ', ''.join(categories[cat]))

print('----------------------------------------------')
text3 = 'The quick brown fox, looks around, and then, jumps over the lazy dog! That\'s graceful!%!%!%'

def get_cat_key(c):
    if c == ' ':
        return None
    elif c in string.ascii_lowercase:
        return 'lower'
    elif c in string.ascii_uppercase:
        return 'upper'
    else:
        return 'other' 

categories = {}
for c in text3:
    key = get_cat_key(c)
    if key:
        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'{cat}: ', ''.join(categories[cat]))

print('----------------------------------------------')
text4 = 'The quick brown fox, looks around, and then, jumps over the lazy dog! That\'s graceful!%!%!%'

cat_keys = {' ': None,
            string.ascii_lowercase: 'lower',
            string.ascii_uppercase: 'upper'}

def get_cat_key1(c):
    for key in cat_keys:
        if c in key:
            return cat_keys[key]
    # when for loop runs fully till the end
    else:
        return 'other'

categories = {}
for c in text4:
    key = get_cat_key1(c)
    if key:
        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'{cat} ', ''.join(categories[cat]))

print('----------------------------------------------')
text5 = 'The quick brown fox, looks around, and then, jumps over the lazy dog! That\'s graceful!%!%!%'

cat_1 = {' ': None}
cat_2 = dict.fromkeys(string.ascii_lowercase, 'lower')
cat_3 = dict.fromkeys(string.ascii_uppercase, 'upper')

def get_cat_key2(c):
    categories = dict(chain(cat_1.items(), cat_2.items(), cat_3.items()))
    # categories = {**cat_1, **cat_2, **cat_3}
    return categories.get(c, 'other')

categories = {}
for c in text5:
    key = get_cat_key2(c)
    if key:
        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'{cat} ', ''.join(categories[cat]))
