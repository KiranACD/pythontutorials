# Collection of my notes on Python #

## Basics ##

## Python types ##

## Python Memory Management ##

## Python Optimizations ##

## Functions ##

## Scopes ##

## Namespace ##

## Modules ##

Module is an instance of the module type, like how class is an instance of class type or funcions are instances of the function type.

Lets say we import the math module or the fractions module. What happens when we import these modules?
Lets print out their references...
```
<module 'math' (built-in)>
<module 'fractions' from '/usr/lib/python3.8/fractions.py'>
```
Math is a type module with name 'math' and it is a built-in module. Likewise, fractions is also a type module with name 'fractions' and its location is shown as '/usr/lib/python3.8/fractions.py'. Fractions is from the standard library. Standard libraries are very written in Python, so you get *.py files, sometimes written in C, whereas the built-in modules are written in C and are built-in to the python language. 

When you import math or fractions,
- First, python looks for it in the sys modules. If it finds the module, then there is no need to load it again.  
- If it does not find it in the sys modules, it loads the module into the cache and it creates a reference to it in `sys.modules`. You can access the math object using `sys.modules['math']
- Then it adds the label and the reference to it in the global namespace which can be accessed through `globals()`, which is also a dict. 

## Packages ##

## Named Tuples ##