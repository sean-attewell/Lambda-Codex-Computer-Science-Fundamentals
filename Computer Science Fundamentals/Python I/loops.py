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
