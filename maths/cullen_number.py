"""
Cullen Number:
In mathematics, a Cullen number is a natural number of the form:
    C_n = n * 2^n + 1
for any integer n >= 1.

The first few Cullen numbers are:
    3, 9, 25, 65, 161, 385, 897, 2049, 4609, 10241, ...

Reference:
    https://en.wikipedia.org/wiki/Cullen_number
    https://oeis.org/A005849
"""


def cullen_number(index: int) -> int:
    """
    Returns the index-th Cullen number: index * 2^index + 1.

    >>> cullen_number(1)
    3
    >>> cullen_number(2)
    9
    >>> cullen_number(3)
    25
    >>> cullen_number(5)
    161
    >>> cullen_number(10)
    10241
    >>> cullen_number(0)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a positive integer (index >= 1).
    >>> cullen_number(-3)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a positive integer (index >= 1).
    >>> cullen_number(2.5)  # type: ignore
    Traceback (most recent call last):
        ...
    TypeError: Input must be an integer.
    """
    if not isinstance(index, int):
        raise TypeError("Input must be an integer.")
    if index < 1:
        raise ValueError("Input must be a positive integer (index >= 1).")
    return index * (1 << index) + 1


def is_cullen_number(number: int) -> bool:
    """
    Checks whether a given positive integer is a Cullen number.

    >>> is_cullen_number(3)
    True
    >>> is_cullen_number(9)
    True
    >>> is_cullen_number(25)
    True
    >>> is_cullen_number(161)
    True
    >>> is_cullen_number(10241)
    True
    >>> is_cullen_number(10)
    False
    >>> is_cullen_number(1)
    False
    >>> is_cullen_number(-5)
    False
    >>> is_cullen_number(0)
    False
    >>> is_cullen_number(3.0)  # type: ignore
    Traceback (most recent call last):
        ...
    TypeError: Input must be an integer.
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    if number < 3:
        return False

    current_index = 1
    while True:
        cullen = cullen_number(current_index)
        if cullen == number:
            return True
        if cullen > number:
            return False
        current_index += 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
