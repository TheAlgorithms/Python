"""
https://en.wikipedia.org/wiki/Lucas_number
"""

import functools
import math


def recursive_lucas_number(n_th_number: int) -> int:
    """
    Returns the nth lucas number
    >>> recursive_lucas_number(1)
    1
    >>> recursive_lucas_number(20)
    15127
    >>> recursive_lucas_number(0)
    2
    >>> recursive_lucas_number(25)
    167761
    >>> recursive_lucas_number(-1.5)
    Traceback (most recent call last):
        ...
    TypeError: recursive_lucas_number accepts only integer arguments.
    """
    if not isinstance(n_th_number, int):
        raise TypeError("recursive_lucas_number accepts only integer arguments.")

    # Use memoization to cache results and avoid redundant calculations
    @functools.cache
    def _recursive_lucas(n: int) -> int:
        if n == 0:
            return 2
        if n == 1:
            return 1
        return _recursive_lucas(n - 1) + _recursive_lucas(n - 2)

    return _recursive_lucas(n_th_number)


def dynamic_lucas_number(n_th_number: int) -> int:
    """
    Returns the nth lucas number
    >>> dynamic_lucas_number(1)
    1
    >>> dynamic_lucas_number(20)
    15127
    >>> dynamic_lucas_number(0)
    2
    >>> dynamic_lucas_number(25)
    167761
    >>> dynamic_lucas_number(-1.5)
    Traceback (most recent call last):
        ...
    TypeError: dynamic_lucas_number accepts only integer arguments.
    """
    if not isinstance(n_th_number, int):
        raise TypeError("dynamic_lucas_number accepts only integer arguments.")

    if n_th_number == 0:
        return 2
    if n_th_number == 1:
        return 1

    a, b = 2, 1
    for _ in range(2, n_th_number + 1):
        a, b = b, a + b

    return b


def matrix_power_lucas_number(n_th_number: int) -> int:
    """
    Returns the nth lucas number using matrix exponentiation
    >>> matrix_power_lucas_number(1)
    1
    >>> matrix_power_lucas_number(20)
    15127
    >>> matrix_power_lucas_number(0)
    2
    >>> matrix_power_lucas_number(25)
    167761
    >>> matrix_power_lucas_number(-1.5)
    Traceback (most recent call last):
        ...
    TypeError: matrix_power_lucas_number accepts only integer arguments.
    """
    if not isinstance(n_th_number, int):
        raise TypeError("matrix_power_lucas_number accepts only integer arguments.")

    if n_th_number == 0:
        return 2
    if n_th_number == 1:
        return 1

    def matrix_mult(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
        return [
            [
                a[0][0] * b[0][0] + a[0][1] * b[1][0],
                a[0][0] * b[0][1] + a[0][1] * b[1][1],
            ],
            [
                a[1][0] * b[0][0] + a[1][1] * b[1][0],
                a[1][0] * b[0][1] + a[1][1] * b[1][1],
            ],
        ]

    def matrix_power(matrix: list[list[int]], power: int) -> list[list[int]]:
        # Start with identity matrix
        result: list[list[int]] = [[1, 0], [0, 1]]
        base = matrix

        while power > 0:
            if power % 2 == 1:
                result = matrix_mult(result, base)
            base = matrix_mult(base, base)
            power //= 2

        return result

    # Lucas number matrix form: [[1, 1], [1, 0]]
    base_matrix = [[1, 1], [1, 0]]
    powered_matrix = matrix_power(base_matrix, n_th_number - 1)

    # L(n) = powered_matrix[0][0] * L(1) + powered_matrix[0][1] * L(0)
    # Where L(1) = 1, L(0) = 2
    return powered_matrix[0][0] * 1 + powered_matrix[0][1] * 2


def closed_form_lucas_number(n_th_number: int) -> int:
    """
    Returns the nth lucas number using the closed-form formula (Binet's formula)
    >>> closed_form_lucas_number(1)
    1
    >>> closed_form_lucas_number(20)
    15127
    >>> closed_form_lucas_number(0)
    2
    >>> closed_form_lucas_number(25)
    167761
    >>> closed_form_lucas_number(-1.5)
    Traceback (most recent call last):
        ...
    TypeError: closed_form_lucas_number accepts only integer arguments.
    """
    if not isinstance(n_th_number, int):
        raise TypeError("closed_form_lucas_number accepts only integer arguments.")

    if n_th_number == 0:
        return 2
    if n_th_number == 1:
        return 1

    # Golden ratio
    phi = (1 + math.sqrt(5)) / 2
    # Conjugate of golden ratio
    psi = (1 - math.sqrt(5)) / 2

    # Lucas number closed form: L(n) = phi^n + psi^n
    return round(phi**n_th_number + psi**n_th_number)


# Global cache for performance optimization
_lucas_cache: dict[int, int] = {0: 2, 1: 1}


def cached_lucas_number(n_th_number: int) -> int:
    """
    Returns the nth lucas number using a cached approach for optimal performance
    >>> cached_lucas_number(1)
    1
    >>> cached_lucas_number(20)
    15127
    >>> cached_lucas_number(0)
    2
    >>> cached_lucas_number(25)
    167761
    >>> cached_lucas_number(-1.5)
    Traceback (most recent call last):
        ...
    TypeError: cached_lucas_number accepts only integer arguments.
    """
    if not isinstance(n_th_number, int):
        raise TypeError("cached_lucas_number accepts only integer arguments.")

    if n_th_number in _lucas_cache:
        return _lucas_cache[n_th_number]

    # Calculate using the fastest method for uncached values
    if n_th_number < 70:  # For smaller values, closed form is efficient
        result = closed_form_lucas_number(n_th_number)
    else:  # For larger values, matrix exponentiation is more stable
        result = matrix_power_lucas_number(n_th_number)

    _lucas_cache[n_th_number] = result
    return result


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    n = int(input("Enter the number of terms in lucas series:\n").strip())
    print("Using recursive function to calculate lucas series:")
    print(" ".join(str(recursive_lucas_number(i)) for i in range(n)))
    print("\nUsing dynamic function to calculate lucas series:")
    print(" ".join(str(dynamic_lucas_number(i)) for i in range(n)))
    print("\nUsing matrix exponentiation to calculate lucas series:")
    print(" ".join(str(matrix_power_lucas_number(i)) for i in range(n)))
    print("\nUsing closed-form formula to calculate lucas series:")
    print(" ".join(str(closed_form_lucas_number(i)) for i in range(n)))
    print("\nUsing cached function to calculate lucas series:")
    print(" ".join(str(cached_lucas_number(i)) for i in range(n)))
