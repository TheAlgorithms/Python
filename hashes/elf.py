def elf_hash(data: str) -> int:
    """
    Implementation of ElfHash Algorithm, a variant of PJW hash function.

    Returns:
        [int] -- [32 bit binary int]
    >>> elf_hash('lorem ipsum')
    253956621
    """
    hash = x = 0
    for letter in data:
        hash = (hash << 4) + ord(letter)
        x = hash & 0xF0000000
        if x != 0:
            hash ^= x >> 24
        hash &= ~x
    return hash


if __name__ == "__main__":
    import doctest

    doctest.testmod()
