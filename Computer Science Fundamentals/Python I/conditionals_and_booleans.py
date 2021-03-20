# Python uses boolean values to evaluate conditions. An expression in any Boolean context will evaluate to a Boolean value and then control your program's flow.
# Python's boolean values are written as True and False (make sure you capitalize the first character).

x = 10
print(x == 10)  # True
print(x == 5)  # False
print(x < 15)  # True
print(x > 15)  # False
print(x <= 10)  # True
print(x >= 10)  # True
print(x != 20)  # True

name = "Elon"
age = 49
if name == "Elon" and age == 49:
    print("You are a 49 year old person named Elon.")

if name == "Elon" or name == "Bill":
    print("Your name is either Elon or Bill.")


# Any time you have an iterable object (like a list), you can check if a specific item exists inside that iterable by using the in operator.

years = [2018, 2019, 2020, 2021]
year = 2020

if year in years:
    print("%s is in the years collection" % year)

# 2020 is in the years collection

# We can use the if, elif, and the else keywords to define a series of code blocks that will execute conditionally.

first_statement = False
second_statement = True

if first_statement:
    print("The first statement is true")
elif second_statement:
    print("The second statement is true")
else:
    print("Neither the first statement nor the second statement are true")
# At most, one of the code blocks specified will be executed.
# If an else clause isn’t included, and all the conditions are false, then none of the blocks will be executed


# Any object that is considered "empty" evaluates to False. For example, "", [], and 0 all evaluate to False.

# If we want to determine if two objects are actually the same instance in memory, we use the is operator instead of the value comparison operator ==.

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True because a and b have the same value
print(a is b)  # False because a and b reference two different list objects

x = [1, 2, 3]
y = x

print(x == y)  # True because x and y have the same value
print(x is y)  # True because x and y reference the same list object


# There is also the not operator, which inverts the boolean that follows it:

print(not False)    # True
print(not (1 == 1))  # False because 1 == 1 is True and then is inverted by not


# https://realpython.com/python-conditional-statements/


# if 'a' in 'bar':
#     print('foo')
# elif 1/0:
#     print("This won't happen")
# elif var:
#     print("This won't either")

# prints foo
# The second expression contains a division by zero, and the third references an undefined variable var.
# Either would raise an error, but neither is evaluated because the first condition specified is true.


# it is permissible to write an entire if statement on one line. The following is functionally equivalent to the example above:

# if <expr>: <statement>

# if <expr>: <statement_1>; <statement_2>; ...; <statement_n>
# If <expr> is true, execute all of <statement_1> ... <statement_n>. Otherwise, don’t execute any of them.

# Python takes the latter interpretation. The semicolon separating the <statements> has higher precedence
# than the colon following <expr>—in computer lingo, the semicolon is said to bind more tightly than the colon.
# Thus, the <statements> are treated as a suite, and either all of them are executed, or none of them are:

# if 'f' in 'foo': print('1'); print('2'); print('3')
# 1
# 2
# 3
# if 'z' in 'foo': print('1'); print('2'); print('3')
# ...

# ^ my linter or whatever doesn't like this and turns it into a multi liner

# Multiple statements may be specified on the same line as an elif or else clause as well:

# >>> x = 2
# >>> if x == 1: print('foo'); print('bar'); print('baz')
# ... elif x == 2: print('qux'); print('quux')
# ... else: print('corge'); print('grault')
# ...
# qux

# While all of this works, and the interpreter allows it, it is generally discouraged on the grounds that it leads to poor readability,
# particularly for complex if statements. PEP 8 specifically recommends against it.


# Conditional Expressions (Python’s Ternary Operator)

# <expr1> if <conditional_expr> else <expr2>

# In the above example, <conditional_expr> is evaluated first. If it is true, the expression evaluates to <expr1>. If it is false, the expression evaluates to <expr2>.
# Notice the non-obvious order: the middle expression is evaluated first, and based on that result, one of the expressions on the ends is returned

raining = False
print("Let's go to the", 'beach' if not raining else 'library')
# Let's go to the beach


# Python’s conditional expression is similar to the <conditional_expr> ? <expr1> : <expr2> syntax used by many other languages—C, Perl and Java to name a few.
# In fact, the ?: operator is commonly called the ternary operator in those languages, which is probably the reason
# Python’s conditional expression is sometimes referred to as the Python ternary operator.

# You can see in PEP 308 that the <conditional_expr> ? <expr1> : <expr2> syntax was considered for Python but ultimately rejected in favor of the syntax shown above

# higher_number = a if a > b else b

# Remember that the conditional expression behaves like an expression syntactically. It can be used as part of a longer expression.
# The conditional expression has lower precedence than virtually all the other operators, so parentheses are needed to group it by itself.

# >>> x = y = 40

# >>> z = 1 + x if x > y else y + 2
# >>> z
# 42

# If you want the conditional expression to be evaluated first, you need to surround it with grouping parentheses

# >>> z = 1 + (x if x > y else y) + 2
# >>> z
# 43


# Conditional expressions also use short-circuit evaluation like compound logical expressions. Portions of a conditional expression are not evaluated if they don’t need to be.

# In the expression <expr1> if <conditional_expr> else <expr2>:

# If <conditional_expr> is true, <expr1> is returned and <expr2> is not evaluated.
# If <conditional_expr> is false, <expr2> is returned and <expr1> is not evaluated.


# Conditional expressions can also be chained together, as a sort of alternative if/elif/else structure, as shown here:
x = 4
s = ('foo' if (x == 1) else
     'bar' if (x == 2) else
     'baz' if (x == 3) else
     'qux' if (x == 4) else
     'quux'
     )
print(s)

# The Python pass Statement

# Occasionally, you may find that you want to write what is called a code stub: a placeholder for where you will eventually put a block of code that you haven’t implemented yet.

# In languages where token delimiters are used to define blocks, like the curly braces in Perl and C, empty delimiters can be used to define a code stub. For example, the following is legitimate Perl or C code:

# # This is not Python
# if (x)
# {
# }
# Here, the empty curly braces define an empty block. Perl or C will evaluate the expression x, and then even if it is true, quietly do nothing.

# Because Python uses indentation instead of delimiters, it is not possible to specify an empty block.
# If you introduce an if statement with if <expr>:, something has to come after it, either on the same line or indented on the following line.
# Otherwise you get this

# C:\Users\john\Documents\Python\doc>python foo.py
#   File "foo.py", line 3
#     print('foo')
#         ^
# IndentationError: expected an indented block

# The Python pass statement solves this problem. It doesn’t change program behavior at all.
# It is used as a placeholder to keep the interpreter happy in any situation where a statement is syntactically required, but you don’t really want to do anything:

if True:
    pass
