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

def karatsuba_multiply(x: str, y: str) -> int:
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
    n = max(len(x), len(y))

    # Pad the shorter string with leading zeros
    x = x.zfill(n)
    y = y.zfill(n)

    # Base case: single bit multiplication
    if n == 1:
        return int(x) * int(y)

    mid = n // 2

    # Split the binary strings into left and right halves
    x_left, x_right = x[:mid], x[mid:]
    y_left, y_right = y[:mid], y[mid:]

    # Recursively compute partial products
    p1 = karatsuba_multiply(x_left, y_left)
    p2 = karatsuba_multiply(x_right, y_right)
    p3 = karatsuba_multiply(
        bin(int(x_left, 2) + int(x_right, 2))[2:],
        bin(int(y_left, 2) + int(y_right, 2))[2:]
    )

    # Karatsuba combination formula:
    result = (p1 << (2 * (n - mid))) + ((p3 - p1 - p2) << (n - mid)) + p2

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
