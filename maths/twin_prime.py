"""
== Twin Prime ==
A number n+2 is said to be a Twin prime of number n if
both n and n+2 are prime.

Examples of Twin pairs: (3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), ...
https://en.wikipedia.org/wiki/Twin_prime
"""

# Author : Akshay Dubey (https://github.com/itsAkshayDubey)
from maths.prime_check import is_prime


def twin_prime(number: int) -> int:
    """
    # doctest: +NORMALIZE_WHITESPACE
    This functions takes an integer number as input.
    returns n+2 if n and n+2 are prime numbers and -1 otherwise.
    >>> twin_prime(3)
    5
    >>> twin_prime(4)
    -1
    >>> twin_prime(5)
    7
    >>> twin_prime(17)
    19
    >>> twin_prime(0)
    -1
    >>> twin_prime(6.0)
    Traceback (most recent call last):
        ...
    TypeError: Input value of [number=6.0] must be an integer
    """
    if not isinstance(number, int):
        msg = f"Input value of [number={number}] must be an integer"
        raise TypeError(msg)
    if is_prime(number) and is_prime(number + 2):
        return number + 2
    else:
        return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
