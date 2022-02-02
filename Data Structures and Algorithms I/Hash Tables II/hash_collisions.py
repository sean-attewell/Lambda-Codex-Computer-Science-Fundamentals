# Remember when we wondered what would happen if multiple keys hashed to the same index, and we said that we would worry about it later? Whelp, it's later 🤪.

# Let's say we were given the key-value pair ("Ryan", 10). Our hash code then maps "Ryan" to index 3. Excellent, that works!
# Now let's say after we inserted ("Ryan", 10), we have to insert ("Parth", 12). Our hash code maps "Parth" to index 3. Uh oh! Ryan is already there! What do we do?? 😱

# Ok, let's stop freaking out, and let's think about this. If we don't do anything, the value stored at index 3 will just get overwritten. Meaning if we try to retrieve the value associated with "Ryan", 12 will be returned instead of 10. That might not seem like a big deal, but what if we were returning passwords based on a user ID, and we returned someone else's password. That would be horrible.

# Let's fix this problem. The most common way to solve this is with linked list chaining. If we see multiple values hashed to an index, we will chain them in a linked list.


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

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
        Return the length of the list you're using to hold the hash table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here
        return len(self.storage)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """

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
        Take an arbitrary key and return a valid integer index between within the hash table's storage capacity.
        """
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        index = self.hash_index(key)

        current_entry = self.storage[index] # get first entry at index (the head)

        # Work through the chain
        # Remember it's the index that's the same, not the key
        while current_entry is not None and current_entry.key != key:
              current_entry = current_entry.next

        # Reached entry with the same key, replace value
        if current_entry is not None:
            current_entry.value = value

        # Reached end of linked list, pre-pend new entry to head    
        else:
            new_entry = HashTableEntry(key, value)
            new_entry.next = self.storage[index] # point at old head
            self.storage[index] = new_entry # replace old head             

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