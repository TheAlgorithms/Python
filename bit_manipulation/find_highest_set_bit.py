from typing import Optional

def find_highest_set_bit(num: int) -> Optional[int]:
    """
    Find Highest Set Bit
    This function calculates the position (or index)
    of the most significant bit being set to 1 in a given integer.

    Parameters:
    num (int): The input integer to find the highest set bit.

    Returns:
    Optional[int]: The position of the highest set bit, if found; otherwise, returns None.

    Raises:
    ValueError: If the input is negative.

    Examples:
    >>> find_highest_set_bit(10)
    3
    >>> find_highest_set_bit(16)
    4
    >>> find_highest_set_bit(0)
    None
    >>> find_highest_set_bit(-1)
    Traceback (most recent call last):
        ...
    ValueError: Input cannot be negative
    """

    if num < 0:
        raise ValueError("Input cannot be negative")

    if num == 0:
        return None

    position = 0
    while num > 0:
        num >>= 1
        position += 1

    return position - 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
