# https://www.freecodecamp.org/news/if-name-main-python-example/

# Python files are called modules and they are identified by the .py file extension. A module can define functions, classes, and variables.

# So when the interpreter runs a module, the __name__ variable will be set as __main__ if the module that is being run is the main program.
# But if the code is importing the module from another module, then the __name__  variable will be set to that module’s name.

# There is a really nice use case for the __name__ variable, whether you want a file that can be run as the main program or imported by other modules.
# We can use an if __name__ == "__main__" block to allow or prevent parts of code from being run when the modules are imported.


# When the Python interpreter reads a file, the __name__ variable is set as __main__ if the module being run, or as the module's name if it is imported.
#  Reading the file executes all top level code, but not functions and classes (since they will only get imported).

from file_two import function_three

print("File one __name__ is set to: {}" .format(__name__))

# If you run this file you get:

# File two __name__ is set to: file_two
# File one __name__ is set to: __main__

# but running file_two directly gives you:
# File two __name__ is set to: __main__

# The variable __name__ for the file/module that is run will be always __main__. But the __name__ variable for all other modules that are being imported will be set to their module's name.


def function_one():
    print("Function one is executed")


def function_two():
    print("Function two is executed")


# The usual way of using __name__ and __main__ looks like this:

# if __name__ == "__main__":
#     ...

if __name__ == "__main__":
    print("File one executed when ran directly")
    function_two()
    function_three()
else:
    print("File one executed when imported")

# When running file_one you will see that the program recognized which of these two modules is __main__ and executed the code according to our first if else statements.
# File two __name__ is set to: file_two
# File two executed when imported
# File one __name__ is set to: __main__
# File one executed when ran directly

# Running file 2
# File two __name__ is set to: __main__
# File two executed when ran directly


# When modules like this are being imported and run, their functions will be imported, and top level code executed.
# File two __name__ is set to: file_two
# File two executed when imported
# File one __name__ is set to: __main__
# File one executed when ran directly
# Function two is executed

# Also, you can run functions from imported files
# File two __name__ is set to: file_two
# File two executed when imported
# File one __name__ is set to: __main__
# File one executed when ran directly
# Function two is executed
# Function three is executed
