# What is the call stack?
# The whole reason we are talking about stacks in the first place is so we can understand the call stack. Call stacks help us understand recursion.

# Whenever your program calls a function, the computer sets aside a chunk of memory for its execution context. 
# Any variables in that function scope are stored here.

# The computer stores these chunks of memory in the call stack, which has two fundamental operations: pushing onto the top and popping off the stack's top. 
# The computer pushes a chunk on the stack when a function is called. 
# The computer pops a piece off when a function finishes executing and returns. 

# We have two functions defined in our scope — one to add 2 to our input, and another to add 4.

def add_two(num):
    return num + 2

def add_four(num):
    return add_two(add_two(num))

# Let's think about what the call stack looks like when we call these functions. First, what happens when we run the following:

add_two(2)
add_four(6)

# add_two call gets pushed onto the call stack
# num gets stored in memory with the value 2
# num + 2 gets returned as 4 and that call gets popped off

# add_four call gets pushed on the stack, and 6 gets stored as num
# the innermost add_two call gets pushed onto the stack, and 6 gets stored as num
# the innermost add_two call returns 8 and pops off
# the second add_two call gets pushed onto the stack with 8 as num
# the second add_two call returns 10 and gets popped off
# we are back in the context of add_four, which now returns 10 and pops off the stack
# the stack is now empty



# Next, we look at the Fibonacci Sequence. This is a series of numbers:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# We can derive the next number in the sequence by summing the previous two numbers — so the following number in the series shown above would be 55 (34 + 21).


# So we can write the 7th term as xn, and you can describe any term in the sequence as:

# x_n = x_{n-1} + x_{n-2}

# Using this rule, if you wanted to find the 10th term, you could write:

# x_{10} = x_{10-1} + x_{10-2}
# x_{10} = x_9 + x_8
# x_{10} = 34 + 21
# x_{10} = 55

# Calculate the nth term (zero based counting)
def recursive_fib(n):
    if n <= 1:
        return n
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)

print(recursive_fib(10))
# 55

# The base cases are the first two terms in the sequence; the 0th term is 0, and the 1st term is 1. 
# For every other term, we find the value by summing the previous two terms.

# To more clearly illustrate the building of the stack, we will split our return statement up like this:

def recursive_fib2(n):
    if n <= 1:
        return n
    else:
        n_minus_1 = recursive_fib2(n-1)
        n_minus_2 = recursive_fib2(n-2)
        return n_minus_1 + n_minus_2

print(recursive_fib2(6))

# Visualise on Python tutor to understand the call stack
# Note that it shows the stack upside down
# But does show the execution context for each function call (any variables in that function scope are stored here).

# Each call to recursive_fib2 has to recursively call itself until it gets the answer for n_minus_1 in it's execution context
# Then has to recursively call itself to get the answer for n_minus_2 in its execution context
# Then it adds them up
# Which either is the final answer
# Or returned to the call below it on the stack as the answer for n_minus_1 or n_minus_2

# https://medium.com/popfizzcs/tracing-recursion-6e787c0adc74

