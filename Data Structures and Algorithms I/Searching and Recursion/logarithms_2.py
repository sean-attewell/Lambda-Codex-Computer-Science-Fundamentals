# Logarithms are a way of looking differently at exponentials. I know that this is a bit of a vague definition, so let's look at an example.

# 2^5
# What does the mathematical expression above mean? It's an abbreviation for the following expression:
# 1 * 2 * 2 * 2 * 2 * 2

# What we are looking at above is two different ways to express an object that doubles in size with each iteration.
# Another way to think about 2^5 = 32 is that 2 is the "growth rate" and 5 is the number of times you went through the growth (doubling). 32 is the final result.

# Let's look at a few more expressions:

# 2^5 = 32
# 2^0 = 1
# 2^-1 = 1/2


# Now, to begin looking at logarithms, let's rewrite the exponential expressions above in logarithmic form.
# Logarithms have an inverse relationship with exponents, just like division and multiplication have an inverse relationship.

# log_2 32 = 5
# log_2 1 = 0
# log_2 1/2 = -1

# For our first expression,
# 2^5 = 32
# 2 was the "growth rate", 5 was the "time" spent growing, and 32 was where we ended up. When we rewrite this logarithmically, we have
# log_2 32 = 5
# In this case, 2 still represents the "growth rate" and 32 still represents where we end up. The 5 also still represents the "time" spent growing.

# So, the difference between when we would use a logarithm and when we use exponentiation depends on what factors we know ahead of time. 
# If you know the growth rate and you know how long you are growing, you can use exponentiation (2^5) to figure out where you end up (32). 
# However, if you know the growth rate and where you end up but do not know the time spent growing, you can use a logarithm (log_2 32) to figure that out.

# So "How long did I spend growing at this growth rate?" is another way of saying "what is the exponent?"


# Why should I care? What does this have to do with programming and interview preparation?
# In computer science, you often ask questions like "How many times must n be divided in half before we get to one?" 
# or "How many times will we halve this collection before the collection has only one item?" 
# To answer these questions, you can use logarithms! Halving is like doubling, so we can say that log_2 n would give us the answer we're seeking.

# You will see this come up when analyzing the time complexity of specific algorithms. 
# Any algorithm that doubles or halves a number or collection on each iteration of a loop is likely to have O(log n) time complexity. 
# You will see this come up specifically when we talk about binary search and its time complexity.
# You will also see this come up in specific sorting algorithms (like merge sort). 
# In simple terms, merge sort divides a collection in half and then merges the sorted halves. 
# The fact that the algorithm repeatedly halves something is your clue that it includes a logarithm in its time complexity. 
# One last place you're likely to see logarithms come up is with a perfect binary tree. One property of these binary trees is that the number of nodes doubles at each level.


# https://www.mathsisfun.com/algebra/logarithms.html

# Negative Logarithms

# logarithms deal with multiplying.
# What is the opposite of multiplying? Dividing!

# A negative logarithm means how many times to divide by the number.

# Example: What is log8(0.125) ... ?
# Well, 1 ÷ 8 = 0.125,
# So log8(0.125) = −1

# (think about how 8^1 is 1 x 8)

# "How long did I spend shrinking at this growth rate of 8 to end up at 0.125?" is another way of saying "what is the exponent?"
# 1 divided by 8 one time (-1)

# Same thing as "How long did I spend growing at a growth rate of 8 to end up at 1?"
# log_2 1 = 0
# The answer is 0 time. 1 x 2^0 = 1

# Example: What is log5(0.008) ... ?
# 1 ÷ 5 ÷ 5 ÷ 5 = 5^−3,
# So log5(0.008) = −3

# (think about how 5^3 is 1 x 5 x 5 x 5)

# the place you end up from either multiplying or dividing by the growth rate must be bigger than zero
# It may approach zero if you're dividing, but it won't get there


# The same way logarithms can be a zero counting function for powers of 10, negative powers of 10 ould the leading zeros (including one before the decimal place)
 
# 100	  1 × 10 × 10	  log10(100)	= 2
# 10	  1 × 10	      log10(10)	= 1
# 1	    1	            log10(1)	= 0
# 0.1	  1 ÷ 10	      log10(0.1)	= −1
# 0.01	1 ÷ 10 ÷ 10	  log10(0.01)	= −2

# "Logarithm" is a word made up by Scottish mathematician John Napier (1550-1617)
# from the Greek word logos meaning "proportion, ratio or word" and arithmos meaning "number"
# ... which together makes "ratio-number" !

