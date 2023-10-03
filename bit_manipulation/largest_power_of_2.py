def largest_power_of_2(number: int) -> int:
    """
    returns the largest power of 2 that is less than
    or equal to the given number
    The way this works is that we shift the binary form of the number
    to the right until we reach the last set bit
    Using the number of times we had to shift to find the last set bit,
    we find the 2**(no of times shifted) which will be the ans
    >>> largest_power_of_2(0)
    0
    >>> largest_power_of_2(1)
    1
    >>> largest_power_of_2(3)
    2
    >>> largest_power_of_2(15)
    8
    >>> largest_power_of_2(99)
    64
    >>> largest_power_of_2(178)
    128
    >>> largest_power_of_2(999999)
    524288

    """
    if number==0:
        return 0
    else:
        last_set_bit = 0
        while number:
            last_set_bit += 1
            number >>= 1
        return 2**(last_set_bit - 1)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
