"""
Fast inverse square root.
Reference: https://en.wikipedia.org/wiki/Fast_inverse_square_root
"""

import struct


def fast_inverse_sqrt(number: float) -> float:
    """
    Calculate the fast inverse square root of a number.

    This function computes the fast inverse square root of a floating-point number
    using the famous Quake III algorithm, originally developed by id Software.

    :param float number: The input number for which to calculate the inverse square root.
    :return float: The fast inverse square root of the input number.

    Example:
    >>> fast_inverse_sqrt(10)
    0.3156857923527257

    >>> fast_inverse_sqrt(4)
    0.49915357479239103

    >>> fast_inverse_sqrt(0)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a positive number.

    >>> fast_inverse_sqrt(-1)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a positive number.
    """
    if number<=0:
        raise ValueError("Input must be a positive number.")
    i = struct.unpack('>i', struct.pack('>f', number))[0]
    i = 0x5f3759df - (i >> 1)
    y = struct.unpack('>f', struct.pack('>i', i))[0]
    return y * (1.5 - 0.5 * number * y * y)

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
