"""
Project Euler Problem 113: https://projecteuler.net/problem=113

Working from left-to-right if no digit is exceeded by the digit to its left it is
called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing
number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a
"bouncy" number; for example, 155349.

As n increases, the proportion of bouncy numbers below n increases such that there
are only 12951 numbers below one-million that are not bouncy and only 277032
non-bouncy numbers below 10^10.

How many numbers below a googol (10^100) are not bouncy?
"""


def choose(n: int, r: int) -> int:
    """
    Calculate the binomial coefficient c(n,r) using the multiplicative formula.
    >>> choose(4,2)
    6
    >>> choose(5,3)
    10
    >>> choose(20,6)
    38760
    """
    ret = 1.0
    for i in range(1, r + 1):
        ret *= (n + 1 - i) / i
    return round(ret)


def non_bouncy_exact(n: int) -> int:
    """
    Calculate the number of non-bouncy numbers with at most n digits.
    >>> non_bouncy_exact(1)
    9
    >>> non_bouncy_exact(6)
    7998
    >>> non_bouncy_exact(10)
    136126
    """
    return choose(8 + n, n) + choose(9 + n, n) - 10


def non_bouncy_upto(n: int) -> int:
    """
    Calculate the number of non-bouncy numbers with at most n digits.
    >>> non_bouncy_upto(1)
    9
    >>> non_bouncy_upto(6)
    12951
    >>> non_bouncy_upto(10)
    277032
    """
    return sum(non_bouncy_exact(i) for i in range(1, n + 1))


def solution(num_digits: int = 100) -> int:
    """
    Calculate the number of non-bouncy numbers less than a googol.
    >>> solution(6)
    12951
    >>> solution(10)
    277032
    """
    return non_bouncy_upto(num_digits)


if __name__ == "__main__":
    print(f"{solution() = }")
