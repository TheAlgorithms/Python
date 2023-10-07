"""Binary Exponentiation."""

# Author : Junth Basnet
# Time Complexity : O(logn)


def binary_exponentiation(a: int, n: int) -> int:
    """

    >>> binary_exponentiation(1, 1)
    1

    >>> binary_exponentiation(2, 1)
    2

    >>> binary_exponentiation(3, 1)
    3

    >>> binary_exponentiation(4, 1)
    4

    >>> binary_exponentiation(1, 2)
    1

    >>> binary_exponentiation(2, 2)
    4

    >>> binary_exponentiation(3, 2)
    9

    >>> binary_exponentiation(4, 2)
    16

    >>> binary_exponentiation(1, 3)
    1

    >>> binary_exponentiation(2, 3)
    8

    >>> binary_exponentiation(3, 3)
    27

    >>> binary_exponentiation(4, 3)
    64

    """
    if n == 0:
        return 1

    elif n % 2 == 1:
        return binary_exponentiation(a, n - 1) * a

    else:
        b = binary_exponentiation(a, n // 2)
        return b * b


if __name__ == "__main__":
    import doctest

    doctest.testmod()
