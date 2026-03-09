"""
Fast inverse square root (1/sqrt(x)) using the Quake III algorithm.
Reference: https://en.wikipedia.org/wiki/Fast_inverse_square_root
Accuracy: https://en.wikipedia.org/wiki/Fast_inverse_square_root#Accuracy
"""

import struct


def fast_inverse_sqrt(number: float) -> float:
    """
    Compute the fast inverse square root of a floating-point number using the famous
    Quake III algorithm.

    :param float number: Input number for which to calculate the inverse square root.
    :return float: The fast inverse square root of the input number.

    Example:
    >>> fast_inverse_sqrt(10)
    0.3156857923527257
    >>> fast_inverse_sqrt(4)
    0.49915357479239103
    >>> fast_inverse_sqrt(4.1)
    0.4932849504615651
    >>> fast_inverse_sqrt(0)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a positive number.
    >>> fast_inverse_sqrt(-1)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a positive number.
    >>> from math import isclose, sqrt
    >>> all(isclose(fast_inverse_sqrt(i), 1 / sqrt(i), rel_tol=0.00132)
    ...     for i in range(50, 60))
    True
    """
    if number <= 0:
        raise ValueError("Input must be a positive number.")
    i = struct.unpack(">i", struct.pack(">f", number))[0]
    i = 0x5F3759DF - (i >> 1)
    y = struct.unpack(">f", struct.pack(">i", i))[0]
    return y * (1.5 - 0.5 * number * y * y)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    # https://en.wikipedia.org/wiki/Fast_inverse_square_root#Accuracy
    from math import sqrt

    for i in range(5, 101, 5):
        print(f"{i:>3}: {(1 / sqrt(i)) - fast_inverse_sqrt(i):.5f}")
