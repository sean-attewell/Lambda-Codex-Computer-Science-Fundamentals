# A queue is a data structure that stores its items in a first-in, first-out (FIFO) order. That is precisely why it is called a queue. 
# It functions just like a queue (or a line) would in everyday life.

# Time and Space Complexity
# Enqueue
# To enqueue an item (add an item to the back of the queue) takes O(1) time.

# Dequeue
# To dequeue an item (remove an item from the front of the queue) takes O(1) time.

# Peek
# To peek at an item (inspect the item from the front of the queue without removing it) takes O(1) time.

# Space
# The space complexity of a queue is linear (O(n)). Each item in the queue will take up space in memory.

# Strengths
# The primary strength of a queue is that all of its operations are fast (take O(1) time).

# Weaknesses
# There are no weaknesses in this data structure. The reason is that it is a very targeted data structure designed to do a few things well.

# When are queues useful?
# Queues are useful data structures in any situation where you want to make sure things are processed in a FIFO order. 
# Think of a web server. The server might be trying to service thousands of page requests per minute. 
# It would make the most sense for the server to process and respond to the requests in the same order that they were received. 
# That way, the first client to request a page is the first client to receive a response. 
# Also, you'll learn soon enough about traversing hierarchical data structures. 
# One of the ways you do that is called a breadth-first traversal. To conduct a breadth-first traversal, a queue can be used.


# Queue class that uses a singly-linked list as the underlying data structure.

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        # next points in the direction of the rear of the queue
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    #     
    def enqueue(self, item):
        new_node = LinkedListNode(item)
        # check if queue is empty
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            # add new node to rear
            self.rear.next = new_node
            # reassign rear to new node
            self.rear = new_node
    def dequeue(self):
        # check if queue is empty
        if self.front is not None:
            # keep copy of old front
            old_front = self.front
            # set new front
            self.front = old_front.next # remeber it points in the direction of the rear

        # check if the queue is now empty
        if self.front is None:
            # make sure rear is also None
            self.rear = None

        return old_front
