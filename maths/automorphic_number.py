"""
== Automorphic Numbers ==
A number n is said to be a Automorphic number if
the square of n "ends" in the same digits as n itself.

Examples of Automorphic Numbers: 0, 1, 5, 6, 25, 76, 376, 625, 9376, 90625, ...
https://en.wikipedia.org/wiki/Automorphic_number
"""

# Author : Akshay Dubey (https://github.com/itsAkshayDubey)
# Time Complexity : O(log10n)


def is_automorphic_number(number: int) -> bool:
    """
    # doctest: +NORMALIZE_WHITESPACE
    This functions takes an integer number as input.
    returns True if the number is automorphic.
    >>> is_automorphic_number(-1)
    False
    >>> is_automorphic_number(0)
    True
    >>> is_automorphic_number(5)
    True
    >>> is_automorphic_number(6)
    True
    >>> is_automorphic_number(7)
    False
    >>> is_automorphic_number(25)
    True
    >>> is_automorphic_number(259918212890625)
    True
    >>> is_automorphic_number(259918212890636)
    False
    >>> is_automorphic_number(740081787109376)
    True
    >>> is_automorphic_number(5.0)
    Traceback (most recent call last):
        ...
    TypeError: Input value of [number=5.0] must be an integer
    """
    if not isinstance(number, int):
        msg = f"Input value of [number={number}] must be an integer"
        raise TypeError(msg)
    if number < 0:
        return False
    number_square = number * number
    while number > 0:
        if number % 10 != number_square % 10:
            return False
        number //= 10
        number_square //= 10
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
