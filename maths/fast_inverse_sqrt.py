"""
Fast inverse square root.
Reference: https://en.wikipedia.org/wiki/Fast_inverse_square_root
"""

import struct


def fastInvSqrt(x: float) -> float:
    """
    Calculate the fast inverse square root of a number.

    This function computes the fast inverse square root of a floating-point number
    using the famous Quake III algorithm, originally developed by id Software.

    :param float x: The input number for which to calculate the inverse square root.
    :return float: The fast inverse square root of the input number.

    Example:
    >>> fastInvSqrt(10)
    0.3156857923527257

    >>> fastInvSqrt(4)
    0.49915357479239103
    """
    i = struct.unpack('>i', struct.pack('>f', x))[0]
    i = 0x5f3759df - (i >> 1)
    y = struct.unpack('>f', struct.pack('>i', i))[0]
    return y * (1.5 - 0.5 * x * y * y)

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)