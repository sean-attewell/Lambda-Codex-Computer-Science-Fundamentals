# You can use two types of loops in Python, a for loop and a while loop. A for loop iterates over a given sequence (iterator expression).
# A while loop repeats as long as a boolean context evaluates to True.

# The break statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop.
# If the break statement is inside a nested loop (loop inside another loop), the break statement will only terminate the innermost loop.

# You can use the continue statement to skip the rest of the code inside a loop for the current iteration only.
# The loop does not terminate entirely but continues with the next iteration.


# Prints 0, 1, 2, 3, 4
for x in range(5):
    print(x)

    # Prints 2, 3, 4, 5, 6
for x in range(2, 7):
    print(x)

# Prints 1, 3, 5, 7
for x in range(1, 8, 2):
    print(x)


# Prints 0, 1, 2, 3, 4
count = 0
while count < 5:
    print(count)
    count += 1

# Prints 2, 3, 4, 5, 6
count = 2
while count < 7:
    print(count)
    count += 1

# Prints 1, 3, 5, 7
count = 1
while count < 8:
    print(count)
    count += 2


# You can use a break statement to exit a for loop or a while loop.

# Prints 0, 1, 2, 3, 4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break


# You can also use a continue statement to skip the current block but not exit the loop entirely.

# Prints 1, 3, 5, 7
for x in range(8):
    # if x is even, skip this block and do not print
    if x % 2 == 0:
        continue
    print(x)


# https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/

# If you only need to loop over a single list just use a for-in loop
# If you need to loop over a list and you need item indexes, use enumerate
# If you need to loop over multiple lists at the same time, use zip

# Stackoverflow example Q

# https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops

# ints = [8, 23, 45, 12, 78]
# i = 0
# for num in range(len(ints)):
#     print('item #{} = {}'.format(i, ints[i]))
#     i += 1

# colors = ["red", "green", "blue", "purple"]
# for color in colors:
#     print(color)

# The enumerate function gives us an iterable where each element is a tuple that contains the index of the item and the original item value.

# This function is meant for solving the task of:

# Accessing each item in a list (or another iterable)
# Also getting the index of each item accessed
# So whenever we need item indexes while looping, we should think of enumerate.

# Note: the start=1 option to enumerate here is optional. If we didn’t specify this, we’d start counting at 0 by default.

ints = [8, 23, 45, 12, 78]

for i, num in enumerate(ints, start=1):
    print('item #{} = {}'.format(i, num))

# https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/

# Often when we use list indexes, it’s to look something up in another list.

# colors = ["red", "green", "blue", "purple"]
# ratios = [0.2, 0.3, 0.1, 0.4]
# for i, color in enumerate(colors):
#     ratio = ratios[i]
#     print("{}% {}".format(ratio * 100, color))

# Note that we only need the index in this scenario because we’re using it to lookup elements at the same index in our second list. What we really want is to loop over two lists simultaneously: the indexes just provide a means to do that.

# We don’t actually care about the index when looping here. Our real goal is to loop over two lists at once. This need is common enough that there’s a special built-in function just for this.

# Python’s zip function allows us to loop over multiple lists at the same time:

colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
for color, ratio in zip(colors, ratios):
    print("{}% {}".format(ratio * 100, color))

# The zip function takes multiple lists and returns an iterable that provides a tuple of the corresponding elements of each list as we loop over it.

# Note that zip with different size lists will stop after the shortest list runs out of items.


# If you find yourself tempted to use range(len(my_list)) or a loop counter, think about whether you can reframe your problem to allow usage of zip or enumerate (or a combination of the two).

# In fact, if you find yourself reaching for enumerate, think about whether you actually need indexes at all. It’s quite rare to need indexes in Python.
