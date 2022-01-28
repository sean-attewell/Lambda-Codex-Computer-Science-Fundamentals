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

# O(1) - Constant time. number of operations is unaffected by input size, it is constant.

# O(log n) - Logarithmic Time.	As the input size increases, the runtime will grow slightly slower. Increases at first but then it stabilizes and changes less. logarithmic growth. The variable that's growing has an output that grows much slower than it (think 'log wants to be the exponent', or counting zeros in base 10 powers of 10 example). 
# An algorithm is said to have a logarithmic time complexity when it reduces the size of the input data in each step
# (it doesn’t need to look at all values of the input data)
# Algorithms with logarithmic time complexity are commonly found in operations on binary trees or when using binary search

# O(n) - Linear Time. means the number of operations grows at the same rate as the input size. Linear growth.

# O(n log n) - Quasilinear Time. (log-linear complexity – also called “linearithmic”)
# An algorithm is said to have a quasilinear time complexity when each operation in the input data have a logarithm time complexity.
# It is commonly seen in sorting algorithms (e.g. mergesort, timsort, heapsort).
# For example: for each value in the data1 (O(n)) use the binary search (O(log n)) to search the same value in data2.
# for value in data1:
    # result.append(binary_search(data2, value))

# O(n^c) - Polynomial.	As the input size increases, the runtime will grow at a faster rate. Polynomial (i.e. the variable that's growing is the number with an exponent rather than the exponent itself)

# O(n²) Quadratic Time
# An algorithm is said to have a quadratic time complexity when it needs to perform a linear time operation for each value in the input data, for example:
# In this case, for each item in the data, print every item in the data.
# for x in data:
#     for y in data:
#         print(x, y)
# Bubble sort is a great example of quadratic time complexity since for each value it needs to compare to all other values in the list

# O(c^n) - Exponential Time. As the input size increases, the runtime will grow at a much faster rate. Expontential. (the variable is the exponent, the exponent is what grows)
# An algorithm is said to have an exponential time complexity when the growth doubles with each addition to the input data set. 
# This kind of time complexity is usually seen in brute-force algorithms
# An example of an exponential time algorithm is the recursive calculation of Fibonacci numbers

# O(n!) - Factorial time. As the input size increases, the runtime will grow astronomically, even with relatively small inputs. Factorial growth.
# A great example of an algorithm which has a factorial time complexity is the Heap’s algorithm, which is used for generating all possible permutations of n objects.
# Another great example is the Travelling Salesman Problem

# Again, n (x axis) represents the size of the data, and on the chart above, N (y axis) represents the number of operations
# Big O notation describes how fast the runtime grows (relative to the input size)
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

# print every possible pair of things in the list
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

# We say that the running time is "big-O of f(n) or just "O of f(n)." We use big-O notation for asymptotic upper bounds, since it bounds the growth of the running time from above for large enough input sizes.

# If you go back to the definition of big-Θ notation, you'll notice that it looks a lot like big-O notation, except that big-Θ notation bounds the running time from both above and below, rather than just from above

# https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/big-big-theta-notation

# Big Theta (big-Θ):
# When we use big-Θ notation, we're saying that we have an asymptotically tight bound on the running time. "Asymptotically" because it matters for only large values of n. "Tight bound" because we've nailed the running time to within a constant factor above and below.


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


# https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7

# Computational complexity is a field from computer science which analyzes algorithms based on the amount resources required for running it.
# The amount of required resources varies based on the input size, so the complexity is generally expressed as a function of n, where n is the size of the input.

# In computer science, the time complexity is the computational complexity that describes the amount of time it takes to run an algorithm.
# Time complexity is commonly estimated by counting the number of elementary operations performed by the algorithm, supposing that each
# elementary operation takes a fixed amount of time to perform.

# Usually, when describing the time complexity of an algorithm, we are talking about the worst-case.

# Big-O notation, sometimes called “asymptotic notation”, is a mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity.

# In computer science, Big-O notation is used to classify algorithms according to how their running time or space requirements grow as the input size (n) grows. This notation characterizes functions according to their growth rates: different functions with the same growth rate may be represented using the same O notation.

# An algorithm is said to have a logarithmic time complexity when it reduces the size of the input data in each step
# (it doesn’t need to look at all values of the input data), for example:

data = [1, 2, 9, 8, 3, 4, 7, 6, 5]

for index in range(0, len(data), 3):
    print(data[index])
# 1
# 8
# 7

# Algorithms with logarithmic time complexity are commonly found in operations on binary trees or when using binary search. Let’s take a look at the example of a binary search, where we need to find the position of an element in a sorted list:


def binary_search(data, value):
    n = len(data)
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if value < data[middle]:
            right = middle - 1
        elif value > data[middle]:
            left = middle + 1
        else:
            return middle
    raise ValueError('Value is not in the list')


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(data, 7))
    # 6 (because 7 is found at index 6)

# Steps of the binary search:

# Calculate the middle of the list.
# If the searched value is lower than the value in the middle of the list, set a new right bounder.
# If the searched value is higher than the value in the middle of the list, set a new left bounder.
# If the search value is equal to the value in the middle of the list, return the middle (the index).
# Repeat the steps above until the value is found or the left bounder is equal or higher the right bounder.

