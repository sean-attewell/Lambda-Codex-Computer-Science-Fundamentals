def greet(name, greeting):
    print("Hello, %s, %s" % (name, greeting))


# Now, we can call our greet function and pass in the data that we want.

greet("Austen", "I hope you are having an excellent day!")
# Hello, Austen, I hope you are having an excellent day!


# If we want to define a function that returns a value to the caller, we use the return keyword.

def double(x):
    return x * 2


eight = double(4)
print(eight)
# 8


# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.


# Arbitrary Arguments, *args
# If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")  # linus


# Keyword Arguments (kwargs)
# You can also send arguments with the key = value syntax.
# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.


# This way the order of the arguments does not matter.

def my_function2(child3, child2, child1):
    print("The youngest child is " + child3)


my_function2(child1="Emil", child2="Tobias", child3="Linus")


# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:

def my_function3(**kid):
    print("His last name is " + kid["lname"])


my_function3(fname="Tobias", lname="Refsnes")


# Default Parameter Value

def my_function4(country="Norway"):
    print("I am from " + country)


my_function4("Sweden")
my_function4("India")
my_function4()  # I am from Norway
my_function4("Brazil")


# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

def my_function5(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function5(fruits)


# Recursive functions
# Python also accepts function recursion, which means a defined function can call itself.

# In this example, tri_recursion() is a function that we have defined to call itself ("recurse").
# We use the k variable as the data, which decrements (-1) every time we recurse.
# The recursion ends when the condition is not greater than 0 (i.e. when it is 0).


def tri_recursion(k):
    print("k input to function: ", k)
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print("result: ", result)
    else:
        result = 0
        print("else result: ", result)
    return result


print("\n\nRecursion Example Results")
what_is_returned = tri_recursion(6)

print('what_is_returned: ', what_is_returned)

# This decrements k from 6 to zero
# then adds 0 returned by whole function and 1 (the k before it was last decremented)
# then adds 1 returned by whole function and 2 (the k before it was last decremented)
# then adds 2 returned by whole function and 3 (the k before it was last decremented)
# ...
# finally adds 15 returned by whole function to 6 (the initial k before first decremented)
# prints and returns the last result

# So it UNWINDS in the reverse direction it wound up.
