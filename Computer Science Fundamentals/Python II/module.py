# Any Python file that ends with the .py extension is considered a module. The name of the module is the name of the file.
# To import from other modules, we can use the import command.

# import math

# print(math.factorial(5)) # 120

# So, by importing the built-in math module, we have access to all of the functions and data defined in that module.
# We access those functions and data using dot notation, just like we do with objects.

# If you only need a specific function from a module, you can import that specific function like so:

# from math import factorial

# print(factorial(5))  # 120

# You can also import all the names from a module with this syntax to avoid using dot notation throughout your file.

# from math import *

# print(factorial(5))  # 120
# print(pow(2, 3))  # 8.0

# You can also bind the module to a name of your choice by using as.

import math as alias

print(alias.factorial(5))  # 120

# To find out which names a module defines when imported, you can use the dir() method. This method returns an alphabetically sorted list of strings for all of the names defined in the module.

print(dir(alias))
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
