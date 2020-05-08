def fnv1(key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        FNV_offset_basis = 0xcbf29ce484222325
        FNV_prime = 0x100000001b3
        hash = FNV_offset_basis
        max = 2**64
        listOfBytes = []
        for char in key:
            listOfBytes.append(int(bin(ord(char)), 2))
            hash = hash ^ int(bin(ord(char)), 2)
            hash = hash * FNV_prime % max
        return hex(hash)

print(fnv1("word"))
print(fnv1("wordd"))

def hash_index(key):
    return int(fnv1(key), 16) % (2**64)

print(hash_index("hello"))