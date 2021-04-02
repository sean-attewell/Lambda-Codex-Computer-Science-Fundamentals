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

# Okay. And that -1 I snuck in at the end? It means to increment the index every time by -1, meaning it will traverse the list by going backwards. If you wanted the even indexes going backwards, you could skip every second element and set the iteration to -2. Simple.


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


# In-Place
# An in-place function modifies or destroys the state of the input data when it is run. For instance, if you write a function that squares every integer in an input list, an in-place version of this function would change the data in the list that was passed in. It would not create a new list and return the new list. In-place functions are more space-efficient because they don't create new variables directly tied to the input size. However, to get that space-efficiency, you have to risk that the function's user may end up changing state to the input accidentally.

# Imagine a scenario where you have an antique map that you are using to navigate on a hike. You end up needing directions, and when you come across another hiker, you ask them for help. The person helping you has two options. They can take your antique map, use a pen, and mark it up with their notations that will help you navigate. However, you most likely didn't want those annotations to be on your map forever. The other option would be to find another piece of paper and have the person helping you write out their annotations on that. This way, your original antique map doesn't have to be modified. However, now you have two maps that you have to carry around on your hike.

# Out-of-Place
# In contrast to in-place functions, out-of-place functions don't modify or destroy the input state when they are run. Any changes done to the input are done to a copy of the input, not the original that was passed in. This is why they are less space-efficient. If you have a list of 1,000,000 items that you want to square, you first have to make a copy of that list. Now, you have two lists of 1,000,000 items. However, you avoid any side-effects that might be unintended.

# Pass By Reference or Value
# In Python, some function arguments are passed in by their actual value, and some are passed in as a reference to the object in memory. Primitive values like integers, floats, and strings are passed in by their actual value. So, if you call a function and pass in the integer 2 when you reference that value by the named parameter of the function, you can't change 2 in memory. However, non-primitive objects like lists or dictionaries are passed in as references to that object in memory. So, if you call a function and pass in the dictionary {"name": "Matt"} when you reference that dictionary using the named parameter, you are changing the original object that was passed in. For objects that are passed in by reference, they must be copied to a new variable before they are modified if you want to avoid side effects.

# When should I use an in-place function or algorithm?
# It would be best if you always defaulted to using an out-of-place function. This is a safer default to avoid unintended side-effects in your program. However, there are scenarios that you might encounter where you need to be extremely space-efficient. In that case, you might have to use an in-place function to work within the particular space-constraints you've been given.

def append_exclamations(str_list):
    for idx, _ in enumerate(str_list):
        str_list[idx] += "!"

# Now, since this is an in-place function, watch what happens when we use it:

my_list = ["Matt", "Beej", "Sean"]
append_exclamations(my_list)
print(my_list) # ['Matt!', 'Beej!', 'Sean!']

# my_list was modified when I called the function, and the function only returned the default return value of None.

# Let's now write a similar function, but this time we will do it out-of-place:

def append_exclamations2(str_list):
    # Create a new empty list that has the same length as the input list
    loud_list = [None] * len(str_list)
    for idx, item in enumerate(str_list):
        # insert the modified string into the new list
        loud_list[idx] = item + "!"
    # Since we didn't modify the input list, we need to return the new list to
    # the function caller
    return loud_list

# Look what happens when we use this function:

my_list = ["Matt", "Beej", "Sean"]
my_new_louder_list = append_exclamations2(my_list)
print(my_list) # ['Matt', 'Beej', 'Sean']
print(my_new_louder_list) # ['Matt!', 'Beej!', 'Sean!']

# Notice how we had to store the returned list in a new variable. Also, notice that it didn't modify the list that we passed in when we called the function.

# https://www.techiedelight.com/in-place-vs-out-of-place-algorithms/

# In-place algorithms:

# An in-place algorithm transforms the input without using any extra memory. As the algorithm executes, the input is usually overwritten by the output, and no additional space is needed for this operation.

# An in-place algorithm may require a small amount of extra memory for its operation. However, the amount of memory required must not be dependent on the input size and should be constant.

# Several sorting algorithms rearrange the input into sorted order in-place, such as insertion sort, selection sort, quick sort, bubble sort, heap sort, etc. All these algorithms require a constant amount of extra space for rearranging the elements in the input array.

