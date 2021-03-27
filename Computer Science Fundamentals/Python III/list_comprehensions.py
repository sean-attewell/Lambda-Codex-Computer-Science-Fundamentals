# With a list comprehension, you can create a new list based on another list in a single, highly readable line.

# The format of a list comprehension follows this syntax:

# [<map expression> for <name> in <sequence expression> if <filter expression>]

# More simply put:
# new_list = [expression for member in iterable (if conditional)]
# new_list = [expression (if conditional) for member in iterable]


# If you are using a for loop to map a list onto a new list or filter an existing list, a list comprehension can be a better option.
# Here is an example of replacing a for loop used to map word lengths with a single line with a list comprehension.

import random
sentence = "Every moment is a fresh beginning."
words = sentence.split()
word_lengths = []

# Using a for loop
for word in words:
    word_lengths.append(len(word))

print(words)        # ['Every', 'moment', 'is', 'a', 'fresh', 'beginning.']
print(word_lengths)  # [5, 6, 2, 1, 5, 10]

# Using a list comprehension
word_lengths = [len(word) for word in words]

print(word_lengths)  # [5, 6, 2, 1, 5, 10]


# Here is an example of replacing a for loop used to filter out odd numbers from a list with a list comprehension.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

# Using a for loop
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)  # [2, 4, 6, 8, 10]

# Using a list comprehension
even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)  # [2, 4, 6, 8, 10]


# You can also write a list comprehension that maps and filters simultaneously.
# Let's go back to our sentence example and only track word lengths that are greater than 2.

sentence = "Every moment is a fresh beginning."
words = sentence.split()
word_lengths = []

# Using a for loop
for word in words:
    if len(word) > 2:
        word_lengths.append(len(word))

print(words)        # ['Every', 'moment', 'is', 'a', 'fresh', 'beginning.']
print(word_lengths)  # [5, 6, 5, 10]

# Using a list comprehension
word_lengths = [len(word) for word in words if len(word) > 2]
print(word_lengths)  # [5, 6, 5, 10]


# https://realpython.com/list-comprehension-python/

# Using map() Objects
# map() provides an alternative approach that’s based in functional programming.
# You pass in a function and an iterable, and map() will create an object.
# This object contains the output you would get from running each iterable element through the supplied function.

# As an example, consider a situation in which you need to calculate the price after tax for a list of transactions:

txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08


def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)


final_prices = map(get_price_with_tax, txns)
print(final_prices)  # <map object at 0x016F0A90>
print(list(final_prices))
# [1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]

# Here, you have an iterable txns and a function get_price_with_tax(). You pass both of these arguments to map(), and store the resulting object in final_prices.
# You can easily convert this map object into a list using list().


# List comprehensions
# new_list = [expression for member in iterable]

squares = [i * i for i in range(10)]
print(squares)
# ([0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# expression is the member itself, a call to a method, or any other valid expression that returns a value. In the example above, the expression i * i is the square of the member value.

# member is the object or value in the list or iterable. In the example above, the member value is i.

# iterable is a list, set, sequence, generator, or any other object that can return its elements one at a time. In the example above, the iterable is range(10).
# Because the expression requirement is so flexible, a list comprehension in Python works well in many places where you would use map()

# So rather than final_prices = map(get_price_with_tax, txns) you can do:

txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08

final_prices = [get_price_with_tax(i) for i in txns]
print(final_prices)
# [1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]

# ***The only distinction between this implementation and map() is that the list comprehension in Python returns a list, not a map object.

# List comprehensions are often described as being more Pythonic than loops or map().
# One main benefit of using a list comprehension in Python is that it’s a single tool that you can use in many different situations.
# In addition to standard list creation, list comprehensions can also be used for mapping and filtering. You don’t have to use a different approach for each scenario.
# This is the main reason why list comprehensions are considered Pythonic, as Python embraces simple, powerful tools that you can use in a wide variety of situations.

# List comprehensions are also more declarative than loops, which means they’re easier to read and understand. Loops require you to focus on how the list is created.
# You have to manually create an empty list, loop over the elements, and add each of them to the end of the list.
# With a list comprehension in Python, you can instead focus on what you want to go in the list and trust that Python will take care of how the list construction takes place.


# new_list = [expression for member in iterable (if conditional)]

# Conditionals are important because they allow list comprehensions to filter out unwanted values, which would normally require a call to filter():
# In this code block, the conditional statement filters out any characters in sentence that aren’t a vowel.

sentence = 'the rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']
print(vowels)
# ['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']

