# the argument for the print function can be an expression. Once the expression is resolved to a string object, the print function can output it to the screen.

# Any object passed as an argument into print will get converted into a string type before outputted to the screen.

# Multiple items can be separated by commas. print will use " " as the default separator value.

print("Lambda School", 2020, True, sep="!!!")
print("Lambda School", 2020, True, sep="\t")  # tab
print("Lambda School", 2020, True, sep="\n")
print("Lambda School", 2020, True, sep="")

# The default end value when calling print is the newline character \n.
# Being able to print a value to the screen but allow the user to stay on the same line is useful and necessary in some cases.
# Below works in python repl
print("Are you a Lambda School student?", end=" (Y or N)")
