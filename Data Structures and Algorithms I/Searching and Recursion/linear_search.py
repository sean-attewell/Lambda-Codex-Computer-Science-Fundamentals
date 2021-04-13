# Imagine that I've chosen a random number from 1 to 20. Then, you must guess the number. 
# One approach would be to start picking at 1 and increment your guess by 1 with each guess. 
# If the computer randomly selected 20, then it would take you 20 guesses to get the correct answer. 
# If the computer guessed 1, then you would have the right answer on your very first guess. 
# On average, you will get the correct answer on the 10th or 11th guess.

# If the collection we are searching through is random and unsorted, linear search is the most efficient way to search through it. 
# Once we have a sorted list, then there are more efficient approaches to use.


def linear_search(arr, target):
    for idx in range(len(arr)):
        if arr[idx] == target:
            return idx
    # if we were able to loop through the entire array, the target is not present
    return -1


def linear_search2(arr, target):
    for idx, _ in enumerate(arr):
        if arr[idx] == target:
            return idx
    # if we were able to loop through the entire array, the target is not present
    return -1

my_arr = [2, 3, 2, 4, 55, 6, 74, 3, 5]

print(linear_search(my_arr, 74)) # 6
print(linear_search2(my_arr, 74)) # 6

# Search backwards:
# Since enumerate() returns a generator and generators can't be reversed, you need to convert it to a list first.

def linear_search3(arr, target):
    for idx, _ in reversed(list(enumerate(arr))):
        # print(_) prints out list in reverse order upto and including target
        if arr[idx] == target:
            return idx
    # if we were able to loop through the entire array, the target is not present
    return -1

print(linear_search3(my_arr, 74)) # 6


# To avoid the confusion: reversed() doesn't modify the list. 
# reversed() doesn't make a copy of the list (otherwise it would require O(N) additional memory). 
# If you need to modify the list use alist.reverse(); 
# if you need a copy of the list in reversed order use alist[::-1]

for item in my_arr[::-1]:
    print(item)