# The conditional can test any valid expression. If you need a more complex filter, then you can even move the conditional logic to a separate function:

sentence = 'The rocket, who was named Ted, came back from Mars because he missed his friends.'


def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels
# The function returns true or false, so you can call the function in your list comprehension as the conditional.


consonants = [i for i in sentence if is_consonant(i)]
#['T', 'h', 'r', 'c', 'k', 't', 'w', 'h', 'w', 's', 'n', 'm', 'd', 'T', 'd', 'c', 'm', 'b', 'c', 'k', 'f', 'r', 'm', 'M', 'r', 's', 'b', 'c', 's', 'h', 'm', 's', 's', 'd', 'h', 's', 'f', 'r', 'n', 'd', 's']

# Here, you create a complex filter is_consonant() and pass this function as the conditional statement for your list comprehension. Note that the member value i is also passed as an argument to your function.

# You can place the conditional at the end of the statement for simple filtering, but what if you want to change a member value instead of filtering it out? In this case, it’s useful to place the conditional near the beginning of the expression:

# new_list = [expression (if conditional) for member in iterable]

# With this formula, you can use conditional logic to select from multiple possible output options. For example, if you have a list of prices, then you may want to replace negative prices with 0 and leave the positive values unchanged:

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
print(prices)  # [1.25, 0, 10.22, 3.78, 0, 1.16]

# Here, your expression i contains a conditional statement, if i > 0 else 0. This tells Python to output the value of i if the number is positive, but to change i to 0 if the number is negative

# If this seems overwhelming, then it may be helpful to view the conditional logic as its own function:


def get_price(price):
    return price if price > 0 else 0


prices = [get_price(i) for i in original_prices]
print(prices)  # [1.25, 0, 10.22, 3.78, 0, 1.16]

# Now, your conditional statement is contained within get_price(), and you can use it as part of your list comprehension expression.

# Using Set and Dictionary Comprehensions

# While the list comprehension in Python is a common tool, you can also create set and dictionary comprehensions.
# A set comprehension is almost exactly the same as a list comprehension in Python. The difference is that set comprehensions make sure the output contains no duplicates.
# You can create a set comprehension by using curly braces instead of brackets:

quote = "life, uh, finds a way"
unique_vowels = {i for i in quote if i in 'aeiou'}
print(unique_vowels)  # {'a', 'e', 'u', 'i'}

# Your set comprehension outputs all the unique vowels it found in quote. Unlike lists, sets don’t guarantee that items will be saved in any particular order.
# This is why the first member of the set is a, even though the first vowel in quote is i.

# Dictionary comprehensions are similar, with the additional requirement of defining a key:

squares = {i: i * i for i in range(10)}
print(squares)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# To create the squares dictionary, you use curly braces({}) as well as a key-value pair(i: i * i) in your expression.


# Using the Walrus Operator

# Python 3.8 will introduce the assignment expression, also known as the walrus operator. To understand how you can use it, consider the following example.

# Say you need to make ten requests to an API that will return temperature data. You only want to return results that are greater than 100 degrees Fahrenheit.
# Assume that each request will return different data. In this case, there’s no way to use a list comprehension in Python to solve the problem.
# The formula expression for member in iterable (if conditional) provides no way for the conditional to assign data to a variable that the expression can access.

# The walrus operator solves this problem. It allows you to run an expression while simultaneously assigning the output value to a variable. The following example shows how this is possible, using get_weather_data() to generate fake weather data:


def get_weather_data():
    return random.randrange(90, 110)


# this works, not sure why it's complaining. Maybe linter not upto date with walrus?
hot_temps = [temp for _ in range(20) if (temp:=get_weather_data()) >= 100]

print(hot_temps)  # [107, 102, 109, 104, 107, 109, 108, 101, 104]

# You won’t often need to use the assignment expression inside of a list comprehension in Python, but it’s a useful tool to have at your disposal when necessary.


# When Not to Use a List Comprehension in Python

# Watch Out for Nested Comprehensions
# Comprehensions can be nested to create combinations of lists, dictionaries, and sets within a collection. 
# For example, say a climate laboratory is tracking the high temperature in five different cities for the first week of June. 
# The perfect data structure for storing this data could be a Python list comprehension nested within a dictionary comprehension:

cities = ['Austin', 'Tacoma', 'Topeka', 'Sacramento', 'Charlotte']
temps = {city: [0 for _ in range(7)] for city in cities}
print(temps)
# {
#     'Austin': [0, 0, 0, 0, 0, 0, 0],
#     'Tacoma': [0, 0, 0, 0, 0, 0, 0],
#     'Topeka': [0, 0, 0, 0, 0, 0, 0],
#     'Sacramento': [0, 0, 0, 0, 0, 0, 0],
#     'Charlotte': [0, 0, 0, 0, 0, 0, 0]
# }

