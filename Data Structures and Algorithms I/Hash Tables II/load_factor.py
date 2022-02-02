# The performance of hash tables for search, insertion, and deletion is constant time (O(1)) in the average case. 
# However, as the chains get longer and longer, in the worst case, those same operations are done in linear time (O(n)).
# The more collisions that your hash table has, the less performant the hash table is. 
# **To avoid collisions, a proper hash function and maintaining a low load factor is crucial**. What is a load factor?

# Load Factor
# The load factor of a hash table is trivial to calculate. 
# You take the number of items stored in the hash table divided by the number of slots.
# (number of items can be more than slots as linked lists get longer, so load factor can go above 1)


# Hash tables use an array for storage. So, the load factor is the number of occupied slots divided by the length of the array. 
# So, an array of length 10 with three items in it has a load factor of 0.3, and an array of length 20 with twenty items has a load factor of 1. 
# If you use linear probing for collision resolution, then the maximum load factor is 1. 
# If you use chaining for collision resolution, then the load factor can be greater than 1.

# As the load factor of your hash table increases, so does the likelihood of a collision, which reduces your hash table's performance. 
# Therefore, you need to monitor the load factor and resize your hash table when the load factor gets too large. 
# The general rule of thumb is to resize your hash table when your load factor is greater than 0.7. 
# Also, when you resize, it is common to double the size of the hash table. 
# NOTE: This is similar to how a dynamic array will double in size
# When you resize the array, you need to re-insert all of the items into this new hash table. 
# You cannot simply copy the old items into the new hash table.
# Each item has to be rerun through the hashing function because the hashing function considers the size of the hash table when determining the index that it returns.
# e.g. the hash_index method uses the capacity
# return self.djb2(key) % self.capacity

# You can see that resizing is an expensive operation, so you don’t want to resize too often. 
# However, when we average it out, hash tables are constant time (O(1)) even with resizing.

# The load factor can also be too small. If the hash table is too large for the data that it is storing, then memory is being wasted. 
# So, in addition to resizing, when the load factor gets too high, you should also resize when the load factor gets too low.

# One way to know when to resize your hash table is to compute the load factor whenever an item is inserted or deleted into the hash table. 
# If the load factor is too high or too low, then you need to resize.


# We added a get_load_factor and resize method to calculate the load factor and resize the hash table with a new capacity when necessary.

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.item_count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        return self.item_count / self.capacity

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # If the load factor is over 0.7 after a put
        # the put method calls self.resize(self.capacity * 2)
        # This doubles the capacity 

        old_storage = self.storage
        self.capacity = new_capacity
        self.storage = [None] * self.capacity

        # Save this because put adds to it, and we don't want that.
        # It might be less hackish to pass a flag to put indicating that
        # we're in a resize and don't want to modify item count.
        old_item_count = self.item_count

        current_entry = None

        for bucket_item in old_storage:
            current_entry = bucket_item
            while current_entry is not None:
                self.put(current_entry.key, current_entry.value)
                current_entry = current_entry.next

        # Restore this to the correct number
        self.item_count = old_item_count

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        str_key = str(key).encode()

        FNV_offset_basis_64 = 10 # placeholder because undefined variable
        hash = FNV_offset_basis_64

        FNV_prime_64 = 10  # placeholder because undefined variable
        for b in str_key:
            hash *= FNV_prime_64
            hash ^= b
            hash &= 0xffffffffffffffff  # 64-bit hash

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        within the hash table's storage capacity.
        """
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        index = self.hash_index(key)

        current_entry = self.storage[index]

        while current_entry is not None and current_entry.key != key:
            current_entry = current_entry.next

        if current_entry is not None:
            current_entry.value = value
        else:
            new_entry = HashTableEntry(key, value)
            new_entry.next = self.storage[index]
            self.storage[index] = new_entry

            self.item_count += 1

            if self.get_load_factor() > 0.7:
                self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
