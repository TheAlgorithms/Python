"""
https://en.wikipedia.org/wiki/Fast_inverse_square_root
Used in Quake III Arena
Source: https://ajcr.net/fast-inverse-square-root-python/
"""
from ctypes import POINTER, byref, c_float, c_int32, cast


def fast_inverse_square_root(x) -> float:
    """
       Find inverse square root of a number.
       Arguments:
           x: Number to find the inverse square root of.
       Return Value: Inverse square root of x
    >>> fast_inverse_square_root(1)
    0.9999957038118442
    >>> fast_inverse_square_root(2)
    0.7071067149264607
    >>> fast_inverse_square_root(3)
    0.5773496109110817
    >>> fast_inverse_square_root(4)
    0.4999978519059221
    """
    threehalfs = 1.5
    x2 = x * 0.5
    y = c_float(x)

    i = cast(byref(y), POINTER(c_int32)).contents.value
    i = c_int32(0x5F3759DF - (i >> 1))
    y = cast(byref(i), POINTER(c_float)).contents.value

    y = y * (threehalfs - (x2 * y * y))
    y = y * (threehalfs - (x2 * y * y))  # 2nd iteration, this can be removed
    return y


if __name__ == "__main__":
    import doctest

    doctest.testmod()
