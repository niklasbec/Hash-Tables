class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value, capacity=10):
        self.key = key
        self.value = value
        self.next = None
        self.capacity = capacity

class HashTable:

    def __init__(self, capacity, ):
        self.capacity = capacity
        self.storage = [None] * capacity
    
    def fnv1(self, key):
        FNV_offset_basis = 0xcbf29ce484222325
        FNV_prime = 0x100000001b3
        hash = FNV_offset_basis
        max = 2**64
        for char in key:
            hash = hash ^ ord(char)
            hash = hash * FNV_prime % max
        return hex(hash)

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return int(self.fnv1(key), 16) % self.capacity
    

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index]:
            curr = self.storage[index]
            while curr:
                if curr.key == key:
                    curr.value = value
                    return
                if curr.next == None:
                    curr.next = HashTableEntry(key, value)
                    return
                curr = curr.next

            curr.next = HashTableEntry(key, value)
        else:
            self.storage[index] = HashTableEntry(key, value)


    def delete(self, key):
        hashIndex = self.hash_index(key)
        
        #check if single value then delete
        if self.storage[hashIndex].next == None:
            if self.storage[hashIndex].key == key:
                self.storage[hashIndex] = None
            else:
                errorMessage = "WARNING -- KEY NOT FOUND"
                print(errorMessage)
        else:
            if self.storage[hashIndex].key == key:
                self.storage[hashIndex] = None
            else:
                self.storage[hashIndex].next = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index]:
            if self.storage[index].next:
                curr = self.storage[index]
                while curr.key != key:
                    curr = curr.next
                return curr.value
            else:
                return self.storage[index].value
        return None

    def resize(self):
        self.capacity = self.capacity * 2
        newList = self.capacity * [None]

        for a, b in enumerate(self.storage):
            while b:
                hashIndex = self.hash_index(b.key)
                if newList[hashIndex]:
                    curr = newList[hashIndex]
                    while curr.next:
                        curr = curr.next
                    curr.next = HashTableEntry(b.key, b.value)
                else:
                    newList[hashIndex] = HashTableEntry(b.key, b.value)
                b = b.next
        self.storage = newList


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
