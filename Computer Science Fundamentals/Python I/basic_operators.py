# There are a few basic operators that you should be familiar with as you start writing Python code

# Multiplies, then divides, then adds
my_number = 2 + 2 * 8 / 5.0
print(my_number)  # 5.2

# There is also an operator called the modulo operator (%). This operator returns the remainder of integer division.

my_remainder = 9 % 4
print(my_remainder)  # 1

# Floor Division is like the inverse of this. Dividing with two // means you isntead don't get any remainder

no_remainder = 9 // 4
print(no_remainder)  # 2

# Floor Division - The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity)

# 9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0

# So -11/3 = -3.666 so it rounds it toward negative infinity and you get -4

# You can use two multiplication operators to make the exponentiation operator (**).

two_squared = 2 ** 2
print(two_squared)    # 4
two_cubed = 2 ** 3
print(two_cubed)      # 8

# You can use the addition operator to concatenate strings and lists:

string_one = "Hello,"
string_two = " World!"
combined = string_one + string_two
print(combined)  # Hello, World!

lst_one = [1, 2, 3]
lst_two = [4, 5, 6]
big_lst = lst_one + lst_two
print(big_lst)  # [1, 2, 3, 4, 5, 6]


# You can also use the multiplication operator to create a new list or string that repeats the original sequence:

my_string = "Bueller"
repeated = my_string * 3
print(repeated)  # BuellerBuellerBueller

my_list = [1, 2, 3]
repeated_list = my_list * 3
print(repeated_list)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]


a = object()
b = object()

# print(a)  # <object object at 0x00874550>
# print(b)  # <object object at 0x00874558>

a_list = [a] * 5
b_list = [b] * 5

# print(a_list)  # [<object object at 0x00FF4550>, <object object at 0x00FF4550>, <object object at 0x00FF4550>, <object object at 0x00FF4550>, <object object at 0x00FF4550>]
# print(b_list)

combined = a_list + b_list

print(combined)  # [<object object at 0x007F4550>, <object object at 0x007F4550>, <object object at 0x007F4550>, <object object at 0x007F4550>, <object object at 0x007F4550>, <object object at 0x007F4558>, <object object at 0x007F4558>, <object object at 0x007F4558>, <object object at 0x007F4558>, <object object at 0x007F4558>]

print(len(combined))  # 10
