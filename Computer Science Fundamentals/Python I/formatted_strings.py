# To format a string in Python, you use the % operator to format a set of stored variables in a tuple.
# You also include argument specifiers in your string with special symbols like %s and %d.

name = "Austen"
year = 2020
print("Hey %s! It's the year %d." % (name, year))
# Hey Austen! It's the year 2020.

# Any object that is not a string can also be formatted using the s% operator. The string which returns from the object's repr method will be used in the formatted string.

my_list = [1, 2, 3]
print("my_list: %s" % my_list)
# my_list: [1, 2, 3]

# %s - String (or any object with a string representation)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the dot's right.
# %x/%X - Integers in hexadecimal (lowercase/uppercase)

my_hex = 0x3523fe2e
print("my_int as hex: %X" % my_hex)

# changing the above to %d or %f will convert the hex.

product_name = "bananas"
price = 1.23
product_id = 123456
print("%s (id: %d) are currently $%.2f." % (product_name, product_id, price))
# bananas (id: 123456) are currently $1.23.

# can also convert to hex
print("%s (id: %x) are currently $%.2f." % (product_name, product_id, price))


# https://realpython.com/python-string-formatting/

errno = 50159747054
name = 'Bob'

# This makes your format strings easier to maintain and easier to modify in the future. You don’t have to worry about making sure the order you’re passing in the values matches up with the order in which the values are referenced in the format string. Of course, the downside is that this technique requires a little more typing.

# Pass in a mapping:
mapped_string = 'Hey %(name)s, there is a 0x %(errno)x error!' % {
    "name": name, "errno": errno}

print(mapped_string)


# “New Style” String Formatting (str.format)
# Python 3 introduced a new way to do string formatting that was also later back-ported to Python 2.7. This “new style” string formatting gets rid of
# the %-operator special syntax and makes the syntax for string formatting more regular. Formatting is now handled by calling .format() on a string object.

print('Hello, {}'.format(name))