# You create the outer collection temps with a dictionary comprehension. The expression is a key-value pair, which contains yet another comprehension. This code will quickly generate a list of data for each city in cities.

# Nested lists are a common way to create matrices, which are often used for mathematical purposes. Take a look at the code block below:

matrix = [[i for i in range(5)] for _ in range(6)]
print(matrix)
# [
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4]
# ]

# The outer list comprehension [... for _ in range(6)] creates six rows, while the inner list comprehension [i for i in range(5)] fills each of these rows with values.

# So far, the purpose of each nested comprehension is pretty intuitive. However, there are other situations, such as flattening nested lists, where the logic arguably makes your code more confusing. Take this example, which uses a nested list comprehension to flatten a matrix:

matrix = [
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2],
]
flat = [num for row in matrix for num in row]
print(flat) # [0, 0, 0, 1, 1, 1, 2, 2, 2]

# The code to flatten the matrix is concise, but it may not be so intuitive to understand how it works. 
# On the other hand, if you were to use for loops to flatten the same matrix, then your code will be much more straightforward:

flat = []
for row in matrix:
    for num in row:
        flat.append(num)
print(flat) # [0, 0, 0, 1, 1, 1, 2, 2, 2]

# Now you can see that the code traverses one row of the matrix at a time, pulling out all the elements in that row before moving on to the next one.

# While the single-line nested list comprehension might seem more Pythonic, what’s most important is to write code that your team can easily understand and modify


# Generators
# https://realpython.com/lessons/python-generators-overview/
# As lists start to get really big and take up a ton of memory, you need a different way to approach the problem of making a long iterable thing.
# Save memory, but the price you pay is in speed.

# Choose Generators for Large Datasets
# A list comprehension in Python works by loading the entire output list into memory. For small or even medium-sized lists, this is generally fine

# sum([i * i for i in range(1000)])
# 332833500
# This may work for a thousand, but your machine may become non-responive if you try for a billion.

# When the size of a list becomes problematic, it’s often helpful to use a generator instead of a list comprehension in Python. 
# A generator doesn’t create a single, large data structure in memory, but instead returns an iterable. 
# Your code can ask for the next value from the iterable as many times as necessary or until you’ve reached the end of your sequence, while only storing a single value at a time.

# If you were to sum the first billion squares with a generator, then your program will likely run for a while, but it shouldn’t cause your computer to freeze (as it would if you ran out of memory). 

# The example below uses a generator:

# sum(i * i for i in range(1000000000))
# 333333332833333333500000000

# You can tell this is a generator because the expression isn’t surrounded by brackets or curly braces. Optionally, generators can be surrounded by parentheses.

# The example above still requires a lot of work, but it performs the operations lazily. Because of lazy evaluation, values are only calculated when they’re explicitly requested. After the generator yields a value (for example, 567 * 567), it can add that value to the running sum, then discard that value and generate the next value (568 * 568). When the sum function requests the next value, the cycle starts over. This process keeps the memory footprint small.


# map() also operates lazily, meaning memory won’t be an issue if you choose to use it in this case:

# sum(map(lambda i: i*i, range(1000000000)))
# pssst this takes ages to run

# 333333332833333333500000000
# It’s up to you whether you prefer the generator expression or map().

import random
import timeit
TAX_RATE = .08
txns = [random.randrange(100) for _ in range(100_000)]

def get_price2(txn):
    return txn * (1 + TAX_RATE)

def get_prices_with_map():
    return list(map(get_price2, txns))

def get_prices_with_comprehension():
    return [get_price2(txn) for txn in txns]

def get_prices_with_loop():
    prices = []
    for txn in txns:
        prices.append(get_price2(txn))
    return prices

print(timeit.timeit(get_prices_with_map, number=100))
# 1.0019186
print(timeit.timeit(get_prices_with_comprehension, number=100))
# 1.1907302
print(timeit.timeit(get_prices_with_loop, number=100))
# 1.5089321999999998

# Here, you define three methods that each use a different approach for creating a list. Then, you tell timeit to run each of those functions 100 times each. timeit returns the total time it took to run those 100 executions.

# As the code demonstrates, the biggest difference is between the loop-based approach and map(), with the loop taking 50% longer to execute. Whether or not this matters depends on the needs of your application.

