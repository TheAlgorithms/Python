def get_highest_set_bit_position(number: int) -> int:
    """
    Returns position of the highest set bit of a number.
    Ref - https://graphics.stanford.edu/~seander/bithacks.html#IntegerLogObvious
    Finds the position (1-indexed) of the highest (most significant) set bit.
    The position is counted from the right starting at 1.
    Algorithm:
    1. Initialize position counter to 0
    2. While number > 0:
       a. Increment position
       b. Right-shift number by 1 bit (number >>= 1)
    3. Return the final position
    Example: 25 = 0b11001
    - Iteration 1: position = 1, number = 0b1100 (12)
    - Iteration 2: position = 2, number = 0b110 (6)
    - Iteration 3: position = 3, number = 0b11 (3)
    - Iteration 4: position = 4, number = 0b1 (1)
    - Iteration 5: position = 5, number = 0b0 (0)
    - Returns 5 (the highest set bit is at position 5)
    >>> get_highest_set_bit_position(25)
    5
    >>> get_highest_set_bit_position(37)
    6
    >>> get_highest_set_bit_position(1)
    1
    >>> get_highest_set_bit_position(4)
    3
    >>> get_highest_set_bit_position(0)
    0
    >>> get_highest_set_bit_position(0.8)
    Traceback (most recent call last):
        ...
    TypeError: Input value must be an 'int' type
    """
    if not isinstance(number, int):
        raise TypeError("Input value must be an 'int' type")

    position = 0
    while number:
        position += 1
        number >>= 1

    return position


if __name__ == "__main__":
    import doctest

    doctest.testmod()
