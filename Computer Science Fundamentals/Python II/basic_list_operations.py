# Lists are similar to arrays. They can store any type of variable and as many variables as you want. You can iterate over lists effortlessly.

my_list = []  # empty list literal
my_list.append(1)  # add 1 to end of list
my_list.append(2)  # add 2 to end of list
my_list.append(3)  # add 3 to end of list
print(my_list[0])  # prints 1
print(my_list[1])  # prints 2
print(my_list[2])  # prints 3

# iterate over the list with for statement to print each item in my_list
for item in my_list:
    print(item)

# In Python, if you try to access a list index that does not exist, you get an IndexError: list index out of range message.
# >>> my_list = [1,2,3]
# >>> print(my_list[10])
# IndexError: list index out of range
