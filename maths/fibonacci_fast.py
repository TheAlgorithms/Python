"""
Fibonacci sequence via matrix exponentiation — O(log n) time complexity.

The standard recursive Fibonacci runs in O(2^n) time. Using matrix exponentiation
we can compute the n-th Fibonacci number in O(log n) multiplications.

The key identity is:
    | F(n+1)  F(n)   |   | 1  1 | ^ n
    | F(n)    F(n-1) | = | 1  0 |

So F(n) = (M^n)[0][1]  where M = [[1, 1], [1, 0]].

References:
  - https://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
"""


def _mat_mul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    """Multiply two 2x2 integer matrices.

    >>> _mat_mul([[1, 1], [1, 0]], [[1, 0], [0, 1]])
    [[1, 1], [1, 0]]
    """
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


def _mat_pow(matrix: list[list[int]], power: int) -> list[list[int]]:
    """Raise a 2x2 integer matrix to a non-negative integer power using
    fast exponentiation (repeated squaring).

    :param matrix: A 2x2 matrix represented as a list of lists.
    :param power: Non-negative integer exponent.
    :return: matrix ** power

    >>> _mat_pow([[1, 1], [1, 0]], 0)
    [[1, 0], [0, 1]]
    >>> _mat_pow([[1, 1], [1, 0]], 1)
    [[1, 1], [1, 0]]
    >>> _mat_pow([[1, 1], [1, 0]], 2)
    [[2, 1], [1, 1]]
    """
    # Identity matrix
    result: list[list[int]] = [[1, 0], [0, 1]]
    while power:
        if power % 2 == 1:
            result = _mat_mul(result, matrix)
        matrix = _mat_mul(matrix, matrix)
        power //= 2
    return result


def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number using matrix exponentiation.

    Time complexity: O(log n)
    Space complexity: O(log n) due to the call stack of _mat_pow

    :param n: Non-negative integer index into the Fibonacci sequence
              (0-indexed: F(0)=0, F(1)=1, F(2)=1, ...).
    :raises ValueError: If *n* is negative.
    :return: The n-th Fibonacci number.

    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(10)
    55
    >>> fibonacci(20)
    6765
    >>> fibonacci(50)
    12586269025
    >>> fibonacci(-1)
    Traceback (most recent call last):
        ...
    ValueError: fibonacci() only accepts non-negative integers
    """
    if n < 0:
        raise ValueError("fibonacci() only accepts non-negative integers")
    if n == 0:
        return 0
    m: list[list[int]] = [[1, 1], [1, 0]]
    return _mat_pow(m, n)[0][1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    for i in range(15):
        print(f"fibonacci({i}) = {fibonacci(i)}")
