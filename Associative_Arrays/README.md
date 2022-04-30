# Associative Arrays

Dictionary (a.k.a associative array) is an abstract data structures. So, there are many ways to implement them. Specifically we are going to implement them using hash tables (a.k.a hash maps)

Dictionaries are everywhere in Python. Modules, classes, objects, scopes, sets, your own dictionaries are all dictionaries.

## What is an associative array?

Consider this list of objects:

`persons = [John, Eric, Michael, Graham]`

We can think of indices a key for the items in the list. To get a hold of the Michael object, we just need to remember the key.

`persons[2]`

However, you should not be expected to remember the index number associated with objects in lists while programming. We might have other lists where the same index numbers are associated with other objects.

Lets make a change to the persons list:
`persons = [('john', John), ('eric', Eric), ('michael', Michael), ('graham', Graham)]`

We have associated a string with each object. Now to get the Michael object, we need to lookup the key 'micahel' and return the associated value. We can iterated over the tuples in the list until we find one with the first element equal to the key. Once we find it, we return the second element of the tuple.

We dont have to remember numbers anymore, but we still have to iterate over a list each time to find our key. There has to be a better way...

Lets break up the persons list from earlier to
```
keys = ['john', 'eric', 'michael', 'graham']
persons = [John, Eric, Michael, Graham]
```
The index of 'john' always match up with the index of John. So, we could define a function h that would return these results always

`h('john')` --> 0, `h('eric')` --> 1 etc...

To get Michael, we would do `persons[h('michael')]`.

Now we are getting a sense of what associative arrays are. They associate keys (that are unique) to values. Abstractly, we can think of them as (key, value) pairs. 

They are also called maps, dictionaries.

All implementations of associative arrays should support the following:

- adding/removing (key, value) pairs
- modifying an associated value
- looking up a value via its key

## Hash Maps

One common concrete implementation of an associative array is a hash map.

Suppose we have an array of 7 slots, initially containing nothing. For now, we have indices associated with each of the slots. Suppose we want to store these maps:

- 'john' --> John 
- 'eric' --> Eric
- 'michael' --> Michael
- 'graham' --> Graham

in a dictionary and we want to retreive these items by using a key (string as we see above).

We will define a function that will return an integer value for all these strings ('john', 'eric' etc). There are going to be a few condtions:

- integer value must be unique for each of these strings
- is between 0 and 6.
- always returns the same integer for the same string

Say our function produces the followig results:

- h('john') --> 2, 
- h('eric') --> 4, 
- h('michael') --> 0, 
- h('graham') --> 5

So we can now store the objects at the indices returned by the hash function when applied to the strings. John will go to index 2, Eric will go to position 4, Michael will go to 0, Graham will go to position 5.

In short, to store a key/value pair:
- calculate h(key) --> idx
- store value in slot idx

To look up a value by key
- calculate h(key) --> idx
- return value in slot idx

### Hash Functions

Creating the function h(key) when we know all the possible keys ahead of time is easy. But this is not the case. 

Bounding the resturned index value can be done usig modulo. Ensuring uniqueness of the return integer value of hash function on an input is hard. We have to ensure h(k1) != h(k2) if k1 != k2.

Maybe we dont need to. Maybe we can drop this requirement.

Hash function is a function, x = y ==> f(x) = f(y), that maps from a set(domain) of abitrary size (possibly infinite) to another (smaller) set of fixed size (range).

h:D --> R where cardinality of R < cardinality of D

For our hash tables, we want:
- the range to be a defined subset of the non-negative integers 0, 1, 2, 3, ...
- the generated indices for expected input values to be uniormly distributed (as much as possible). Now that we have allowed the hash function to return the same integer for different inputs, we dont want the generated indices to be in a small grouping amongst the empty slots. We want them to be spread out.

A simple way would be:
```
def h(key, num_slots):
    return len(key) % num_slots # assuming key as strings
```
- h('alexander', 11) --> 9
- h('john', 11) --> 4
- h('eric', 11) --> 4
- h('michael', 11) --> 7
- h('graham', 11) --> 6

There is a collision between john and eric. If we take the num_slots as 5:

- h('alexander', 5) --> 4
- h('john', 5) --> 4
- h('eric', 5) --> 4
- h('michael', 5) --> 2
- h('graham', 5) --> 1

There are three collisions now, between alexander, john and eric.

Lets take another function:
```
def h(key, num_slots):
    total = sum(ord(c) for c in key)
    return total % num_slots
```
- h('alexander', 11) --> 948 % 11 = 2
- h('john', 11) --> 431 % 11 = 2
- h('eric', 11) --> 419 % 11 = 1
- h('michael', 11) --> 723 % 11 = 8
- h('graham', 11) --> 624 % 11 = 8

All these hash functions have collisions

How do we deal with collisions?

#### Chaining

Given the output from the above hash function, we store ['alexander', Alexander] in slot number 2, ['john', John] in the same slot, ['eric', Eric] in slot number 1, ['michael', Michael] in slot 8, ['graham', Graham] in slot 8 too. So we end up with a list of lists in some slots. When want to lookup a particular key, we get the index value from the hash function for the key and we iterate over the list of lists in the associated slot until we find our key.

