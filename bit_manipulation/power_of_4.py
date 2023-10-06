"""

Task:
Given a positive int number. Return True if this number is power of 4
or False otherwise.

Implementation notes: Use bit manipulation.
For example if the number is the power of 2 it's bits representation:
n     = 0..100..00
n - 1 = 0..011..11

n & (n - 1) - no intersections = 0
If the number is a power of 4 then it should be a power of 2
and the set bit should be at an odd position.
"""


def power_of_4(number: int) -> bool:
    """
    Return True if this number is power of 4 or False otherwise.

    >>> power_of_4(0)
    Traceback (most recent call last):
        ...
    ValueError: number must be positive
    >>> power_of_4(1)
    True
    >>> power_of_4(2)
    False
    >>> power_of_4(4)
    True
    >>> power_of_4(6)
    False
    >>> power_of_4(8)
    False
    >>> power_of_4(17)
    False
    >>> power_of_4(64)
    True
    >>> power_of_4(-1)
    Traceback (most recent call last):
        ...
    ValueError: number must be positive
    >>> power_of_4(1.2)
    Traceback (most recent call last):
        ...
    TypeError: number must be an integer

    """
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    if number <= 0:
        raise ValueError("number must be positive")
    if number & (number - 1) == 0:
        c = 0
        while number:
            c += 1
            number >>= 1
        return c % 2 == 1
    else:
        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
