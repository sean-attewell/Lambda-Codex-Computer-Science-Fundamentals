# In Python, everything is an object.

a = 1
b = "hello"
c = [1, 2, 3]
print(isinstance(a, object))  # True
isinstance(b, object)  # True
isinstance(c, object)  # True

# Additionally, all objects in Python have three things:
# Identity
# Type
# Value

a = 1

# Identity
print(id(a))  # 1483629664 <-- address in memory

# Type
print(type(a))  # <class 'int'>

# Value
print(a)  # 1


# IDENTITY
# An object's identity can never change once it has been created. You can think of an object's identity as its specific address in memory.
# In the code above, a = 1 created a new object in memory whose identity is represented by the integer 1483629664.

# Python has an is operator that allows you to compare two object's identities.

a = 1
b = 2
print(a is b)  # False
b = a
print(a is b)  # True

# In the code above, we first assign 1 to the variable a. Then, we assign 2 to the variable b. These are two different objects in memory and thus have different identities.
# We verify that they are different by using the is operator, which returns False. T
# he line b = a assigns the variable b the object that the variable a is pointed to. Now, both a and b are referencing the same object in memory.

# We can use the id() function to verify that this is the case as well:

print(id(a))  # 1483629664
print(id(b))  # 1483629664

# TYPE
# The type of an object determines what are its possible values and what operations that object supports.
# The type() function will return what type an object is:

a = 'Hello'
print(type(a))  # <class 'str'>
b = 100
print(type(b))  # <class 'int'>
c = True
print(type(c))  # <class 'bool'>

# Just like identity, once created its type can never change.
# It's an object's type that determines whether an object is mutable or immutable.

# VALUE
# The value of some objects can be changed after they are created. The value of some objects cannot be changed after they are created.
# If the object's value can be changed, that object is considered to be mutable (changeable). If the object's value cannot be changed,
# that object is considered to be immutable (unchangeable).

# MUTABLE OBJECTS
# A mutable object is an object whose value can be changed after it is created. The word mutable is defined as: liable to change
# The following types of objects are mutable:

# list
# set
# dict
# byte array
# instances of user-defined classes

# Lists
my_list = ['laughter', 'happiness', 'love']
my_list[2] = 'joy'
my_list.append('excellent')
print(my_list)  # ['laughter', 'happiness', 'joy', 'excellent']

# Sets
my_set = {'laughter', 'happiness', 'love'}
my_set.add('happy')
print(my_set)  # {'love', 'happiness', 'laughter', 'happy'}
my_set.remove('happiness')
print(my_set)  # {'love', 'laughter', 'happy'}

# Dicts
my_dict = {"first_name": "Mattieu", "last_name": "Ricard"}
my_dict["location"] = "Nepal"
print(my_dict)
# {'first_name': 'Mattieu', 'last_name': 'Ricard', 'location': 'Nepal'}
del my_dict['location']
print(my_dict)
# {'first_name': 'Mattieu', 'last_name': 'Ricard'}


# Mutable objects work great when you know you will likely need to change the size of the object as you use and interact with it.
# Changing mutable objects is cheap (because you don't have to copy all existing elements to a new object).


# Aliasing with Mutable Objects
# In Python, aliasing happens whenever a variable's value is assigned to another variable because variables are just names that store references to values
# (i.e. store identities).

# we removed the element 1 from my_list_orig. Notice, just like when we added to the list, my_list_alias is also affected.
# This behavior is something you need to be aware of if you ever use aliasing with mutable objects in your code.

# Immutable Objects
# An immutable object is an object whose value cannot be changed after it is created. Immutable means not changeable.
# Anytime you try to update the value of an immutable object, a new object is created instead.
# The following types are immutable:

# Numbers (int, float, complex)
# Strings
# Bytes
# Booleans
# Tuples

# Immutable objects are useful when you want to make sure that the object you created will always maintain the same value.
# Immutable objects are more expensive to change (in terms of time and space complexity) because changing the object requires making a copy of the existing object.