This is relatively efficient when compared to iterating over all five elements everytime we looked up a key. This is also why we want the index values returned by our hash function be spread out. This minimizes the number of collisions and we have fewer items to iterate over in each slot on average.

#### Probing (Linear)

Consider the same hashing function as above and its output and the probe sequence:

- h('alexander', 5) --> 948 % 5 = 3    3 -> 4 -> 0 -> 1 -> 2
    - The hash value will always be the same and the probe sequence will always be the same.   We put ['alexander', Alexander] at slot number 3.

- h('john', 5) --> 431 % 5 = 1         1 -> 2 -> 3 -> 4 -> 0
    - We put ['john', John] at 1 because there was an empty slot. 

- h('eric', 5) --> 419 % 5 = 4         4 -> 0 -> 1 -> 2 -> 3
    - We put ['eric', Eric] at slot number 4 as it is empty.

- h('michael', 5) --> 723 % 5 = 3      3 -> 4 -> 0 -> 1 -> 2
    - Slot number 3 is already taken by Alexander, 4 is taken up by Eric. Slot 0 is empty, so we put ['eric', Eric] at slot number 0.

- h('graham', 5) --> 624 % 5 = 4       4 -> 0 -> 1 -> 2 -> 3
    - Slot number 4 is occupid by Eric, 0 is taken up by Michael, 1 is taken up by John, so we put graham in slot number 2 as it is empty

There are other types of probing.

Lets find out how to fetch Alexander. The hash value is 3, and we check if 'alexander' is at 3. In this case, it is, so we return Alexander.

To find Michael, get the hash value of 'michael' which is 3. As 'michael' is not at 3, we next check 4 and we find 'michael' is not at 4 either. Finally, moving along the probe sequence, we find 'michael' is at 0 and we return Michael.

This is the basic idea of how to use hash function.

#### Sizing Issues

When we create a hash table, how big should it be? 

- We cannot make it arbitrarily large as there are memory constraints. 
- Start small and grow it over time as needed.
- resizing is expensive as you need to recompute hashes and move data around. 
- over allocate. Say we start with 10 slots. Once all slots are filled, instead of resizing it to 11, we resize it to 15 slots. Then, once we reach 15, resize to 25. And so on...

#### Other Issue

Deleting items can affect the probing algorithm, as you leave holes in there. We also need to compact the table when items are deleted.
Hash function output needs to be evenly distriuted, satisfy the requirements of hash functions, and the probe sequence needs to be decent as well.


## Python Dictionaries

### Key Sharing

Suppose we have this class:
```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```
Multiple instances of this class could be:
```
john = Person('John', 78)
eric = Person('Eric', 75)
michael = Person('Michael', 75)
```
Each of the objects are essentially dictionaries. The dictionary would have ['name', 'John'] and ['age', 78] and similar struture for the other objects. It would be redundant to have the multiple name, age three times. 

We can pull name, age out as a seperate object and we maintain another object that has the values of the name and age. 

This is also called a split table dictionary. Key sharing helps multiple instances of the same cash have more efficient storage. 

### Compact Dictionaries

Consider this dictionary `{'alex':Alex, 'john':John, 'eric':Eric}`.

- hash('alex') --> 3
- hash('john') --> 1
- hash('eric') --> 6

Assume we have dictionary with 7 slots and we have populated three of those slots. 'john' is at 1, 'alex' is at 3 and 'eric' is at 6. How do we represent this?
```
[['-', '-', '-'],
 [-6350376054362344353, 'john', John],
 ['-', '-', '-'],
 [4939205761874899982, 'alex', Alex],
 ['-', '-', '-'],
 ['-', '-', '-'],
 [6629767757277097963, 'eric', Eric]
]
```
The first element in the non-empty list is the hash value. We store the hash value because it is fast and efficient to compare integers. So we start the comparison with the hash value rather than comparing strings. A point to note here is that the key order in the slots is different from the insertion order. 

What happens in compact dictionaries is that we store the data into 2 seperate lists. The first one is going to just be the items. 
```
values = [
          [4939205761874899982, 'alex', Alex],
          [-6350376054362344353, 'john', John],
          [6629767757277097963, 'eric', Eric]
         ]
indices = [None, 1, None, 0, None, None, 2]
```
The key order in the values list is the same as the insertion order. The indices list maps the hash value of the key to the position in the values list. If we want to find Alex, the hash value of hash('alex') is the 3, so we go to values[indices[3]] to find Alex.

## Python Hash

The python buit-in function always returns an int. It satisfies the condition that if a==b is True, then hash(a) == hash(b) is also True. Python truncates hashes to some fixed size. You can find the size by running `sys.hash_info.width`. Of course, you will have to import the sys module. 

- `map(hash, [1, 2, 3, 4])` --> 1, 2, 3, 4
- `map(hash, [1.1, 2.2, 3.3, 4.4])` --> 230584300921369601, 461168601842739202, 691752902764107779, 922337203685478404
- `map(hash, ['hello', 'python', '!'])` --> -9163354275683762850, -7847635527679356851, -4573390878920968095
- `hash((1, 'a', 10.5))` --> 3594221671904477154

