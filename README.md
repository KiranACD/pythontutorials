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
Math is a type module with name 'math' and it is a built-in module. Likewise, fractions is also a type module with name 'fractions' and its location is shown as '/usr/lib/python3.8/fractions.py'. Fractions is from the standard library. Standard libraries are usually written in Python, so you get *.py files, but some are written in C. They are located in the lib folder as we saw above. Built-in modules are usually written in C and are built-in to the python language.

A high level view into what happends when you import math or fractions,
- First, python looks for it in the sys modules. If it finds the module, then there is no need to load it again and the existing object is returned. 
- If it does not find it in the sys modules, Python creates a new module object (`types.ModuleType`). It then loads the source code from the file.
- It, then, adds it to the `sys.modules` with name as key. For e.g., you can access the math object using `sys.modules['math']`.
- It also compiles and executes the module code.
- Then it adds the label and the reference to it in the global namespace which can be accessed through `globals()`, which is also a dict. 

Math is a type module. To check it,
```
import types
print(isinstance(math, types.ModuleType))
```
So, we can create our own module. `mod = types.ModuleType('test', 'This is a test module')`. It has been assigned a name 'test', which can be accessed by `mod.__name__`, and a description which can be accessed by `mod.__doc__`.

To give it functionality, we can give it attributes. 
```
mod.a = 10
mod.hello = lambda: 'Hello World!'

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

mod.Person = Person # mod gets a class
```
Now that we know how to create a module object, lets import a module from scratch. Lets set up a directory called Modules and have two files in there, main.py and module.py

```
Modules
|
+--main.py
+--module.py
```
`module.py` contains
```
print('Running module.py')

def pprint():

    print('Module says hello.')
```

Lets build this module up in main.py

```
import os.path
import types
import sys

# Setting a module name
module_name = 'module'
# Specifying the file name. Python usually assigns the file name as the module name.
module_file = 'module.py'
module_path = '.' # Current directory


module_rel_file_path = os.path.join(module_path, module_file)

# Get the absolute path to put into the file attribute of the module object
module_abs_file_path = os.path.abspath(module_rel_file_path)

# Read source code from file
with open(module_rel_file_path, 'r') as code_file:
    source_code = code_file.read()

# Create a module object
mod = types.ModuleType(module_name)
# Putting the absolute path into the file attribute
mod.__file__ = module_abs_file_path

# Set a reference in the sys.modules
sys.modules[module_name] = mod

# Compile the source code
code = compile(source_code, filename=module_abs_file_path, mode='exec')

# Execute the compiled code. We will put all the variables and function objects in the...
# ... module namespace into the mod dictionary. This will enable us to use mod.pprint() which..
# ... is a function in module.py.
exec(code, mod.__dict__)

# And now we can use the module in main.py
mod.pprint()
```

## Packages ##

## Named Tuples ##