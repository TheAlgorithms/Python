"""
Project Euler Problem 190: https://projecteuler.net/problem=190

Maximising a Weighted Product

Let S_m = (x_1, x_2, ..., x_m) be the m-tuple of positive real numbers with
x_1 + x_2 + ... + x_m = m for which P_m = x_1 * x_2^2 * ... * x_m^m is maximised.
For example, it can be verified that |_P_10_| = 4112
(|__| is the integer part function).
Find Sum_{m=2}^15 = |_P_m_|.

Solution:
- Fix x_1 = m - x_2 - ... - x_m.
- Calculate partial derivatives of P_m wrt the x_2, ..., x_m. This gives that
  x_2 = 2 * x_1, x_3 = 3 * x_1, ..., x_m = m * x_1.
- Calculate partial second order derivatives of P_m wrt the x_2, ..., x_m.
  By plugging in the values from the previous step, can verify that solution is maximum.

>>> solution(5)
10

"""


def solution(n: int = 15) -> int:
    """
    Calculate sum of P_m for m from 2 to n.

    >>> solution(2)
    1
    >>> solution(3)
    2
    >>> solution(4)
    4

    """

    ans = 0
    for m in range(2, n + 1):
        x1 = 2 / (m + 1)
        capital_p = 1.0
        for i in range(1, m + 1):
            xi = i * x1
            capital_p *= pow(xi, i)
        ans += int(capital_p)
    return ans


if __name__ == "__main__":
    print(f"{solution() = }")