The last item shows we can hash a tuple as well. But we cannot hash sequence types that are mutable as they cannot be hashed. We cannot hash an immutable data type, if it has a mutable data type within it. 

This is because hash values are used for hash tables which is used to determine the position index, and the start values of the probe sequence. 
- The hash of an immutable data type named 'a' will never change 
- When we look for dict[a], we will always look for a at the same index. 

- The hash of a mutable data type will change. 
- We will end up looking at the wrong index. 

Two identical tuples will still be different objects occupying different memory slots. However its hash values are determined by the content of the tuple. If you make a key:value pair with one of the identical tuple as the key, then we can retreive the value using the other tuple as well, because the hash values of both tuples are the same.

The hash value of an object changes from run-to-run. You can rely on them being the same in a single program run, but not across runs. 


# Dictionaries

## Dictionary Elements

Basic structure of dictionary elements key:value. The value can be any python object. The key on the other hand need to be a hashable object. The hash table requires the hash of an object to be constant in the lifetime of a program run. 

### Hashable Objects

The Python function hash(obj):

- Returns some integer truncated based on Python build: 32-bit, 64-bit.
- Raises exception if obj is unhashable type.

Listing out objects that are hashable:

- int, float, complex, binary, Decimal, fraction --> immutable --> hashable
- strings --> immutable collection --> hashable
- frozenset --> immutable collection --> elements within are required to be immutable --> hashable
- tuples --> immutable collection --> hashable only if all elements are also hashable.
- set, dictionary --> mutable collection --> not hashable
- list --> mutable collection --> not hashable
- functions --> immutable. Yes, you can change the metadata, the docstring, but you cannot change the function itself --> hashable
- custom classes and objects --> maybe

Requirments for an object to be hashable:

- the hash value of the object must be an integer value. It is to be used as the start value of a probe sequence. 
- if two objects are equal, then the hashes must also be equal.

Two objects that do not compare equal, may have the same hash. This is known as hash collision. More the number of hash collisions, slower the dictionary, because, to find a key now, we have to do multiple probes into the associative array inorder to find that key. 

Python does a certain amount of randomization to generate these hash values because if it were predictable, any particular website may be attacked by forcing the values to go into that dictionary that have the same key and hence slow down the system. 

We have to follow these requirements of hashes when we create custom hashes as well.

## Creating Dictionaries

### Literals

```
{key1 : value1,
 key2 : value2,
 key3 : value3}
```
### Constructor

`dict(key1=value1, key2=value2, key3=value3)`

When we use this approach, the key should be a valid idenntifier name. The dictionary key will be a string of that name.

if we have an existing dictionary d1 and we make a new dictionary `d2 = dict(d1)`, then d2 becomes a shallow copy of d1. 

### Comprehensions

`{str(i): i**2 for i in range(1, 5)}` --> {'1':1, '2':4, '3':9, '4': 16}

### Using fromkeys()

`fromkeys()` is a class method on dict. It creates a dictionary with depcified keys all assigned the same value. 

`d = dict.fromkeys(iterable, value)`. All the items from the iterable, provided they are immutable, will become keys and will be assigned value. If value is not provided, they will be assigned None. 


## Common Operations

`d[key] = value`

- Creates a key if it idoes not exist
- Assigns a value to key

`d[key]`

- As an expression, returns the value for the specified key
- exception KeyError if key is not found

`d.get(key)`

- Return value if key is found, None if key is not found
- Default return value can be specified. `d.get(key, default)

`key in d` or `key not in d` 

- Membership testing - Test if a key is present in the dictionary or not.
- Hash a key a do a probe in the hash table looking for the hash value of the key. Hence, key membership testing is efficient in Python. 
- True if key is in d, False if not. 
- To test if a value is present in the dictionary, we have to iterate through the values of the dictionary and hence, is not as efficient as searching for a key.

`len(d)` - Return the number of items in dictionary

`d.clear()`

- Clears out all items in dictionary
- It does an inplace change in the dictionary.
- Assigning d = {} replaces the old object with the new empty dictionary object.

`del d[key]`

- Removes element with that key from d
- exception KeyError if key is not in d

`d.pop(key)`

- Removes the element with that key from d
- Returns the corresponding value
- exception KeyError if key is not in d
- Adding default as argument avoids the KeyError exception. If key is not in d, it returns the default value specified.

`d.popitem()`

- Removes an item from d
- Returns tuple (key, value)
- KeyError if dictionary is empty
- Python 3.6+, it will remove the last inserted item - guaranteed.

`result = d.setdefault(key, value)`

- To insert a key with a default value only if key does not exist.

```
d = {'a': 1, 'b': 2}
if 'c' not in d:
    d[c] = 0
```
Combine this with returning the newly inserted (default) value or existing valeue if already there. 
```
def insert_if_not_present(d, key, value):
    if key not in d:
        d[key] = value
        return value
    else:
        return d[key]
        


