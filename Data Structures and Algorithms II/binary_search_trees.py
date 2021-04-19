# There are lots of different types of tree data structures. A binary tree is a specific type of tree. 
# It is called a binary tree because each node in the tree can only have a maximum of two child nodes. 
# It is common for a node's children to be called either left or right.

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# "Perfect" Trees
# A "perfect" tree has all of its levels full. This means that there are not any missing nodes in each level.
# "Perfect" trees have specific properties: 

# First, the quantity of each level's nodes doubles as you go down.
# Second, the quantity of the last level's nodes is the same as the quantity of all the other nodes plus one.


# The height of a tree is the number of levels that it contains. 
# Based on the properties outlined above, we can deduce that we can calculate the tree's height with the following formula:

# log_2(n+1) = h

# where n is the number of nodes
# so a perfect tree with 15 nodes, the height is 4
# because the exponent of 2 that gives you 16 is 4

# If you know the tree's height and want to calculate the total number of nodes, you can do so with the following formula:

# n = 2^h - 1

# so a perfect tree with a height of 4 has 15 nodes.


# Just like a binary tree is a specific type of tree, a binary search tree (BST) is a specific type of binary tree. 
# A binary search tree is just like a binary tree, except it follows specific rules about how it orders the nodes contained within it. 
# For each node in the BST, all the nodes to the left are smaller, and all the nodes to the right of it are larger.

# We can call a binary search tree balanced if the heights of its left and right subtrees differ by at most one, and both of the subtrees are also balanced.

# Time and Space Complexity

# Provided it is reasonably balanced:
# The order of nodes in a BST means that each comparison skips about half of the remaining tree
# so the whole lookup takes time proportional to the binary logarithm of the number of items stored in the tree

# Lookup
# If a binary search tree is balanced, then a lookup operation's time complexity is logarithmic (O(log n)). 
# If the tree is unbalanced, the time complexity can be linear (O(n)) in the worst possible case 
# (virtually a linear chain of nodes will have all the nodes on one side of the tree).

# Insert
# If a binary search tree is balanced, then an insertion operation's time complexity is logarithmic (O(log n)). 
# If the tree is entirely unbalanced, then the time complexity is linear (O(n)) in the worst case.

# Delete
# If a binary search tree is balanced, then a deletion operation's time complexity is logarithmic (O(log n)). 
# If the tree is entirely unbalanced, then the time complexity is linear (O(n)) in the worst case.

# Space
# The space complexity of a binary search tree is linear (O(n)). Each node in the binary search tree will take up space in memory.


# Strengths
# One of the main strengths of a BST is that it is sorted by default. 
# You can pull out the data in order by using an in-order traversal. 
# BSTs also have efficient searches (O(log n)). 
# They have the same efficiency for their searches as a sorted array (using binary search); however, BSTs are faster with insertions and deletions. 
# In the average-case, dictionaries have more efficient operations than BSTs, but a BST has more efficient operations in the worst-case.
# Dictionaries (hash tables) have O(1) lookip, insertion and deletion in the average case, but O(n) when there are hash collisions.

# Weaknesses
# The primary weakness of a BST is that they only have efficient operations if they are balanced. 
# The more unbalanced they are, the worse the efficiency of their operations gets. 
# Another weakness is that they are don't have stellar efficiency in any one operation. 
# They have good efficiency for a lot of different operations. So, they are more of a general-purpose data structure.

# If you want to learn more about trees that automatically rearrange their nodes to remain balanced, look into AVL trees or Red-Black trees



# To create a binary search tree, we need to define two different classes: one for the nodes that will make up the binary search tree and another for the tree itself.

class BST:
    def __init__(self, value):
        self.root = BSTNode(value)

    def insert(self, value):
        self.root.insert(value)

    def search(self, value):
        self.root.search(value)

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def search(self, target):
        if self.value == target:
            return self
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.search(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(target)


# implement a delete operation on our BST and BSTNode classes, we must consider three cases:

# If the BSTNode to be deleted is a leaf (has no children), we can remove that node from the tree.
# If the BSTNode to be deleted has only one child, we copy the child node to be deleted and delete it.
# If the BSTNode to be deleted has two children, we have to find the "in-order successor". 
# The "in-order successor" is the next highest value, the node that has the minimum value in the right subtree.

# Given the above information, can you write pseudocode for a method that can find the minimum value of all the nodes within a tree or subtree?

# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/ <-- delete in python example (first example, python not python3)