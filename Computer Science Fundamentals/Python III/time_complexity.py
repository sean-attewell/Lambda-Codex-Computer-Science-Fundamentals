# What is an algorithm?
# An algorithm is a set of instructions for accomplishing a task. Within this broad definition, we could call every piece of code an algorithm.

# When given a choice between different algorithms, we want to choose the most efficient algorithm (considering both time and space efficiency depending on our needs).

# Big O notation is called this because:
# "Big" means "capital", and "O" means order, as in "order of complexity".
# So named because of the convention of writing "order of complexity" as O(f(x)),
# e.g., with a capital letter 'O', or a 'Big O'.

# The specific terms of Big O notation describe how fast the runtime grows (relative to the input size)
# focusing on when the input gets extremely large.

# The actual runtime depends on the specific computer running the algorithm, so we cannot compare efficiencies that way. By focusing on the general growth, we can avoid exact runtime differences between machines and environments.

# We also talk about runtime relative to the input size because we need to express our speed in terms of something. So we show the speed of the algorithm in terms of the input size. That way, we can see how the speed reacts as the input size grows.

# n represents the size of the data (x axis), and on the chart above, N represents the number of operations (y axis).
# So you're looking at how the number of operations (N) changes, depending on the size of the data (n)

# We don't care about speed when the input size is small. The differences in speed are likely to be minimal when the input size is small. When the input size gets enormous, we can see the differences in efficiency between algorithms.

# O(1) number of operations is unaffected by input size, it is constant.
# O(log n)	As the input size increases, the runtime will grow slightly slower. logarithmic growth. The variable that's growing has an output that grows much slower than it (think 'log wants to be the exponent', or counting zeros in base 10 powers of 10 example)
# O(n) means the number of operations grows at the same rate as the input size. Linear growth.
# O(n^c)	As the input size increases, the runtime will grow at a faster rate. Polynomial (i.e. the variable that's growing is the number with an exponent rather than the exponent itself)
# O(c^n) As the input size increases, the runtime will grow at a much faster rate. Expontential. (the variable is the exponent, the exponent is what grows)
# O(n!) As the input size increases, the runtime will grow astronomically, even with relatively small inputs. Factorial growth.

# Again, n (x axis) represents the size of the data, and on the chart above, N (y axis) represents the number of operations

# Note: Big O only matters for large data sets. An O(n^3) solution is adequate, as long as you can guarantee that your datasets will always be small.


my_list = ['thing 1', 'thing 2', 'thing 3', 'thing 4', 'thing 5']

# Constant Time O(1)
# No matter how large or small the input is (1,000,000 or 10), the number of computations within the function is the same.


def print_only_one_thing(list_of_things):
    print(list_of_things[0])


print_only_one_thing(my_list)  # thing 1


# Linear Time O(n)
# the runtime of the algorithm increases at the same rate as the input size

def print_list(list_of_things):
    for thing in list_of_things:
        print(thing)


print_list(my_list)


# Quadratic: involving the second and no higher power of an unknown quantity or variable.
# e.g. ax^2 + bx + c
# Quadratus is Latin for square.

# Quadratic Time O(n^2)
# Why is this quadratic time? The clue is the nested for loops. These nested for loops mean that for each item in list_of_things (the outer loop),
# we iterate through every item in list_of_things (the inner loop). For an input size of n, we have to print n * n times or n^2 times.

def print_permutations(list_of_things):
    for thing_one in list_of_things:
        for thing_two in list_of_things:
            print(thing_one, thing_two)


print_permutations(my_list)
# 5 items in the list. Prints out all 5 items for every item = 5*5 = 5^2 = quadratic  = a second degree monomial = polynomial time.

# thing 1 thing 1
# thing 1 thing 2
# thing 1 thing 3
# thing 1 thing 4
# thing 1 thing 5
# thing 2 thing 1
# thing 2 thing 2
# thing 2 thing 3
# thing 2 thing 4
# thing 2 thing 5
# thing 3 thing 1
# thing 3 thing 2
# thing 3 thing 3
# thing 3 thing 4
# thing 3 thing 5
# thing 4 thing 1
# thing 4 thing 2
# thing 4 thing 3
# thing 4 thing 4
# thing 4 thing 5
# thing 5 thing 1
# thing 5 thing 2
# thing 5 thing 3
# thing 5 thing 4
# thing 5 thing 5

# = total of 25

# What are we supposed to do with the constants?


