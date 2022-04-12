
import os.path
import types
import sys

module_name = 'module1'
module_file = 'Modules_And_Packages/module2.py'
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
# ... module namespace into the mod dictionary. This will enable us to use mod.pprint() which...
# ... is a function in module.py.
exec(code, mod.__dict__)

# And now we can use the module in main.py
mod.pprint()


