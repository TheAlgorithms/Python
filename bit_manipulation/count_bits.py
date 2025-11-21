def count_bits(n: int) -> int:
    """
    Count the number of set bits (1s) in the binary representation of a
    non-negative integer.

    Examples:
    >>> count_bits(0)
    0
    >>> count_bits(1)
    1
    >>> count_bits(5)  # 101
    2
    >>> count_bits(15)  # 1111
    4
    >>> count_bits(16)  # 10000
    1
    """
    if n < 0:
        raise ValueError("Input must be non-negative")

    count = 0
    while n > 0:
        count += n & 1
        n >>= 1

    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()
