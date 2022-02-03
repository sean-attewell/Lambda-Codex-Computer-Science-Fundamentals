# For finding and item in an unsorted array you may be stuck with linear search, which takes linear time O(n)
# If the array is sorted, you can use binary search (halving the number of possibilities with each guess), which takes O(log n)
# This is much more efficient

def binary_search(array, target):
    # 1. Declare min = 0 and max = length of array - 1
    min = 0
    max = len(array) - 1
    while not max < min:
        # 2. Figure out the guess value by getting the middle integer between min and max
        guess = (max + min) // 2
        # 3. if array[guess] equals the target, we found the element, return the index
        if array[guess] == target:
            return guess
        # 4. if the guess was too low, reset min to be one more than the guess
        elif array[guess] < target:
            min = guess + 1
        # 5. if the guess was too high, reset max to be one less than the guess
        else:
            max = guess - 1
    # no match was found
    return -1


my_arr = [0, 2, 55, 234, 334, 666, 733, 2002]

print(binary_search(my_arr, 733)) # 6