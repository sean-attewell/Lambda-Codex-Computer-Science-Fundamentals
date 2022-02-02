# A linked list is a simple, linear data structure used to store a collection of elements. 
# Unlike an array, each element in a linked list does not have to be stored contiguously in memory.

# Because the elements are not stored contiguously, each element in memory must contain information about the next element in the list. 
# The first item stores the data 43 and the location in memory (*3) for the next item in the list (shown in the nextdoor memory bucket to 43)

# the second item in the list could be located anywhere in memory. It could even come before the first item in memory.


# Pretty much any type of data can be stored in a linked list. Strings, numbers, booleans, and other data structures can be stored. 
# You should not feel limited using a linked list based on what type of data you are trying to store.

# The elements in a linked list can be either sorted or unsorted. 
# There is nothing about the data structure that forces the elements to be sorted or unsorted.

# Linked lists can contain duplicates. 
# There is nothing about the linked list data structure that would prevent duplicates from being stored.


# There are three types of linked lists: 
# singly linked list (SLL)
# doubly linked list (DLL)
# circular linked list. 

# All linked lists are made up of nodes where each node stores the data and also information about other nodes in the linked list.

# Each singly linked list node stores the data and a pointer where the next node in the list is located. 
# Because of this, you can only navigate in the forward direction in a singly linked list. 
# To traverse an SLL, you need a reference to the first node called the head. From the head of the list, you can visit all the other nodes using the next pointers.

# Each node in a DLL also stores a reference to the previous item. 
# Because of this, you can navigate forward and backward in the list. 
# A DLL also usually stores a pointer to the last item in the list (called the tail).

# A Circular Linked List links the last node back to the first node in the list. 
# This linkage causes a circular traversal; when you get to the end of the list, the next item will be back at the beginning of the list.

# Time and Space Complexity

# Lookup
# To look up an item by index in a linked list is linear time (O(n)). 
# To traverse through a linked list, you have to start with the head reference to the node and then follow each subsequent pointer to the next item in the chain. 
# Because each item in the linked list is not stored contiguously in memory, you cannot access a specific index of the list using simple math. 
# The distance in memory between one item and the next is varied and unknown.

# Append
# Adding an item to a linked list is constant time (O(1)). 
# We always have a reference point to the tail of the linked list, so we can easily insert an item after the tail.
# NOTE: Video says for a SLL it's only quick at the head (prepend), and that the end (append) will be linear time. In DLL you would know the tail.
# This makes sense based on implementation coded below, where append requires starting at the head and going through.

# Insert
# In the worst case, inserting an item in a linked list is linear time (O(n)). 
# To insert an item at a specific index, we have to traverse — starting at the head — until we reach the desired index.

# Delete
# In the worst case, deleting an item in a linked list is linear time (O(n)). 
# Just like insertion, deleting an item at a specific index means traversing the list starting at the head.

# Space
# The space complexity of a linked list is linear (O(n)). Each item in the linked list will take up space in memory.

# Strengths of a Linked List
# The primary strength of a linked list is that operations on the linked list's ends are fast. 
# This is because the linked list always has a reference to the head (the first node) and the tail (the last node) of the list.
#  Because it has a reference, doing anything on the ends is a constant time operation (O(1)) no matter how many items are stored in the linked list. 
# 
# Additionally, just like a dynamic array, you don't have to set a capacity to a linked list when you instantiate it. 
# If you don't know the size of the data you are storing, or if the amount of data is likely to fluctuate, linked lists can work well. 
# One benefit over a dynamic array is that you don't have doubling appends. 
# This is because each item doesn't have to be stored contiguously; whenever you add an item, you need to find an open spot in memory to hold the next node.

# Weaknesses of a Linked List
# The main weakness of a linked list is not efficiently accessing an "index" in the middle of the list. 
# The only way that the linked list can get to the seventh item in the linked list is by going to the head node and then traversing one node at a time 
# until you arrive at the seventh node. 
# You can't do simple math and jump from the first item to the seventh.

# What data structures are built on linked lists?
# Remember that linked lists have efficient operations on the ends (head and tail). 
# There are two structures that only operate on the ends; queues and stacks. 
# So, most queue or stack implementations use a linked list as their underlying data structure.

# Why is a linked list different than an array? What problem does it solve?
# We can see the difference between how a linked list and an array are stored in memory, but why is this important? 
# Once you see the problem with the way arrays are stored in memory, the benefits of a linked list become clearer.
#
# The primary problem with arrays is that they hold data contiguously in memory. 
# Remember that having the data stored contiguously is the feature that gives them quick lookups. 
# If I know where the first item is stored, I can use simple math to figure out where the fifth item is stored. 
# The reason that this is a problem is that it means that when you create an array, you either have to know how much space in memory you need to set aside
# or you have to set aside a bunch of extra memory that you might not need, just in case you do need it. 
# In other words, you can be space-efficient by only setting aside the memory you need at the moment. 
# But, in doing that, you are setting yourself up for low time efficiency if you run out of room and need to copy all of your elements to a newer, bigger array.
# (instead of constant time complexity, appending an element to an array becomes linear in this case. 
# Prepending to a SLL linked list, and prepending/appending to a DLL however, will always be constant time)
#
# With a linked list, the elements are not stored side-by-side in memory. Each element can be stored anywhere in memory.
# In addition to storing the data for that element, each element also stores a pointer to the memory location of the next element in the list. 
# The elements in a linked list do not have an index. 
# To get to a specific element in a linked list, you have to start at the head of the linked list and work your way through the list, one element at a time
# to reach the specific element you are searching for. 
# Now you can see how a linked list solves some of the problems that the array data structure has.


# How do you represent a singly linked list graphically and in Python code?
# Let’s say you wanted to store the numbers 1, 2, and 3. You would need to create three nodes. 
# Then, each of these nodes would be linked together using the pointers.
# The last element or node in the linked list does not have a pointer to any other node. This fact is how you know you are at the end of the linked list.

class LinkedListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):  
        self.head = head

    def append(self, data): # Appending to tail 
        new_node = LinkedListNode(data)

        if self.head:
            current = self.head # Starts at the start, if there is a start

            while current.next: # if the node links to another, go to the next one
                current = current.next

            current.next = new_node # When you get to the end, link it to the new node
        else:
             self.head = new_node # If there is no head, new node becomes the head

# Note that this appends to the tail rather than pre-pending to the head.
# Hence it has to traverse through the linked list with linear time
# That's because this is a singly linked list (SLL)
# A doubly linked list (DLL) also usually stores a pointer to the last item in the list (called the tail)
# For a doubly linked list it would therefore me constant time O(1)

a = LinkedListNode(1)
my_ll = LinkedList(a)
my_ll.append(2)
my_ll.append(3)

print(my_ll.head.data) # 1
print(my_ll.head.next) # <__main__.LinkedListNode object at 0x00000221075F3940>

print(my_ll.head.next.data) # 2
print(my_ll.head.next.next.data) # 3


# https://www.youtube.com/watch?v=njTh_OwMljA

# This vid shows a prepend method too.
# Makes a new head node, sets it's 'next' to the old head
# Then updates the head pointer (head = NewHead)

# Shows a delete method - much like append it walks through
# but 'if current.next.data == dataToDel'
# then current.next = current.next.next
# to cut out the one you're deleting
# special case for deleting the head:
# if head.data == dataToDel
# then head = head.next
# again just cuts it out
