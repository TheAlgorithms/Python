"""
Binary Exponentiation

This is a method to find a^b in O(log b) time complexity and is one of the most commonly
used methods of exponentiation. The method is also useful for modular exponentiation,
when the solution to (a^b) % c is required.

To calculate a^b:
- If b is even, then a^b = (a * a)^(b / 2)
- If b is odd, then a^b = a * a^(b - 1)
Repeat until b = 1 or b = 0

For modular exponentiation, we use the fact that (a * b) % c = ((a % c) * (b % c)) % c
"""


def binary_exp_recursive(base: float, exponent: int) -> float:
    """
    Computes a^b recursively, where a is the base and b is the exponent

    >>> binary_exp_recursive(3, 5)
    243
    >>> binary_exp_recursive(11, 13)
    34522712143931
    >>> binary_exp_recursive(-1, 3)
    -1
    >>> binary_exp_recursive(0, 5)
    0
    >>> binary_exp_recursive(3, 1)
    3
    >>> binary_exp_recursive(3, 0)
    1
    >>> binary_exp_recursive(1.5, 4)
    5.0625
    >>> binary_exp_recursive(3, -1)
    Traceback (most recent call last):
        ...
    ValueError: Exponent must be a non-negative integer
    """
    if exponent < 0:
        raise ValueError("Exponent must be a non-negative integer")

    if exponent == 0:
        return 1

    if exponent % 2 == 1:
        return binary_exp_recursive(base, exponent - 1) * base

    b = binary_exp_recursive(base, exponent // 2)
    return b * b


def binary_exp_iterative(base: float, exponent: int) -> float:
    """
    Computes a^b iteratively, where a is the base and b is the exponent

    >>> binary_exp_iterative(3, 5)
    243
    >>> binary_exp_iterative(11, 13)
    34522712143931
    >>> binary_exp_iterative(-1, 3)
    -1
    >>> binary_exp_iterative(0, 5)
    0
    >>> binary_exp_iterative(3, 1)
    3
    >>> binary_exp_iterative(3, 0)
    1
    >>> binary_exp_iterative(1.5, 4)
    5.0625
    >>> binary_exp_iterative(3, -1)
    Traceback (most recent call last):
        ...
    ValueError: Exponent must be a non-negative integer
    """
    if exponent < 0:
        raise ValueError("Exponent must be a non-negative integer")

    res: int | float = 1
    while exponent > 0:
        if exponent & 1:
            res *= base

        base *= base
        exponent >>= 1

    return res


def binary_exp_mod_recursive(base: float, exponent: int, modulus: int) -> float:
    """
    Computes a^b % c recursively, where a is the base, b is the exponent, and c is the
    modulus

    >>> binary_exp_mod_recursive(3, 4, 5)
    1
    >>> binary_exp_mod_recursive(11, 13, 7)
    4
    >>> binary_exp_mod_recursive(1.5, 4, 3)
    2.0625
    >>> binary_exp_mod_recursive(7, -1, 10)
    Traceback (most recent call last):
        ...
    ValueError: Exponent must be a non-negative integer
    >>> binary_exp_mod_recursive(7, 13, 0)
    Traceback (most recent call last):
        ...
    ValueError: Modulus must be a positive integer
    """
    if exponent < 0:
        raise ValueError("Exponent must be a non-negative integer")
    if modulus <= 0:
        raise ValueError("Modulus must be a positive integer")

    if exponent == 0:
        return 1

    if exponent % 2 == 1:
        return (binary_exp_mod_recursive(base, exponent - 1, modulus) * base) % modulus

    r = binary_exp_mod_recursive(base, exponent // 2, modulus)
    return (r * r) % modulus


def binary_exp_mod_iterative(base: float, exponent: int, modulus: int) -> float:
    """
    Computes a^b % c iteratively, where a is the base, b is the exponent, and c is the
    modulus

    >>> binary_exp_mod_iterative(3, 4, 5)
    1
    >>> binary_exp_mod_iterative(11, 13, 7)
    4
    >>> binary_exp_mod_iterative(1.5, 4, 3)
    2.0625
    >>> binary_exp_mod_iterative(7, -1, 10)
    Traceback (most recent call last):
        ...
    ValueError: Exponent must be a non-negative integer
    >>> binary_exp_mod_iterative(7, 13, 0)
    Traceback (most recent call last):
        ...
    ValueError: Modulus must be a positive integer
    """
    if exponent < 0:
        raise ValueError("Exponent must be a non-negative integer")
    if modulus <= 0:
        raise ValueError("Modulus must be a positive integer")

    res: int | float = 1
    while exponent > 0:
        if exponent & 1:
            res = ((res % modulus) * (base % modulus)) % modulus

        base *= base
        exponent >>= 1

    return res


if __name__ == "__main__":
    from timeit import timeit

    a = 1269380576
    b = 374
    c = 34

    runs = 100_000
    print(
        timeit(
            f"binary_exp_recursive({a}, {b})",
            setup="from __main__ import binary_exp_recursive",
            number=runs,
        )
    )
    print(
        timeit(
            f"binary_exp_iterative({a}, {b})",
            setup="from __main__ import binary_exp_iterative",
            number=runs,
        )
    )
    print(
        timeit(
            f"binary_exp_mod_recursive({a}, {b}, {c})",
            setup="from __main__ import binary_exp_mod_recursive",
            number=runs,
        )
    )
    print(
        timeit(
            f"binary_exp_mod_iterative({a}, {b}, {c})",
            setup="from __main__ import binary_exp_mod_iterative",
            number=runs,
        )
    )
