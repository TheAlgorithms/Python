"""
Project Euler Problem 9: https://projecteuler.net/problem=9

Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a*b*c.

References:
    - https://en.wikipedia.org/wiki/Pythagorean_triple
"""


def get_squares(n: int) -> list[int]:
    res = [0] * n
    for i in range(n):
        res[i] = i * i
    return res


def solution(n: int = 1000) -> int:
    """
    Precomputing squares and checking if a*a + b*b is the square by set look-up.

    >>> solution(12)
    60
    >>> solution(36)
    1620
    """

    squares = get_squares(n)
    squares_set = set(squares)
    for i in range(1, n):
        for j in range(i, n):
            if (
                squares[i] + squares[j] in squares_set
                and squares[n - i - j] == squares[i] + squares[j]
            ):
                return i * j * (n - i - j)

    return -1


if __name__ == "__main__":
    print(f"{solution() = }")
