# https://stackoverflow.com/questions/38125328/what-does-a-backslash-by-itself-mean-in-python

# 2.1.5. Explicit line joining
# Two or more physical lines may be joined into logical lines using backslash characters (\), as follows: when a physical line ends in a backslash that is not part of a string literal or comment, it is joined with the following forming a single logical line, deleting the backslash and the following end-of-line character. For example:

# if 1900 < year < 2100 and 1 <= month <= 12 \
#    and 1 <= day <= 31 and 0 <= hour < 24 \
#    and 0 <= minute < 60 and 0 <= second < 60:   # Looks like a valid date
#         return 1

# There is also the option to use implicit line joining, by using parentheses or brackets or curly braces; Python will not end the logical line until it finds the matching closing bracket or brace for each opening bracket or brace. This is the recommended code style, the sample you found should really be written as:

# if ((i < len(words_and_emoticons) - 1 and item.lower() == "kind" and
#         words_and_emoticons[i+1].lower() == "of") or
#         item.lower() in BOOSTER_DICT):
#     sentiments.append(valence)
#     continue
