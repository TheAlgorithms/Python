def largest_power_of_2(number: int) -> int:
    """
    returns the largest power of 2 that is less than or equal to the given number
    The way this works is that we shift the binary form of the number to the right until we reach the last set bit
    Using the number of times we had to shift to find the last set bit, we find the 2**(no of times shifted) which will be the ans
    >>> largest_pow_of_two_less_than_or_equal_to_a_number(0)
    0
    >>> largest_pow_of_two_less_than_or_equal_to_a_number(1)
    1
    >>> largest_pow_of_two_less_than_or_equal_to_a_number(-1)
    0
    >>> largest_pow_of_two_less_than_or_equal_to_a_number(3)
    2
    >>> largest_pow_of_two_less_than_or_equal_to_a_number(15)
    8
    >>> largest_pow_of_two_less_than_or_equal_to_a_number(99)
    64
    >>> largest_pow_of_two_less_than_or_equal_to_a_number(178)
    128
    >>> largest_pow_of_two_less_than_or_equal_to_a_number(999999)
    524288

    """

    last_set_bit = 0
    while number:
        last_set_bit += 1
        number >>= 1
    return 2 ** (last_set_bit - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
