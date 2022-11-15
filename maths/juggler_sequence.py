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
    # doctest: +NORMALIZE_WHITESPACE
    >>> juggler_sequence(0)
    Traceback (most recent call last):
        ...
    TypeError: Input value of [number=0] must be greater than 0
    >>> juggler_sequence(1)
    [1]
    >>> juggler_sequence(2)
    [2, 1]
    >>> juggler_sequence(3)
    [3, 5, 11, 36, 6, 2, 1]
    >>> juggler_sequence(5)
    [5, 11, 36, 6, 2, 1]
    >>> juggler_sequence(6.0)
    Traceback (most recent call last):
        ...
    TypeError: Input value of [number=6.0] must be an integer
    >>> juggler_sequence(-1)
    Traceback (most recent call last):
        ...
    TypeError: Input value of [number=-1] must be positive
    """
    if not isinstance(number, int):
        raise TypeError(f"Input value of [number={number}] must be an integer")
    if number < 0:
        raise TypeError(f"Input value of [number={number}] must be positive")
    if number == 0:
        raise TypeError(f"Input value of [number={number}] must be greater than 0")
    sequence = [number]
    while number != 1:
        if number % 2 == 0:
            temp = int(math.floor(math.sqrt(number)))
        else:
            temp = int(
                math.floor(math.sqrt(number) * math.sqrt(number) * math.sqrt(number))
            )
        number = temp
        sequence.append(number)
    return sequence


if __name__ == "__main__":
    import doctest

    doctest.testmod()