def do_a_bunch_of_stuff(list_of_things):  # O(1 + n/2 + 1000)
    last_idx = len(list_of_things) - 1
    print(list_of_things[last_idx])  # O(1)

    middle_idx = len(list_of_things) / 2
    idx = 0
    while idx < middle_idx:  # O(n/2)
        print(list_of_things[idx])
        idx = idx + 1

    for num in range(1000):  # O(1000)
        print(num)


# do_a_bunch_of_stuff(my_list)

# print(items[last_idx]) is constant time because it doesn't change as the input changes. So, that portion of the function is O(1).

# The while loop that prints up to the middle index is 1/2 of whatever the input size is; we can say that portion of the function is O(n/2).

# The final portion will run 1000 times, no matter the size of the input.

# So, putting it all together, we could say that the efficiency is O(1 + n/2 + 1000). However, we don't say this. We describe this function as having linear time O(n) because we drop all of the constants. Why do we cut all of the constants? Because as the input size gets huge, adding 1000 or dividing by 2 has minimal effect on the algorithm's performance.


# Most significant term

def do_different_things_in_the_same_function(list_of_things):  # O(n + n^2)
    # print all each item in the list
    for thing in list_of_things:  # O(n)
        print(thing)

    # print every possible pair of things in the list
    for thing_one in list_of_things:  # O(n * n) = O(n^2)
        for thing_two in list_of_things:
            print(thing_one, thing_two)


# We could describe this function as O(n + n^2); however, we only need to keep the essential term, n^2, so this would be O(n^2). Why can we do this? Because as the input size (n) gets larger and larger, the less significant terms have less effect, and only the most significant term is important.


# Big O represents the worst-case

def find_thing(list_of_things, thing_we_are_trying_to_find):
    for thing in list_of_things:
        if thing == thing_we_are_trying_to_find:
            return True

    return False

# What would the result be if it just so happens that the thing_we_are_trying_to_find in list_of_things is the very first item in the list? The function would only have to look at one item in list_of_things before returning. In this case, it would be O(1). But, when we talk about a function's complexity, we usually assume the "worst case." What would the "worst-case" be? It would be if it were the last item in list_of_things. In that case, we would have to look through all the list_of_things, and that complexity would be O(n)

# Big theta gives both an upper and a lower bound for the running time. Big O only provides an upper bound.

# https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/big-o-notation

# We say that the running time is "big-O of f(n)f(n)f, left parenthesis, n, right parenthesis" or just "O of f(n)f(n)f, left parenthesis, n, right parenthesis." We use big-O notation for asymptotic upper bounds, since it bounds the growth of the running time from above for large enough input sizes.

# If you go back to the definition of big-Θ notation, you'll notice that it looks a lot like big-O notation, except that big-Θ notation bounds the running time from both above and below, rather than just from above

# https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/big-big-theta-notation

# Big Theta (big-Θ):
# When we use big-Θ notation, we're saying that we have an asymptotically tight bound on the running time. "Asymptotically" because it matters for only large values of nnn. "Tight bound" because we've nailed the running time to within a constant factor above and below.


# Do constants ever matter?

# Complexity analysis with Big O notation is a valuable tool. It would be best if you got in the habit of thinking about the efficiency of the algorithms you write and use in your code. However, just because two algorithms have the same Big O notation doesn't mean they are equal.

# Imagine you have a script that takes 1 hour to run. By improving the function, you can divide that runtime by six, and now it only takes 10 minutes to run. With Big O notation, O(n) and O(n/6) can both be written as O(n), but that doesn't mean it isn't worth optimizing the script to save 50 minutes every time the script runs.

#  It is your job as a developer to know when making your code more efficient is necessary. You will always be making calculated tradeoffs between runtime, memory, development time, readability, and maintainability. It takes time to develop the wisdom to strike the right balance depending on the scenario.

# Let's look at a few code snippets and classify their runtime complexity using Big O notation.

def foo(n):
    i = 1
    while i < n:
        print(i)
        i *= 2

# First, let's think about what the above function is doing. It's printing i…but i is not being incremented by 1, as we usually see. It's doubled every time we run the loop. So, for example, if n = 100, then the final result would be…

# 1
# 2
# 4
# 8
# 16
# 32
# 64

# Or if n = 10, then we would print…

# 1
# 2
# 4
# 8

# We can use the process of elimination to narrow down which runtime classification makes sense for this algorithm. The number of times the loop runs seems to vary based on the value of n, so this is NOT O(1).

# From the above examples, we can also see that the number of times the loop runs is increasing slower than the input size is increasing. n must be doubled before the loop will run one more time. We can eliminate classifications such as O(n log n), O(n^c), O(c^n), and O(n!).

# The only two options left at this point are logarithmic and linear. Since the two growth rates (input, the number of operations) are not the same, this function must run in logarithmic time!
