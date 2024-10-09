def elf_hash(veri: str) -> int:
    """
    ElfHash Algoritmasının uygulanması, PJW hash fonksiyonunun bir varyantı.

    >>> elf_hash('lorem ipsum')
    253956621
    """
    hash_ = x = 0
    for harf in veri:
        hash_ = (hash_ << 4) + ord(harf)
        x = hash_ & 0xF0000000
        if x != 0:
            hash_ ^= x >> 24
        hash_ &= ~x
    return hash_


if __name__ == "__main__":
    import doctest

    doctest.testmod()
