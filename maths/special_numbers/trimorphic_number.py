"""
A Trimorphic Number is a number whose cube ends in the same digits as the number itself.
For example, 4^3 = 64, which ends in 4.

Reference: https://en.wikipedia.org/wiki/Automorphic_number#Trimorphic_numbers
"""


def is_trimorphic(number: int) -> bool:
    """
    Checks if a number is a Trimorphic number.

    :param number: The number to check
    :return: True if the number is trimorphic, False otherwise
    :raises ValueError: If the input number is negative

    >>> is_trimorphic(0)
    True
    >>> is_trimorphic(1)
    True
    >>> is_trimorphic(4)
    True
    >>> is_trimorphic(5)
    True
    >>> is_trimorphic(24)
    True
    >>> is_trimorphic(249)
    True
    >>> is_trimorphic(2)
    False
    >>> is_trimorphic(7)
    False
    >>> is_trimorphic(10)
    False
    >>> is_trimorphic(-1)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a non-negative integer
    """
    if number < 0:
        raise ValueError("Input must be a non-negative integer")

    if number == 0:
        return True

    cube = number**3
    return str(cube).endswith(str(number))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
