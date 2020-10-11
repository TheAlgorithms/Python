"""
Problem 16: https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def power(x: int, n: int) -> int:
    """
    Returns the value x^n in O(log(n)) complexity.
    >>> power(2, 0)
    1
    >>> power(2, 3)
    8
    >>> power(10, 3)
    1000
    >>> power(15, 3)
    3375
    """
    if n == 0:
        return 1

    d = power(x, n // 2)
    result = d * d
    if n % 2 != 0:
        result *= x
    return result


def solution(n: int = 1000) -> int:
    """
    Returns the sum of the digits of the number 2^n.
    >>> solution(1000)
    1366
    >>> solution(50)
    76
    >>> solution(20)
    31
    >>> solution(15)
    26
    """
    res = power(2, n)
    answer = 0
    while res > 0:
        answer += res % 10
        res //= 10
    return answer


if __name__ == "__main__":
    print(solution())