# It is important to understand that an algorithm that must access all elements of its input data cannot take logarithmic time, as the time taken for reading input of size n is of the order of n.

# Quasilinear Time — O(n log n)
# An algorithm is said to have a quasilinear time complexity when each operation in the input data have a logarithm time complexity.
# It is commonly seen in sorting algorithms (e.g. mergesort, timsort, heapsort).
# For example: for each value in the data1 (O(n)) use the binary search (O(log n)) to search the same value in data2.

# for value in data1:
    # result.append(binary_search(data2, value))

# Another, more complex example, can be found in the Mergesort algorithm. Mergesort is an efficient, general-purpose,
# comparison-based sorting algorithm which has quasilinear time complexity, let’s see an example:
# (the image in the link is very helpful)


def merge_sort(data):
    if len(data) <= 1:
        return

    mid = len(data) // 2
    left_data = data[:mid]
    right_data = data[mid:]

    merge_sort(left_data)
    merge_sort(right_data)

    left_index = 0
    right_index = 0
    data_index = 0

    while left_index < len(left_data) and right_index < len(right_data):
        if left_data[left_index] < right_data[right_index]:
            data[data_index] = left_data[left_index]
            left_index += 1
        else:
            data[data_index] = right_data[right_index]
            right_index += 1
        data_index += 1

    if left_index < len(left_data):
        del data[data_index:]
        data += left_data[left_index:]
    elif right_index < len(right_data):
        del data[data_index:]
        data += right_data[right_index:]


if __name__ == '__main__':
    data = [9, 1, 7, 6, 2, 8, 5, 3, 4, 0]
    merge_sort(data)
    print(data)

# Quadratic Time — O(n²)
# An algorithm is said to have a quadratic time complexity when it needs to perform a linear time operation for each value in the input data, for example:
# In this case, for each item in the data, print every item in the data.

for x in data:
    for y in data:
        print(x, y)
# 0 0
# 0 1
# 0 2
# 0 3
# 0 4
# 0 5
# 0 6
# 0 7
# 0 8
# 0 9
# 1 0
# 1 1
# 1 2
# 1 3
# etc

# Bubble sort is a great example of quadratic time complexity since for each value it needs to compare to all other values in the list, let’s see an example:


def bubble_sort(data):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True

# If any swap took place in a run through the array, then swapped will be set to true
# This causes the while loop to keep going, and it does another run through the array from the start

if __name__ == '__main__':
    data = [9, 1, 7, 6, 2, 8, 5, 3, 4, 0]
    bubble_sort(data)
    print(data)


# Exponential Time — O(2^n)

# An algorithm is said to have an exponential time complexity when the growth doubles with each addition to the input data set. This kind of time complexity is usually seen in brute-force algorithms.

# As exemplified by Vicky Lai:
# In cryptography, a brute-force attack may systematically check all possible elements of a password by iterating through subsets. Using an exponential algorithm to do this, it becomes incredibly resource-expensive to brute-force crack a long password versus a shorter one. This is one reason that a long password is considered more secure than a shorter one.

# Another example of an exponential time algorithm is the recursive calculation of Fibonacci numbers:


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print('fibonacci of 4:', fibonacci(4))
# https://stackoverflow.com/questions/360748/computational-complexity-of-fibonacci-sequence/360773#360773


# Factorial — O(n!)

# An algorithm is said to have a factorial time complexity when it grows in a factorial way based on the size of the input data, for example:
# 2! = 2 x 1 = 2
# 3! = 3 x 2 x 1 = 6
# 4! = 4 x 3 x 2 x 1 = 24
# 5! = 5 x 4 x 3 x 2 x 1 = 120
# 6! = 6 x 5 x 4 x 3 x 2 x 1 = 720
# 7! = 7 x 6 x 5 x 4 x 3 x 2 x 1 = 5040
# 8! = 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 40320

# As you may see it grows very fast, even for a small size input.

# A great example of an algorithm which has a factorial time complexity is the Heap’s algorithm, which is used for generating all possible permutations of n objects.
# According to Wikipedia:

# Heap found a systematic method for choosing at each step a pair of elements to switch, in order to produce every possible permutation of these elements exactly once.
# Let’s take a look at the example:


def heap_permutation(data, n):
    if n == 1:
        print(data)
        return

    for i in range(n):
        heap_permutation(data, n - 1)
        if n % 2 == 0:
            data[i], data[n-1] = data[n-1], data[i]
        else:
            data[0], data[n-1] = data[n-1], data[0]


if __name__ == '__main__':
    data = [1, 2, 3]
    heap_permutation(data, len(data))

# The result will be:

# [1, 2, 3]
# [2, 1, 3]
# [3, 1, 2]
# [1, 3, 2]
# [2, 3, 1]
# [3, 2, 1]

# Note that it will grow in a factorial way, based on the size of the input data, so we can say the algorithm has factorial time complexity O(n!).
# Another great example is the Travelling Salesman Problem.
