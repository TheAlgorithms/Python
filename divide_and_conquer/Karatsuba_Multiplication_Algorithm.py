"""
Description:
    Karatsuba Multiplication Algorithm is an efficient way to multiply two large numbers
    by reducing the multiplication operations using divide and conquer approach.

Functionality:
    The algorithm breaks down the multiplication of two n-digit numbers into
    at most 3n^log2(3) (approximately 3n^1.585) single-digit multiplications in general.

Complexity:
    The time complexity of Karatsuba Multiplication Algorithm is O(n^log2(3)),
    which is better than the traditional O(n^2) complexity for large n.

Example:
    >>> karatsuba_multiplication(1234, 5678)
    7006652
    >>> karatsuba_multiplication(123, 456)
    56088
    >>> karatsuba_multiplication(12345, 6789)
    83810205
"""


def karatsuba_multiplication(x, y):
    """
    Multiply two integers using Karatsuba's algorithm.

    Parameters:
    x (int): First integer to multiply.
    y (int): Second integer to multiply.

    Returns:
    int: The product of x and y.

    >>> karatsuba_multiplication(1234, 5678)
    7006652
    >>> karatsuba_multiplication(123, 456)
    56088
    >>> karatsuba_multiplication(0, 12345)
    0
    """
    # Base case for recursion
    if x < 10 or y < 10:
        return x * y

    # Calculates the size of the numbers.
    n = max(len(str(x)), len(str(y)))
    half = n // 2

    # Split the digit sequences in the middle.
    a, b = divmod(x, 10**half)
    c, d = divmod(y, 10**half)

    # 3 calls made to numbers approximately half the size.
    ac = karatsuba_multiplication(a, c)
    bd = karatsuba_multiplication(b, d)
    ad_plus_bc = karatsuba_multiplication(a + b, c + d) - ac - bd

    # Performs the multiplication.
    return ac * 10 ** (2 * half) + (ad_plus_bc * 10**half) + bd


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    x = 1234
    y = 5678
    print(f"The product of {x} and {y} is {karatsuba_multiplication(x, y)}")
