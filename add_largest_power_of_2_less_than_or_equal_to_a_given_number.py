"""
Fixes #9347
Name : Sharnabh Banerjee

"""


def add_largest(num: int) -> int:
    """
    Add Largest Power of 2 less then or equal to a given number
    >>> add_largest(5.3)
    Traceback (most recent call last):
        ...
    TypeError: num must be an integer !!
    >>> add_largest(5)
    9
    >>> add_largest(10)
    18
    >>> add_largest(99)
    163
    >>> add_largest(-10)
    0
    >>> add_largest(999)
    1511

    """

    """Checks if Float or not"""
    if isinstance(num, float):
        raise TypeError("num must be an integer !!")
    """Checks if negative or Zero"""
    if num <= 0:
        return 0
    res = 1
    """Left Bit Shift till it res is less than or equal to the given number"""
    while (res << 1) <= num:
        res <<= 1
    
    """Return the Final Result"""
    return res + num


if __name__ == "__main__":
    import doctest

    doctest.testmod()
