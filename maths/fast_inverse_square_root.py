"""
https://en.wikipedia.org/wiki/Fast_inverse_square_root
Used in Quake III Arena
Source: https://ajcr.net/fast-inverse-square-root-python/
"""
from ctypes import c_float, c_int32, cast, byref, POINTER

def Q_rsqrt(x):
    threehalfs = 1.5
    x2 = x * 0.5
    y = c_float(x)

    i = cast(byref(y), POINTER(c_int32)).contents.value
    i = c_int32(0x5f3759df - (i >> 1))
    y = cast(byref(i), POINTER(c_float)).contents.value

    y = y * (threehalfs - (x2 * y * y))
    y = y * (threehalfs - (x2 * y * y)) # 2nd iteration, this can be removed
    return y


if __name__ == "__main__":
    num = 2
    print(Q_rsqrt(num))