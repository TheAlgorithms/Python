"""
== Pronic Number ==
A number n is said to be a Proic number if
there exists an integer m such that n = m * (m + 1)

Examples of Proic Numbers: 0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110 ...
https://en.wikipedia.org/wiki/Pronic_number
"""

# Author : Akshay Dubey (https://github.com/itsAkshayDubey)


def is_pronic(number: int) -> bool:
    """
    # doctest: +NORMALIZE_WHITESPACE
    This functions takes an integer number as input.
    returns True if the number is pronic.
    >>> is_pronic(-1)
    False
    >>> is_pronic(0)
    True
    >>> is_pronic(2)
    True
    >>> is_pronic(5)
    False
    >>> is_pronic(6)
    True
    >>> is_pronic(8)
    False
    >>> is_pronic(30)
    True
    >>> is_pronic(32)
    False
    >>> is_pronic(2147441940)
    True
    >>> is_pronic(9223372033963249500)
    True
    >>> is_pronic(6.0)
    Traceback (most recent call last):
        ...
    TypeError: Input value of [number=6.0] must be an integer
    """
    if not isinstance(number, int):
        raise TypeError(f"Input value of [number={number}] must be an integer")
    if number < 0 or number % 2 == 1:
        return False
    number_sqrt = int(number**0.5)
    return number == number_sqrt * (number_sqrt + 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
