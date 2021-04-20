# There is only one way to traverse linear data structures like arrays, linked lists, queues, and stacks. 
# The linear nature of the structure itself forces a particular type of traversal.

# However, with hierarchical structures like trees, there are multiple ways that you can traverse the stored data. 
# There are two primary categories for tree traversals:

# Depth-First
# Breadth-First

# Furthermore, there are three different types of depth-first traversals:
# Inorder
# Preorder
# Postorder

# They depend on when you visit them. 
# Inorder means left visit right
# Preorder means you visit first: visit left right
# Post order means you visit last: left right visit

# Depth-First Inorder Traversal

# In this traversal, we start at the tree's root node and complete the following steps recursively:

# Go to the left subtree
# Visit node
# Go to the right subtree

# visualised by turning grey for going to the node and red for actually visiting

# So you keep going to the left subree of each left subtree until you hit the end
# then visit that node and turn it red
# then check the right node

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def helper_inorder(root, res):
    if root is None:
        return
    helper_inorder(root.left, res)
    res.append(root.val)
    helper_inorder(root.right, res)

def inorder_traversal(root):
    result = []
    helper_inorder(root, result)
    return result


# Depth-First Preorder Traversal
# This traversal type is very similar to an inorder traversal except that the three steps' order is slightly different. 
# Notice that in this traversal, we "visit" the node before we recurse to the left subtree 
# In the inorder traversal above, we recursed to the left subtree before visiting the node.

# Visit the node
# Go to the left subtree
# Go to the right subtree

def helper_preorder(root, res):
    if root is None:
        return
    res.append(root.val)
    helper_preorder(root.left, res)
    helper_preorder(root.right, res)

def preorder_traversal(root):
    result = []
    helper_preorder(root, result)
    return result


# Depth-First Postorder Traversal
# This traversal type is very similar to our other traversals except that the three steps' order is slightly different. 
# Notice that in this traversal, we "visit" the node after we recurse to the left subtree and the right subtree.

# Go to the left subtree
# Go to the right subtree
# Visit node

def helper_postorder(root, res):
    if root is None:
        return
    helper_postorder(root.left, res)
    helper_postorder(root.right, res)
    res.append(root.val)

def postorder_traversal(root):
    result = []
    helper_postorder(root, result)
    return result


# In a breadth-first traversal, we visit all the nodes at the same level (same distance from the root node) before going on to the next level.

# A breadth-first traversal and a level order traversal are the same things. 
# However, a breadth-first traversal can be done on any hierarchical data structure like trees and graphs. 
# But, a level order traversal refers only to the traversal of a tree. 
# Graphs do not have levels like trees do, so that term would not make sense.

# A breadth-first traversal is a little different than the depth-first traversals we've gone over. 
# We cannot merely use the recursive call stack to keep track of where we are in the tree. 
# Instead, we must use a queue to keep track of what nodes we should visit. 
# Remember that a queue data structure follows a first-in-first-out (FIFO) access order.

# add root
# pop
# add left of one you just popped off queue
# add right of one you just popped off queue
# pop first in (left just added)
# add left of that one just popped
# add right of that one just popped

def breadth_first_traversal(root):
    if root is None:
        return []

    result = []
    queue = []
    queue.append(root)

    while len(queue) != 0:
        node = queue.pop(0) # Setting the pop index at 0 rather than the end keeps it FIFO
        result.append(node.val)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return result
