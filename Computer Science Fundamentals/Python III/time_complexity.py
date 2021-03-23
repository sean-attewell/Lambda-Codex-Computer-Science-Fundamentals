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
# O(log n)	As the input size increases, the runtime will grow slightly slower. logarithmic growth.
# O(n) means the number of operations grows at the same rate as the input size. Linear growth.
# O(n^c)	As the input size increases, the runtime will grow at a faster rate. Polynomial.
# O(c^n) As the input size increases, the runtime will grow at a much faster rate. Expontential.
