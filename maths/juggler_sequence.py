"""
== Juggler Sequence ==
Juggler sequence start with any positive integer n. The next term is
obtained as follows:
    If n term is even, the next term is floor value of square root of n .
    If n is odd, the next term is floor value of 3 time the square root of n.

https://en.wikipedia.org/wiki/Juggler_sequence
"""

# Author : Akshay Dubey (https://github.com/itsAkshayDubey)
import math


def juggler_sequence(number: int) -> list[int]:
    """
    >>> juggler_sequence(0)
    Traceback (most recent call last):
        ...
    ValueError: Input value of [number=0] must be a positive integer
    >>> juggler_sequence(1)
    [1]
    >>> juggler_sequence(2)
    [2, 1]
    >>> juggler_sequence(3)
    [3, 5, 11, 36, 6, 2, 1]
    >>> juggler_sequence(5)
    [5, 11, 36, 6, 2, 1]
    >>> juggler_sequence(10)
    [10, 3, 5, 11, 36, 6, 2, 1]
    >>> juggler_sequence(25)
    [25, 125, 1397, 52214, 228, 15, 58, 7, 18, 4, 2, 1]
    >>> juggler_sequence(6.0)
    Traceback (most recent call last):
        ...
    TypeError: Input value of [number=6.0] must be an integer
    >>> juggler_sequence(-1)
    Traceback (most recent call last):
        ...
    ValueError: Input value of [number=-1] must be a positive integer
    """
    if not isinstance(number, int):
        msg = f"Input value of [number={number}] must be an integer"
        raise TypeError(msg)
    if number < 1:
        msg = f"Input value of [number={number}] must be a positive integer"
        raise ValueError(msg)
    sequence = [number]
    while number != 1:
        if number % 2 == 0:
            number = math.floor(math.sqrt(number))
        else:
            number = math.floor(
                math.sqrt(number) * math.sqrt(number) * math.sqrt(number)
            )
        sequence.append(number)
    return sequence


if __name__ == "__main__":
    import doctest

    doctest.testmod()
