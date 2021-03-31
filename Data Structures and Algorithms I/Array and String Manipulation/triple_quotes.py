# we can use triple quotes (i.e., triplet of single quotes or triplet double quotes) to represent the strings containing both single and double quotes to eliminate the need of escaping any.

print('''She said, "Thank you! It's mine."''') # She said, "Thank you! It's mine."

# It should be noted that when a string starts or ends with a single or double quote and we want to use the triple quotes for the string, we need to use the ones that differ from the starting or ending one.

# Another use case of the triple quotes is to represent a multi-line string rather than using \n

print("""First line
second line
third line
        fourth line.""")


# In addition, a useful application of the triple-quote enclosed strings is to specify some comments in a multi-line string, for example, as part of a function definition like below.

def multiple_line_comment(a, b):
    '''
    a is a string # other additional description
    b is a list of integers # other additional description
    '''
    pass


print(multiple_line_comment.__doc__)

# a is a string # other additional description
# b is a list of integers # other additional description

# We can clearly tell what are the comments for the function.
# Note that the description is indented when printed as it is indented in the function.


