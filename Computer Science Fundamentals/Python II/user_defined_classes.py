# A Python object encapsulates variables (data) and functions (behavior) into a single entity.
# An object instance gets its variables and functions from the class that was used to instantiate it.
# Think of a class as a blueprint or template that you can use to create objects.


class MyFirstClass:
    variable = "data"

    def function(self):
        return "Printing from a MyFirstClass object."


a_class_object = MyFirstClass()

print(a_class_object.variable)  # data
print(a_class_object.function())  # Printing from a MyFirstClass object.

# In general, a dot expression is written as <expression>.<name>. The <expression> must evaluate to an object, and the name must be an attribute on that object.

# The whole point of defining a class is so that you can use the same template to create multiple objects.
# All of the objects you make by instantiating the class will have the attributes that were a part of the class definition.

another_class_object = MyFirstClass()

print(another_class_object.variable)  # data
print(another_class_object.function())  # Printing from a MyFirstClass object.


# https://www.hackerearth.com/practice/python/object-oriented-programming/classes-and-objects-i/tutorial/

# You can also provide the values for the attributes at runtime. This is done by defining the attributes inside the init method
class Snake:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"This is an instance of the Snake class called {self.name}"

    def change_name(self, new_name):
        self.name = new_name

# Now you can directly define separate attribute values for separate objects. For example,


# two variables are instantiated
python = Snake("python")
anaconda = Snake("anaconda")

# print the names of the two variables
print(python.name)  # python
print(anaconda.name)  # anaconda

anaconda.change_name("Adder")
print(anaconda.name)  # Adder

print(anaconda)  # This is an instance of the Snake class called Adder
