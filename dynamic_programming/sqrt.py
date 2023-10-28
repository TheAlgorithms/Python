import struct


def fast_inverse_square_root(number):
    """
    Approximates the inverse square root of a floating-point number using the Fast InvSqrt algorithm.

    Args:
        number (float): The input number for which to compute the inverse square root.

    Returns:
        float: The approximate inverse square root of the input number.

    Examples:
        >>> fast_inverse_square_root(4.0)
        0.4991540749756012
        >>> fast_inverse_square_root(16.0)
        0.24907859867279026
        >>> fast_inverse_square_root(9.0)
        0.33340289926886996
    """
    threehalfs = 1.5

    # Convert the input number to a 32-bit float
    i = struct.unpack("I", struct.pack("f", number))[0]

    # Initial guess for the square root (using bit manipulation)
    i = 0x5F3759DF - (i >> 1)

    # Convert the modified bits back to a float
    number = struct.unpack("f", struct.pack("I", i))[0]

    # Newton-Raphson iteration for increased accuracy
    number = number * (threehalfs - (0.5 * number * number))

    return number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
