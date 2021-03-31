# A data structure is a structure that is designed for holding information in a particular way. A static array is a data structure that is designing for storing information sequentially (in order). For example, if you were to store the English alphabet in a static array, you would expect the "B" character to right next to both the "A" character and the "C" character. Additionally, every position within the static array is labeled with an index. So, if you wanted to access the first item in the static array, you would expect that item to have an index of 0. The second item would have an index of 1. The third item would have an index of 2. This pattern continues for the entire capacity of the static array.

# Python does not have a static array data type. However, lists are built on dynamic arrays. As you will see, dynamic arrays rely on an underlying static array to work.

# Time and Space Complexity

# Lookup
# To look up an item by index in an array is constant time (O(1). If you have the specific index of an object in an array, the computations to find that item in memory are all constant time as well.

# Append
# Adding an item to an array is constant time (O(1)). We always have a reference point to the last thing in a static array, so we can insert an item after the current end.

# Insert
# Unless you are inserting an item at the end of the list, items must be shifted over to make room for the new information you add to the static array. It's like if you had a chain of people stretched out, holding hands, in a line. The first person in the line is butted right up against a wall, and there is no room on one side of him. If someone wanted to join the end of the line, the people already in the line wouldn't have to do anything (O(1)). However, if you wanted to join the beginning of the line, every single person would have to move over (away from the wall) (O(n)) so that you would have room to join. If you wanted to join the line somewhere in the middle, only the people to your one side would have to shift to make room for you. In the computer, this shifting is moving information from one address in memory to another. Each move takes time.

# Delete
# Just like insertions, deletions are only efficient (O(1)) when they are done at the end of the static array. If something is deleted from any other position in the array, the items have to be moved over, so there isn't any empty space left. 

# Remember, static arrays can be a good data structure because retrieving information from a specific index is fast. It is fast because we can ensure that information is consistently stored in sequence right next to each other. That way, we can always be confident that whatever information is at index 5 is the sixth item in the array. If we left empty spaces in the middle of our static array, we would no longer ensure that this was true.

# Strengths
# Static arrays are great to use when you need a data structure to retrieve information from a specific index efficiently. This is because, as we explained earlier, accessing any specific index in a static array involves a simple mathematical computation (starting index + (size of each item * index)). This computation is done in O(1) time and is not affected by the static array size at all. 
# If you need a data structure where you are likely only to append items (add them to the end of the list), a static array also works great. When you add a new item to the end of the list, nothing has to be shifted over or moved in memory, so that operation is very efficient (O(1)).

# Weaknesses
# There are situations where static arrays are not the best data structure to use for storing your information. What about if you don't know how much information you need to store? Or if the amount of information you need to store is likely to fluctuate or change frequently. In this case, a static array is not good. The reason is that when you create a static array, you have to know and declare the size of that array. That way, your computer can separate off a chunk of memory that is the exact right size for storing that static array. If you run out of room in the static array, you can't simply make it bigger; you have to create a brand new, bigger static array. You have to copy each item from the first static array into the newer, bigger one.

# Another reason that static arrays are not always the best choice to use for storing information is that they are inefficient unless you are performing operations at the end of the static array. They are inefficient because if you want to insert or delete something at the beginning (or the middle of the list), all the items to the right of that index must be moved over. If you delete something, everything has to be shifted over, so there isn't an empty index in the middle of your data. If you insert something, all the items have to shift over to make room for the new item before inserting it.


# What about array slicing?
# You often encounter a scenario where you want to use a subset of items from an existing array. Array slicing is when you take a subset from an existing array and allocate a new array with just the items from the slice.

# In Python, the syntax looks like this:

# my_list[start_index:end_index]
# The default start index is 0, and if you leave off the end_index, the slice will capture through the end of the list.

my_list = [0,1,2,3,4,5,6,7,8]

print(my_list[:])  # This would be all of the items in my_list [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(my_list[:5]) # This would be the items from index 0 to 4 [0, 1, 2, 3, 4]
print(my_list[5:]) # This would be the items from index 5 to the end of the list [5, 6, 7, 8]

# You might be wondering, what is the time and space complexity of slicing an array? To understand the complexity, you need to know what is happening behind the scenes when you take a slice of an array. 

# First, you are actually allocating a new list. 
# Second, you copy all of the items in your slice from the original array into the newly allocated list. 
# This means that you have an O(n) time cost (for the copying) and an O(n) space cost for the newly allocated list.

# You must keep these facts in mind and account for them when using a slice in your code. It's not a free operation.


# https://www.hackerearth.com/practice/data-structures/arrays/1-d/tutorial/

# Array declaration

# Declaring an array is language-specific.
# For example, in C/C++, to declare an array, you must specify, the following:

# Size of the array: This defines the number of elements that can be stored in the array.

# Type of array: This defines the type of each element i.e. number, character, or any other data type.
# e.g. int arr[5] = {4, 12, 7, 15, 9};


# This is a static array and the other kind is dynamic array, where type is just enough for declaration. 
# In dynamic arrays, size increases as more elements are added to the array.

# An array can be initialized after declaration by assigning values to each index of the array as follows

# type arr[size]
#  arr[index] = 12
# C++ example:

# int arr[5];
# arr[0] = 4;
# arr[1] = 12;

# https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/

# Slicing can not only be used for lists, tuples or arrays, but custom data structures as well, with the slice object, which will be used later on in this article.

# There is also an optional second clause that we can add that allows us to set how the list's index will increment between the indexes that we've set.
# e.g. a[1:4:2]


# Python Slicing (Lists, Tuples and Arrays) in Reverse

print(my_list[::-1])

# Lists have a default bit of functionality when slicing. If there is no value before the first colon, it means to start at the beginning index of the list. If there isn't a value after the first colon, it means to go all the way to the end of the list. This saves us time so that we don't have to manually specify len(a) as the ending index.

# Okay. And that -1 I snuck in at the end? It means to increment the index every time by -1, meaning it will traverse the list by going backwards. If you wanted the even indexes going backwards, you could skip every second element and set the iteration to -2. Simple


# Everything above also works for tuples. The exact same syntax and the exact same way of doing things

t = (2, 5, 7, 9, 10, 11, 12)
print(t[2:4])


# Using Python Slice Objects
# There is another form of syntax you can use that may be easier to understand. 
# There are objects in Python called slice objects and the can be used in place of the colon syntax above.

a = [1, 2, 3, 4, 5]
sliceObj = slice(1, 3)
print(a[sliceObj]) # [2, 3]

# The slice object initialization takes in 3 arguments with the last one being the optional index increment. The general method format is: slice(start, stop, increment), and it is analogous to start:stop:increment when applied to a list or tuple.

