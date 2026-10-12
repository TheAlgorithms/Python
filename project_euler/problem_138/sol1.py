"""
Project Euler Problem 138: https://projecteuler.net/problem=138

Special Isosceles Triangles


With change of variables

c = b/2

and requiring that

h = 2c +- 1

the triangle relation

c^2 + h^2 = L^2

can be expressed as

5 c^2 +- 4c + 1 = L^2

or with some rearrangement:

(5c +- 2)^2 = 5L^2 - 1

This to be solved for positive integer c and L, requires that

5L^2 - 1 = m^2

The above equation is negative Pell's equation with n = 5 and can be solved
recursively as outlined in the wikipedia article.
Note, we neglect first solution (m = 2, L = 1), as this leads to b and h
being non-integers.

Reference: https://en.wikipedia.org/wiki/Pell%27s_equation#The_negative_Pell's_equation

"""


def solution(k: int = 12) -> int:
    """
    The recursive solution of negative Pell's equation with k + 1 values of L
    summed and the first solution being skipped.

    >>> solution(2)
    322
    >>> solution(5)
    1866293
    """

    m_i = 2
    l_i = 1
    ans = 0
    for _ in range(2, k + 2):
        m_i, l_i = 4 * m_i + 5 * m_i + 20 * l_i, 4 * l_i + 5 * l_i + 4 * m_i
        ans += l_i

    return ans


if __name__ == "__main__":
    print(f"{solution() = }")
