# Recursion is a method to solve problems. 
# It means breaking down a problem into smaller and smaller sub-problems until the sub-problem is easy to solve. 
# Recursive functions call themselves. 
# Often, recursive solutions are terse and elegant. 
# Recursive solutions are not always the most efficient


def sum_list(items):
    sum = 0
    for i in items:
        sum = sum + i
    return sum

# This iterative function depends on the ability to loop through each item in the list. 
# Another way to iterate through a collection is with recursion.

# How many numbers can you sum without having to rely on the loop construct? 
# The answer is two. 
# How can we think of our problem as a collection of sums of only two numbers?

# separate the problem into two subproblems
# continue doing so until we can no longer divide the problem into two subproblems:
# 1 + 2 + 3 + 4 + 5
# (1 + (2 + 3 + 4 + 5))
# (1 + (2 + (3 + 4 + 5)))
# (1 + (2 + (3 + (4 + 5))))
# (1 + (2 + (3 + (4 + (5)))))

# Once we no longer have a list of items longer than one, we cannot break the list into the first item and the rest of the items. 
# So if someone asks us to sum one number, we know that the result is equal to that number. 
# This "running out" is the base case for our recursive function.

# Note: We usually place the base case of a recursive function in the first few lines of the function, though it doesn't have to be there.

my_list = [1,2,3,4,5,6]

def sum_list_recursively(items):
    if len(items) == 1: # Base case
        return items[0]
    else:
        return items[0] + sum_list(items[1:]) # items[1:] has one less item

print(sum_list_recursively(my_list))

# You can see how the recursive calls go "out" before returning and starting working their way "back" to the original call.

# When the function is called within the function, each time imagine going to a new piece of paper below
# Which will eventually return to the paper above it, until you get back up to the original piece of paper.

def print_to_zero(n):
    if n < 0: # base case
        return
    print(n)
    return print_to_zero(n - 1) # recursive case

print_to_zero(-4)

# An == 0 base case could lead to infinite recursion with negative numbers 
# the base case wouldn't hit and it would keep taking away 1


# The three rules for a recursive function are:

# Must have a base case
# Must change its state to move towards the base case
# Must call itself


# What is a base case? It allows the algorithm to stop recursing. 
# With our sum_list function, what allows the algorithm to stop recursing?
# It's the first line: if len(items) == 1:. Notice how if this condition is true, it returns a value and doesn't make a recursive call to itself. 
# We are saying to stop recursing if the list to sum has only one item.

# The second rule is that the algorithm must change its state to move towards the base case.
# How does our function do that? With each subsequent recursion, the list passed into sum_list is one item smaller. 
# For example, on the first recursion, items is [2,3,4,5], and on the subsequent recursion, items is [3,4,5].

# The third rule is that the algorithm must call itself. We are doing this on the final line of the function.
# return items[0] + sum_list(items[1:])


# So, what clues or hints might you find within a problem that could lead you to use recursion?
# Compute the nth term
# List the first or last n terms
# Generate all permutations

# Another way to think about it is to use the three rules. 
# Is there a clear base case or stopping point that you are working towards (Rule 1)? 
# Is there a straightforward way that the state of the data changes with each iteration that brings it closer to the base case (Rule 2)?


# Let's look at another typical example of learning recursion–computing factorials.

# When does computing factorials come in handy? 
# They are required when figuring combinations; how many ways can we arrange these many items? 
# Or how many orders can there be with this list? 
# Also, they are useful for determining ways of choosing a certain number of items from a collection. 
# For example, if you have 100 different menu items, how many possible 5-item orders could you make?

# Base case: stop when we hit 1
# And Rule 2 is satisfied because we make each subsequent call to factorial on a smaller n.
# For any n! we can solve it by breaking it into smaller sub-problems that also require factorial (Rule 3).

def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)


# https://www.interviewcake.com/concept/python3/overlapping-subproblems?course=fc1&section=dynamic-programming-recursion

# A problem has overlapping subproblems if finding its solution involves solving the same subproblem multiple times.

# https://betterprogramming.pub/when-to-loop-when-to-recurse-b786ad8977de

# One good example of this would be searching through a file system. You could start at the root folder, 
# and then you could search through all the files and folders within that one. 
# After that, you would enter each folder and search through each folder inside of that.

# Recursion works well for this type of structure because you can search multiple branching paths 
# without having to include many different checks and conditions for every possibility.

# For those of you who are familiar with data structures, you might notice that the image above of the file system looks a lot like a tree structure.
# Trees and graphs are another time when recursion is the best and easiest way to do traversal.

# Recursion is a useful tool, but it can increase memory usage.
# Another thing to consider is that understanding and reading your code might sometimes be easier to do in an iterative solution.

# Every time we add a new call to the stack, we are increasing the amount of memory that we are using. 
# If we are analyzing the algorithm using Big O notation, then we might note that this increases our space complexity.

# There are times when we might want to pay this cost in order to get a short, useful algorithm, like when we are traversing a tree. 
# But there are other times when there may be better, more efficient ways of solving this problem.

# For many small projects, the call stack won’t hamper you program very much. 
# However, once your program starts making many recursive calls, then you might want to consider the potential impact of your large call stack.

