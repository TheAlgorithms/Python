"""
The Bob Jenkins hash is a fast, non-cryptographic hash function
designed for general-purpose use, such as hash table lookups.

source: https://en.wikipedia.org/wiki/Jenkins_hash_function
"""

def joaat(key: str) -> int:
    """
    Calculate Jenkins One-at-a-Time hash for a key.
    
    >>> joaat("apple")
    2297466611
    >>> joaat("test")
    1064684737
    >>> joaat("")
    0
    """
    hash = 0
    mask = 0xFFFFFFFF
    key_bytes = key.encode("utf-8")
    
    for byte in key_bytes:
        hash = (hash + byte) & mask
        hash = (hash + (hash << 10)) & mask
        hash = (hash ^ (hash >> 6)) & mask
    
    hash = (hash + (hash << 3)) & mask
    hash = (hash ^ (hash >> 11)) & mask
    hash = (hash + (hash << 15)) & mask
    
    return hash

if __name__ == "__main__":
    import doctest
    doctest.testmod()