# Numbers
my_int = 1
print(id(my_int))  # 1483629664
my_int = 2
print(id(my_int))  # 1483629680

# When we assign 2 to my_int, it creates a whole new object and assigns it to the variable my_int.
# This object also has int for its type, but 4513307312 for its identity (which you can see is different from the first object), and 2 for its value.

# Strings
# Let's look at how string concatenation works in Python. Remember that str objects are immutable.

my_str = 'a'
id(my_str)  # 1483629664
my_str += 'b'
id(my_str)  # 1483629680
print(my_str)  # 'ab'

# because string objects are immutable, we cannot change a string object's value after it has been created.
# To concatenate, we create a new string object and assign the value 'ab' to that object.

# This behavior in Python is vital to be aware of when working with string concatenation.
# If you have to add and remove frequently from a string, this will be inefficient if you work with string objects directly.


# Tuples
# Tuples are an immutable container of names, where each name has an unchangeable (immutable) binding to an object in memory. You cannot change the bindings of the names to the objects.

my_tuple = ('love', [1, 2, 3], True)
print(my_tuple[0])  # 'love'

# my_tuple[0] = 'laughter'
# Traceback(most recent call last):
#     File "<stdin>", line 1, in < module >
# TypeError: 'tuple' object does not support item assignment


# Just like a list, tuples can contain elements of any type. Above, we've included a string, a list, and a boolean as our tuple elements.
# We are proving the tuple object's immutability by showing the error that occurs when trying to assign a new item to a position in the tuple.

# One thing that often causes confusion surrounding the immutability of tuples in Python is demonstrated by the following behavior:

# my_tuple[1] = [4,5,6]
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment

print(id(my_tuple))  # 31328936
print(id(my_tuple[1]))  # 19380184

my_tuple[1][0] = 4
my_tuple[1][1] = 5
my_tuple[1][2] = 6
print(my_tuple[1])  # [4, 5, 6]
print(my_tuple)  # ('love', [4, 5, 6], True)

print(id(my_tuple))  # 31328936
print(id(my_tuple[1]))  # 19380184

# Notice that we cannot create a new list object and bind it to the name at position 1 of our tuple. This is demonstrated when my_tuple[1] = [4,5,6] raises a TypeError.
# However, we can assign new objects to the list that is at position 1 of our tuple? Why is that? Well, what do we know about lists in Python? Lists are mutable objects.
# So, we can modify a list without creating a new object.
# So, when we are modifying the list directly (instead of assigning a new object), it doesn't affect our tuple's immutability.
# Notice that the identity of the list at my_tuple[1] doesn't change after replacing its three elements with 4, 5, and 6.


# Passing Objects to Functions

# Mutable and immutable objects are not treated the same when they are passed as arguments to functions. When mutable objects are passed into a function, they are passed by reference. So, suppose you change the mutable object that was passed in as an argument. In that case, you are changing the original object as well.

# Mutable Objects as Arguments
my_list = [1, 2, 3]


def append_num_to_list(lst, num):
    lst.append(num)


append_num_to_list(my_list, 4)
print(my_list)

# Notice that when append_num_to_list is called and my_list is passed in as an argument.
# When my_list is bound to lst in that stack frame, lst points to the original my_list in memory.
# The function call did not create a copy of my_list.
# This behavior is because lists are mutable objects in Python.


# Immutable Objects as Arguments
# Next, let's see how Python behaves when we pass an immutable object as an argument to a function:

my_string = "I am an immutable object."


def concatenate_string_to_string(orig_string, string_to_add):
    return orig_string + string_to_add


returned_from_funct = concatenate_string_to_string(my_string, " I hope!")

print("returned_from_funct: ", returned_from_funct)
# 'I am an immutable object. I hope!'

print('my_string: ', my_string)
# 'I am an immutable object.'

# Notice when an immutable object is passed into a function, the object is copied and bound to the ***parameter name***.
# In the example above, when my_string is passed into concatenate_string_to_string, my_string is copied to a new object bound to the name orig_string.
