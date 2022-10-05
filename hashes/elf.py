def ELFHash(data):
    """
    Implementation of ElfHash Algorithm, a variant of PJW hash function.
    """
    hash = x = i = 0
    for i in range(len(data)):
        hash = (hash << 4) + ord(data[i])
        x = hash & 0xF0000000
        if x != 0:
            hash ^= (x >> 24)
        hash &= ~x
    return hash