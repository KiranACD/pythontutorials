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

'john' --> John
'eric' --> Eric
'michael' --> Michael
'graham' --> Graham

in a dictionary and we want to retreive these items by using a key (string as we see above).

We will define a function that will return an integer value for all these strings ('john', 'eric' etc). There are going to be a few condtions:

- integer value must be unique for each of these strings
- is between 0 and 6.
- always returns the same integer for the same string

Say our function produces the followig results:

h('john') --> 2, 
h('eric') --> 4, 
h('michael') --> 0, 
h('graham') --> 5

So we can now store the objects at the indices returned by the hash function when applied to the strings. John will go to index 2, Eric will go to position 4, Michael will go to 0, Graham will go to position 5.



