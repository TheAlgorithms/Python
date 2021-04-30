"""
Project Euler Problem 1: https://projecteuler.net/problem=1

Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def calc_arith_sum(A1: int, An: int, d: int) -> int:
    """
    Returns the sum of A.P with A1, An and d
    More info here - https://en.wikipedia.org/wiki/Arithmetic_progression#Sum

    >>> calc_arith_sum(0, 9, 3)
    18
    >>> calc_arith_sum(4, 16, 4)
    40
    >>> calc_arith_sum(1, 8, 7)
    9
    """
    num_elemens = int((An - A1) / d + 1)
    return int(((A1 + An) * num_elemens) / 2)


def find_An(n: int, d: int) -> int:
    """
    Returns the max element of an A.P with a common difference of d that ends below n.

    >>> find_An(1000, 3)
    999
    >>> find_An(1000, 5)
    995
    >>> find_An(1000, 15)
    990
    >>> find_An(1000, 10)
    990
    """
    return int((n - 1) / d) * d


def solution(n: int = 1000) -> int:
    """
    Returns the sum of all the multiples of 3 or 5 below n.
    We'll divide into two sequences:
    1) S1 = 3 + 6 + 9 + 12 + 15 + ... + 999
    2) S2 = 5 + 10 + 15 + 20 + 25 + ... + 995
    These are Arithmetic progressions with a common difference of 3 and 5 respectively.

    We are then need to remove the elements that we've counted twice because they
    appear in both S1 & S2:
    S3 = 15 + 30 + 45 + ...
    This is simply the Arithmetic progression with a common difference 15.

    The results will be: S1 + S2 - S3.

    Runtime complexity: O(1).
    Memory complexity: O(1).

    >>> solution(3)
    0
    >>> solution(4)
    3
    >>> solution(10)
    23
    >>> solution(600)
    83700
    >>> solution(1000000)
    233333166668
    """
    S1 = calc_arith_sum(3, find_An(n, 3), 3)
    S2 = calc_arith_sum(5, find_An(n, 5), 5)
    S3 = calc_arith_sum(15, find_An(n, 15), 15)
    return S1 + S2 - S3


if __name__ == "__main__":
    print(f"Solution = {solution()}")
