"""
Project Euler Problem 9: https://projecteuler.net/problem=9

Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2.

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

References:
    - https://en.wikipedia.org/wiki/Pythagorean_triple
"""


def get_squares(n: int) -> list[int]:
    """
    >>> get_squares(0)
    []
    >>> get_squares(1)
    [0]
    >>> get_squares(2)
    [0, 1]
    >>> get_squares(3)
    [0, 1, 4]
    >>> get_squares(4)
    [0, 1, 4, 9]
    """
    return [number * number for number in range(n)]


def solution(n: int = 1000) -> int:
    """
    Precomputing squares and checking if a^2 + b^2 is the square by set look-up.

    >>> solution(12)
    60
    >>> solution(36)
    1620
    """

    squares = get_squares(n)
    squares_set = set(squares)
    for a in range(1, n // 3):
        for b in range(a + 1, (n - a) // 2 + 1):
            if (
                squares[a] + squares[b] in squares_set
                and squares[n - a - b] == squares[a] + squares[b]
            ):
                return a * b * (n - a - b)

    return -1


if __name__ == "__main__":
    print(f"{solution() = }")
