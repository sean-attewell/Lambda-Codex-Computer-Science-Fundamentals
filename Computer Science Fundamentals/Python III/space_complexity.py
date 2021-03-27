# Talking about space complexity is very similar to talking about time complexity. Except with space complexity, we are looking at the efficiency of memory usage instead of the number of operations.

# Often, it isn't easy to optimize for time and space at the same time. For instance, by increasing time efficiency, you may need to use more memory and decrease space complexity. This is not always the case, but you have to decide if you are optimizing for space or time complexity because of this.


def print_something_a_certain_number_of_times(thing_to_print, number_of_times):
    for _ in range(number_of_times):
        print(thing_to_print)

# The function above has a constant (O(1)) space complexity because no matter how large n gets, the amount of memory being used stays the same.

# print_something_a_certain_number_of_times("Get it", 5)

# This function takes O(n) space:


def append_to_list_a_certain_number_of_times(number_of_times):
    # create an empty list
    my_list = []

    # append to the list the number of times specified by the caller
    for _ in range(number_of_times):
        my_list.append("lambda")

    return my_list


# We are often referring to additional space when we talk about space complexity–meaning that we do not include the memory used by the inputs.
# This function takes constant space (O(1)) even though the input has n items:


def get_the_max(items_list):
    # sets the maximum to negative infinity, so anything else will become the max
    maximum = float("-inf")
    for item in items_list:
        if item > maximum:
            maximum = item

    return maximum

# https://www.baeldung.com/cs/space-complexity

# Space complexity measures the total amount of memory that an algorithm or operation needs to run according to its input size.

# Big-O notation describes an asymptotic upper bound. It represents the algorithm’s scalability and performance.

# Simply put, it gives the worst-case scenario of an algorithm’s growth rate. We can say that: “the amount of space this algorithm takes will grow no more quickly than this f(x), but it could grow more slowly.”

# O(1) – constant complexity – takes the same amount of space regardless of the input size
# O(log n) – logarithmic complexity – takes space proportional to the log of the input size
# O(n) – linear complexity – takes space directly proportional to the input size
# O(n log n) – log-linear/quasilinear complexity – also called “linearithmic”, its space complexity grows proportionally to the input size and a logarithmic factor
# O(n^2) – square/polynomial complexity – space complexity grows proportionally to the square of the input size

# Omega Notation – Ω
# Omega notation expresses an asymptotic lower bound.

# So, it gives the best-case scenario of an algorithm’s complexity, opposite to big-O notation. We can say that: “the amount of space this algorithm takes will grow no more slowly than this fix), but it could grow more quickly.”

# Theta Notation – θ
# Theta notation represents a function that is within lower and upper bounds.

# We can say that: “the algorithm’s space takes at least that (lower bound function) amount of space and no more than that (maximum bound function) amount of space”.

# Unfortunately, in algorithmics, space and time are like two separate poles. Increasing speed will most often lead to increased memory consumption and vice-versa.

# On the one side, we have merge sort, which is extremely fast but requires a lot of memory. On the other side, we have bubble sort, a slow algorithm but one that occupies minimal space.

# There are also some balanced ones like in-place heap sort. Its speed and space usage are not the best, but they’re acceptable.


# A great example of optimizing the time complexity of the algorithm at the expense of memory is memoization. It’s a technique used to reduce time complexity of algorithms that frequently call some method with the same input data. Instead of calling the method every time, which might be time-consuming, we store the results, and on each call, we check if there is already a cached result for a given input.

# In computing, memoization or memoisation is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again

# The algorithm’s speed cannot cause a program’s failure. The speed will rely on the computing power of the machine on which it’s executed. In a worst-case scenario, low computing power will force the algorithm to slow down.

# On the other hand, if an algorithm requires more memory than the machine provides, it won’t complete. Most often, it will cause some type of memory-related error.
