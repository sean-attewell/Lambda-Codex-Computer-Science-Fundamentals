# Hash tables are also called hash maps, maps, unordered maps, or dictionaries. 
# A hash table is a structure that maps keys to values. This makes them extremely efficient for lookups because if you have the key, retrieving the associated value is a constant-time operation.


# Time and Space Complexity

# Lookup
# Hash tables have fast lookups (O(1)) on average. However, in the worst case, they have slow (O(n)) lookups. The slow lookups happen when there is a hash collision (two different keys hash to the same index).

# Insert
# Hash tables have fast insertions (O(1)) on average. However, in the worst case, they have slow (O(n)) insertions. Just like with the lookups, the worst case occurs due to hash collisions.

# Delete
# Hash tables have fast deletes (O(1)) on average. However, in the worst case, they have slow (O(n)) deletions. Just like with lookups and insertions, the worst case occurs due to hash collisions.

# Space
# The space complexity of a hash table is linear (O(n)). Each key-value pair in the hash table will take up space in memory.

# Strengths
# The main reason why hash tables are great is that they have constant-time (O(1)) lookup operations in the average case. That makes them great to use in any situation where you will be conducting many lookup operations. 
# The second reason they are great is that they allow you to use any hashable object as a key. This means they can be used in many different scenarios where you want to map one object (the key) to another object (the value).

# Weaknesses
# One weakness of the hash table is that the mapping goes only one way. So, if you know the key, it's incredibly efficient to retrieve the mapped value to that key. However, if you know the value and want to find the key that is mapped to that value, it is inefficient. 
# Another weakness is that if your hash function produces lots of collisions, the hash table's time complexity gets worse and worse. This is because the underlying linked lists are inefficient for lookups.

# What About Hash Collisions?
# A hash collision is when our hash function returns the same index given two different keys. Theoretically, there is no perfect hash function, though some are better than others. Thus, any hash table implementation has to have a strategy to deal with the scenario when two different keys hash to the same index. You can't just have the hash table overwrite the already existing value.

# The most common strategy for dealing with hash collisions is not storing the values directly at an index of the hash table's array. Instead, the array index stores a pointer to a linked list. Each node in the linked list stores a key, value, and a pointer to the next item in the linked list.

# The above is just one of the ways to deal with hash collisions. Hopefully, you can now see why all of our hash table operations become O(n) in the worst case. What is the worst case? 
# The worst case is when all of the keys collide at the same index in our hash table. If we have ten items in our hash table, all ten items are stored in one linked list at the same index of our array. That means that our hash table has the same efficiency as a linked list in the worst case.

# https://www.geeksforgeeks.org/hashing-data-structure/
# Hashing is a technique or process of mapping keys, values into the hash table by using a hash function. It is done for faster access to elements. The efficiency of mapping depends on the efficiency of the hash function used.


# Hashing functions take an input (usually a string) and return an integer as the output
# So, hash functions convert the strings into indexes, and then we store the given string into the computed index of an array.
# Hash Function + Array = Hash Table

# To convert a string into an integer, hashing functions operate on the individual characters that make up the string.

# In Python, we can encode strings into their bytes representation with the .encode() method (read more here). Once encoded, an integer represents each character.
# Let's do this with the string hello

bytes_representation = "hello".encode()
print(bytes_representation) # b'hello' 

for byte in bytes_representation:
    print(byte)

### Print Output
### 104
### 101
### 108
### 108
### 111

# Now that we’ve converted our string into a series of integers, we can manipulate those integers somehow. For simplicity’s sake, we can use a simple accumulator pattern to get a sum of all the integer values.

sum = 0
for byte in bytes_representation:
    sum += byte

print(sum)

### Print Output
### 532

# Great! We turned a string into a number. Now, let's generalize this into a function.

def my_hashing_func(str):
    bytes_representation = str.encode()

    sum = 0
    for byte in bytes_representation:
        sum += byte

    return sum

# We aren't done yet 🤪. As shown earlier, hello returns 532. But, what if our hash table only has ten slots? We have to make 532 a number less than 10 😱.

# Remember the modulo operator %? We can use that in our hashing function to ensure that the integer the function returns is within a specific range.

def my_hashing_func2(str, table_size):
    bytes_representation = str.encode()

    sum = 0
    for byte in bytes_representation:
        sum += byte

    return sum % table_size

print(my_hashing_func2('hello', 10))
# the sum is 532, if you modulo by 10 you'll return the remainder 2 to use as the index for where to store 'hello' in the array.

# https://zetcode.com/python/hashing/

# Python uses hash tables for dictionaries and sets. A hash table is an unordered collection of key-value pairs, where each key is unique. 
# Hash tables offer a combination of efficient lookup, insert and delete operations. These are the best properties of arrays and linked lists.

# Hashing is the process of using an algorithm to map data of any size to a fixed length. This is called a hash value. 
# Hashing is used to create high performance, direct access data structures where large amount of data is to be stored and accessed quickly. 
# Hash values are computed with hash functions.

# Python hashable
# An object is hashable if it has a hash value which never changes during its lifetime. (It can have different values during multiple invocations of Python programs.) 
# ^ perhaps because if it's based on an id for some things (like instances of user-defined classes), then is stored in a different palce in memory next time.
# A hashable object needs a __hash__() method. In order to perform comparisons, a hashable needs an __eq__() method.
# Note: Hashable objects which compare equal must have the same hash value.

# Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally. 
# Python immutable built-in objects are hashable; mutable containers (such as lists or dictionaries) are not. 
# Objects which are instances of user-defined classes are hashable by default. 
# They all compare unequal (except with themselves), and their hash value is derived from their id().

# Note: If a class does not define an __eq__() method it should not define a __hash__() operation either; 
# if it defines __eq__() but not __hash__(), its instances will not be usable as items in hashable collections.

# Python hash() function
# The hash() function returns the hash value of the object if it has one. Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup. Objects can implement the __hash__() method.

# Python immutable builtins are hashable
# Python immutable builtins, such as integers, strings, or tuples, are hashable.

val = 100

print(val.__hash__()) # 100
print("falcon".__hash__()) # 7231380644105876859
print((1,).__hash__()) # -6644214454873602895

# The example prints the values of three hashables: an integer, a string, and a tuple.


# Python custom objects are hashable by default. Their hash is derived from their Id.

class User:

    def __init__(self, name, occupation):

        self.name = name
        self.occupation = occupation

u1 = User('John Doe', 'gardener')
u2 = User('John Doe', 'gardener')

print('hash of user 1')
print(hash(u1)) # 132860208890

print('hash of user 2')
print(hash(u2)) # 132860208884

if (u1 == u2):
    print('same user')
else:
    print('different users')

# The hash() function returns the hash value of the object. The default implementation is derived from the Id of the object.
# Even though the user details are the same, the comparison yields differet objects. 
# In order to change it, we need to implement the __eq__() method.

class User_2:

    def __init__(self, name, occupation):

        self.name = name
        self.occupation = occupation

    def __eq__(self, other):
      # A backslash at the end of a line tells Python to extend the current logical line over across to the next physical line.
        return self.name == other.name \
            and self.occupation == other.occupation

    def __str__(self):
        return f'{self.name} {self.occupation}'


u1 = User_2('John Doe', 'gardener')
u2 = User_2('John Doe', 'gardener')

if (u1 == u2):
    print('same user')
    print(f'{u1} == {u2}') # prints __str__ method
else:
    print('different users')

# Now the comparison returns the expected output for us - that they are equal

# users = {u1, u2}
# # print(len(users))
# ^ however, we cannot insert the objects into a Python set; 
# it would result in TypeError: unhashable type: 'User'. 
# In order to change this, we implement the __hash__() method.

# In the third example, we implement the __eq__() and the __hash__() methods.

class User_3:

    def __init__(self, name, occupation):

        self.name = name
        self.occupation = occupation

    def __eq__(self, other):

        return self.name == other.name \
            and self.occupation == other.occupation

    def __hash__(self):
        return hash((self.name, self.occupation)) # This is a tuple you're hashing.
        # The implementation of the __hash__() function returns a hash value computed with the hash() function from a tuple of attributes.
        # Makes sense that it contains only name and occupation, since if they match the __eq__ method says they're equal.

    def __str__(self):
        return f'{self.name} {self.occupation}'

print('-------User_3----------')

u1 = User_3('John Doe', 'gardener')
u2 = User_3('John Doe', 'gardener')

users = {u1, u2}

print(len(users)) # 1 because sets don't allow duplicate values (duplicate values will be ignored)

if (u1 == u2):
    print('same user') # this runs
    print(f'{u1} == {u2}')
else:
    print('different users')

print('------------------------------------')

u1.occupation = 'programmer'

users = {u1, u2} 

print(len(users)) # 2

if (u1 == u2):
    print('same user')
    print(f'{u1} == {u2}')
else:
    print('different users') # this runs


print('-------User_3----------')


from dataclasses import dataclass

@dataclass(frozen=True)
class User_4:

    name: str
    occupation: str


u1 = User_4('John Doe', 'gardener')
u2 = User_4('John Doe', 'gardener')

if (u1 == u2):
    print('same user') # this runs
    print(f'{u1} == {u2}')
else:
    print('different users')

users = {u1, u2}
print(len(users)) # 1

# The dataclass decorator has a frozen argument (False by default). If specified, the fields will be frozen (i.e. read-only). 
# If eq is set to True, which it is by default then the __hash__() method is implemented and object instances will be hashable.


# Below is a simple HashTable class implementation that does not handle collisions

class HashTable:
    """
    A hash table with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.item_count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        """
        return len(self.storage)

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        """
        # Cast the key to a string and get bytes
        str_key = str(key).encode()

        # Start from an arbitrary large prime
        hash_value = 5381

        # Bit-shift and sum value for each character
        for b in str_key:
            hash_value = ((hash_value << 5) + hash_value) + b

            # https://stackoverflow.com/questions/22832615/what-do-and-mean-in-python
            # x << y
            # Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.

            hash_value &= 0xffffffff  # DJB2 is a 32-bit hash, only keep 32 bits

            # the "binary AND", (akin to intersection) of the binary numbers 1110 and 1011 is 1010
            # I guess since they're all maxed out at f, it keeps the hash_value as it is, but gives it the desired length.

        return hash_value

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index within the hash table's storage capacity.
        """
        return self.djb2(key) % self.capacity


    def put(self, key, value):
        """
        Store the value with the given key.
        """
        index = self.hash_index(key)
        self.storage[index] = value
        return


    def delete(self, key):
        """
        Remove the value stored with the given key.
        """
        index = self.hash_index(key)
        self.storage[index] = None


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        """
        index = self.hash_index(key)
        return self.storage[index]
