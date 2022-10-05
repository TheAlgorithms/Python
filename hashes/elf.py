def elf_hash(data):
    """
    Implementation of ElfHash Algorithm, a variant of PJW hash function.

    Returns:
        [int] -- [32 bit binary int]
    >>> elf_hash('lorem ipsum')
    '253956621'
    """
    hash = x = i = 0
    for i in range(len(data)):
        hash = (hash << 4) + ord(data[i])
        x = hash & 0xF0000000
        if x != 0:
            hash ^= x >> 24
        hash &= ~x
    return hash

if __name__ == "__main__":
    import doctest

    doctest.testmod()