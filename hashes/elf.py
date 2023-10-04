def elf_hash(data: str) -> int:
    """
    Implementation of ElfHash Algorithm, a variant of PJW hash function.

    >>> elf_hash('lorem ipsum')
    253956621
    """
    hash_ = x = 0
    for letter in data:
        hash_ = (hash_ << 4) + ord(letter)
        x = hash_ & 0xF0000000
        if x != 0:
            hash_ ^= x >> 24
        hash_ &= ~x
    return hash_


if __name__ == "__main__":
    import doctest

    doctest.testmod()
