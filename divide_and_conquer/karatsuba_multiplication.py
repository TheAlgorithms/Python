"""
Performs multiplication of two binary strings using the Karatsuba algorithm.

Given two binary strings of equal length n, the goal is to compute
their product as integers.

For example:
"1100" (12) × "1010" (10) = 120

Karatsuba's algorithm reduces the multiplication of two n-bit numbers
to at most three multiplications of n/2-bit numbers. It achieves
a time complexity of O(n^log₂3) ≈ O(n^1.585), which is faster
than the naive O(n²) approach.

References:
https://en.wikipedia.org/wiki/Karatsuba_algorithm

Example:
>>> karatsuba_multiply("1100", "1010")
120
>>> karatsuba_multiply("10", "11")
6
>>> karatsuba_multiply("101", "111")
35
>>> karatsuba_multiply("0", "0")
0
>>> karatsuba_multiply("1", "0")
0
"""


def karatsuba_multiply(binary_str_1: str, binary_str_2: str) -> int:
    """
    Multiplies two binary strings using the Karatsuba algorithm.

    Both input strings should be of equal length.

    >>> karatsuba_multiply("1100", "1010")
    120
    >>> karatsuba_multiply("11", "10")
    6
    >>> karatsuba_multiply("1111", "1111")
    225
    """
    n = max(len(binary_str_1), len(binary_str_2))

    # Pad the shorter string with leading zeros
    binary_str_1 = binary_str_1.zfill(n)
    binary_str_2 = binary_str_2.zfill(n)

    # Base case: single bit multiplication
    if n == 1:
        return int(binary_str_1) * int(binary_str_2)

    mid = n // 2

    # Split the binary strings into left and right halves
    left_1, right_1 = binary_str_1[:mid], binary_str_1[mid:]
    left_2, right_2 = binary_str_2[:mid], binary_str_2[mid:]

    # Recursively compute partial products
    product_left = karatsuba_multiply(left_1, left_2)
    product_right = karatsuba_multiply(right_1, right_2)
    product_sum = karatsuba_multiply(
        bin(int(left_1, 2) + int(right_1, 2))[2:],
        bin(int(left_2, 2) + int(right_2, 2))[2:],
    )

    # Karatsuba combination formula
    result = (
        (product_left << (2 * (n - mid)))
        + ((product_sum - product_left - product_right) << (n - mid))
        + product_right
    )

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
