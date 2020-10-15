"""
Problem 16: https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def power(base: int, exponent: int) -> int:
    """
    Returns the value base^exponent in O(log(exponent)) complexity.
    >>> power(2, 0)
    1
    >>> power(2, 3)
    8
    >>> power(10, 3)
    1000
    >>> power(15, 3)
    3375
    """
    if exponent == 0:
        return 1

    d = power(base, exponent // 2)
    result = d * d
    if exponent % 2 != 0:
        result *= base
    return result


def solution(exponent: int = 1000) -> int:
    """
    Returns the sum of the digits of the number 2^exponent.
    >>> solution(1000)
    1366
    >>> solution(50)
    76
    >>> solution(20)
    31
    >>> solution(15)
    26
    """
    result = power(2, exponent)
    answer = 0
    while result > 0:
        answer += result % 10
        result //= 10
    return answer


if __name__ == "__main__":
    print(f"{solution() = }")
