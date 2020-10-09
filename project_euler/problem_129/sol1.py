"""
A number consisting entirely of ones is called a repunit. We shall define R(k) to be
a repunit of length k; for example, R(6) = 111111.

Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there
always exists a value, k, for which R(k) is divisible by n, and let A(n) be the least
such value of k; for example, A(7) = 6 and A(41) = 5.

The least value of n for which A(n) first exceeds ten is 17.

Find the least value of n for which A(n) first exceeds one-million.
"""


def A(n: int) -> int:
    """
    Return the least value k such that the Repunit of length k is divisible by n.
    >>> A(7)
    6
    >>> A(41)
    5
    >>> A(1234567)
    34020
    """
    if n % 5 == 0 or n % 2 == 0:
        return 0
    R = 1
    k = 1
    while R:
        R = (10 * R + 1) % n
        k += 1
    return k


def solution(limit: int = 1000000) -> int:
    """
    Return the least value of n for which A(n) first exceeds limit.
    """
    n = limit - 1
    while A(n) <= limit:
        n += 2
    return n


if __name__ == "__main__":
    print(solution())
