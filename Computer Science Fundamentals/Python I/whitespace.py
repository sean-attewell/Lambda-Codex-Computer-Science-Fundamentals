# >>> import string
# >>> string.whitespace
# ' \t\n\r\x0b\x0c'
# >>>
# Notice the characters are " " (space), \t (tab), \n (newline), \r (return), \x0b (unicode line tabulation), and \x0c (unicode form feed).
# You've seen the different types of whitespace characters that can appear, but you mainly need to concern yourself with " ", \t, and \n.


# Whitespace is used to denote the end of a logical line of code. In Python, a logical line of code's end (a statement or a definition) is marked by a \n.
# >>> first = "Lambda"
# >>> second = "School"
# >>> first + second
# 'LambdaSchool'
# >>> first \
# ... + \
# ... second
# 'LambdaSchool'
# >>>
# Whitespace is used to denote the end of a logical line of code. In Python, a logical line of code's end (a statement or a definition) is marked by a \n.


# Whitespace (indentation) can denote code blocks.
# Python gives meaning to the amount of whitespace (indentation level) that comes before a logical line of code.

if True:
    print('4 spaces')

# The mismatch of tab usage and spaces raises an error when Python tries to interpret the code.

# There is not a single situation in any country, in any programming language, or at any skill level, in which is it acceptable to not indent your code the way Python requires it. Therefore, it is technically redundant to have a language that is not whitespace-sensitive. Any language that is not whitespace-sensitive requires (by universal convention) that programmers communicate the scoping of the code in two distinct manners for every single line of code: braces (or begin/end) and indentation. You are required to make sure that these two things match up, and if you don’t, then you have a program that doesn’t work the way it looks like it works, and the compiler isn’t going to tell you.

# When you really analyse it, Python’s whitespace sensitivity is actually the only logical choice for a programming language, because you only communicate your intent one way, and that intent is read the same way by humans and computers. The only reason to use a whitespace-insensitive language is that that’s the way we’ve always done things, and that’s never a good reason.
