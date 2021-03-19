# The len() method prints out the number of characters in the string.

my_string = "Hello, world!"
print(len(my_string))  # 12

# The index() method prints out the index of the substring argument's first occurrence.

my_string = "Hello, world!"
print(my_string.index("o"))   # 4
print(my_string.index(", w"))  # 5

# The count() method returns the number of occurrences of the substring argument.

my_string = "Hello, world!"
print(my_string.count("o"))  # 2
print(my_string.count("ll"))  # 1

# To slice a string, you can use this syntax: [start:stop:step]. To reverse the string's order, you can set the step value to be -1.

my_string = "Hello, world!"
print(my_string[3:7])   # lo,
print(my_string[3:7:2])  # l,
print(my_string[::-1])  # !dlrow ,olleH

# You can convert a string to uppercase or lowercase with the upper() and lower() methods.

my_string = "Hello, world!"
print(my_string.upper())  # HELLO, WORLD!
print(my_string.lower())  # hello, world!

# You can determine if a string starts with or ends with a specific sequence with the startswith() and endswith() methods.

my_string = "Hello, world!"
print(my_string.startswith("Hello"))  # True
print(my_string.endswith("globe!"))  # False

# The split() method allows you to split up a string into a list. The default separator is any whitespace. You can also specify the separator value with an argument if you want.

my_string = "Hello, world!"
print(my_string.split())    # ['Hello,', 'world!']
print(my_string.split(","))  # ['Hello', ' world!']
print(my_string.split("l"))
# ['He', '', 'o, wor', 'd!'] <-- empty string between the two 'l's
