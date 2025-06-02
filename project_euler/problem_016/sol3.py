"""
Problem 16: https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

from numpy import log10, zeros


def solution(power: int = 1000) -> int:
    """
    Calculates the sum of digits by explicit construction of digits array
    without the help of Python's large integer property.

    >>> solution(50)
    76
    >>> solution(20)
    31
    >>> solution(15)
    26
    >>> solution(3)
    8
    """

    digits = zeros(int(power * log10(2)) + 1)
    digits[0] = 1
    dig_count = 1
    for _ in range(power):
        carry = 0
        for d in range(dig_count):
            digits[d] = digits[d] * 2 + carry
            carry = digits[d] // 10
            digits[d] %= 10
        if carry > 0:
            digits[dig_count] = carry
            dig_count += 1

    return int(sum(digits))


if __name__ == "__main__":
    print(solution())
