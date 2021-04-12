# A stack data structure handles information in a last-in, first-out order. 
# This means that the last item added to the storage will be the first item removed from the storage. 
# A stack is like having a paper tray inbox on your desk. Anytime a person walks by and drops a piece of paper or a letter in your inbox, it will go on the top of your inbox. 
# So, when you process your inbox, the first item you would remove from the top of the stack of papers would be the last item added to it.

# Time and Space Complexity
# Push
# To push an item (add an item to the top of the stack) takes O(1) time.

# Pop
# To pop an item (remove an item from the top of the stack) takes O(1) time.

# Peek
# To peek at an item (inspect the item from the top of the stack without removing it) takes O(1) time.

# Space
# The space complexity of a stack is linear (O(n)). Each item in the stack will take up space in memory.

# Strengths
# The primary strength of a stack is that all of its operations are fast (take O(1) time).

# Weaknesses
# There are no weaknesses in this data structure. The reason is that it is a very targeted data structure designed to do a few things well.

# When are stacks useful?
# Stacks can be useful in any situation where you desire a LIFO order. One common use-case is for parsing strings. 
# Let's say you wanted to parse a string to ensure that all the parentheses in your string are correctly nested. A stack could be useful for this. 
# When you encounter an opening parenthesis, you add it to the stack. When you encounter a closing parenthesis, you remove the top opening parenthesis from the stack.
#  After going through all the characters in the string, the stack should be empty. 
# If it isn't or if you try to remove an item from an empty stack, you'll know that the parentheses were not correctly nested.

# Additionally, function calls and execution contexts are managed on a call stack. 
# When you call a function, it's added to the call stack. 
# When it returns, it gets popped off of the stack. 

# Last, an iterative depth-first-search can be done using a stack.

# There are two common ways to implement a stack. One is by using a linked list, and the other is by using a dynamic array. Both of these implementations work well.

class Stack_DA:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        return "The stack is empty"


# In the implementation that uses a linked list, the push method inserts a new node at the linked list's head, and the pop method removes the node at the linked list's head.

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None # Linked list points down!

class Stack_LL:
    def __init__(self):
        self.top = None

    def push(self, data):
        # create new node with data
        new_node = LinkedListNode(data)
        # point new_node at the one below it (current top)
        new_node.next = self.top
        # reset the top pointer to the new node
        self.top = new_node

    def pop(self):
        # make sure stack is not empty
        if self.top is not None:
            # store popped node
            popped_node = self.top
            # reset top pointer one below it (linked list points down)
            self.top = popped_node.next
            # return the value from the popped node
            return popped_node.data