# Usually, an algorithm is categorized as an in-place or an out-of-place algorithm based on the explicit storage allocated by the algorithm. However, calling a recursive algorithm as in-place is highly debatable since extra space is being used by the call stack. Although this space required by the call stack technically takes the recursive algorithms out of the in-place algorithms category, the algorithms requiring only O(log(n)) additional space is considered to be in-place.

# In-place algorithms are usually used in an embedded system that runs in limited memory. They reduce the space requirements to a great extent, but the algorithm time complexity increases in some cases.

# Out-of-place algorithms:

# An algorithm that is not in-place is called a not-in-place or out-of-place algorithm. Unlike an in-place algorithm, the extra space used by an out-of-place algorithm depends on the input size.

# The standard merge sort algorithm is an example of out-of-place algorithm as it requires O(n) extra space for merging. The merging can be done in-place, but it increases the time complexity of the sorting routine


# Dynamic arrays

# Remember how we said you had to know how much information you were going to store when you created a static array? Well, with a dynamic array, you don't have to know. You don't have to declare a size when you instantiate a dynamic array. That makes it better in scenarios where the amount of information you need to store is unknown or is likely to fluctuate.

# Time and Space Complexity

# Lookup
# To look up an item by index in an array is constant time (O(1). If you have the specific index of an item in an array, the computations to find that item in memory are all constant time as well.

# Append
# Adding an item to an array is constant time (O(1)) in the average case. However, in the worst case, the cost is O(n) (if you exceed the current size of the array, it needs to make a new bigger array and copy everything over).

# Insert
# In the worst case, inserting an item is linear time (O(n)). When you insert into an array, all the items — starting at the index we are inserting into — have to be shifted one index. These items have to be "moved over" to make room for the new item being inserted. The worst-case scenario is inserting at the 0th index, and every item in the array has to shift over.

# Delete
# In the worst case, deleting an item is linear time (O(n)). For any item you delete (unless it is the last item), all of the items after that index have to be shifted over to fill the now blank spot in the array. Remember, arrays store data in sequential order, so if we delete an item, we cannot just leave that space blank. If we left the space blank, it would ruin the quick lookup time. To have a fast lookup time, we need to be able to rely on the distance from the start of the array to whatever index we are trying to access.

# Space
# The space complexity of an array is linear (O(n)). Each item in the array will take up space in memory.

# Strengths
# Again, probably the dynamic array's biggest strength is not having to know or worry about the size of the data structure. It can grow to accommodate your data as needed. And, you don't have to manage this growth; the data structure itself grows when necessary. Dynamic arrays also have some of the same strengths as a static array. They also have efficient lookups (O(1)) when you have a specific index that you want to retrieve from.

# Weaknesses
# The main weakness of the dynamic array is related to its strength. To not have to worry about or manage the array's size, when the array runs out of room, it has to grow to accommodate more items. So, let's say your dynamic array is currently set up to store ten items. If it's full and you try to add an 11th item, the data structure can't just assume that there is a spot available right after the 10th item. It actually creates a new, bigger array and then copies all of the first ten items into the new array, and finally, it adds the 11th item. We will talk a bit more about how this works below. Additionally, dynamic arrays have the same weaknesses as static arrays, slow insertions and deletions (O(n)).

# Doubling Appends

# Underneath the hood of a dynamic array is a static array. When you create a dynamic array, it is a static array that keeps track of the starting index, the index of the last item that it stores, and the index for the last slot in its capacity. This brings up an important point. An array has a size and a capacity. An array's size is how many items it is storing at the moment. Its capacity is how many items it could store before it runs out of room.

# So, let's say that your dynamic array instantiates with an underlying static array with a capacity of 10 and a size of 0 when you create it. Then, you add ten items to the array. Now, it has a capacity of 10 and a size of 10. If you now go to append an 11th item to the array, you've run out of capacity. Here is where the dynamic of the dynamic array comes into play. The data structure will create a new underlying static array with a capacity twice the size of the original underlying static array. It will then copy the ten original items into the new array and finally add the 11th item. The cost of copying the original items into the new array is O(n). So, when we say that, in the worst-case, an append on a dynamic array has a time-complexity of O(n), this is why. However, all the other appends still have a time-complexity of O(1). So, in the average case append, the time-complexity is still efficient.

# Also, consider that as the array's capacity keeps doubling, the doublings will occur less and less frequently.

