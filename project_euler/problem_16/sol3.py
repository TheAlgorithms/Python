"""
Problem 16: https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""


def solution(power: int) -> int:
    """
    Returns the sum of the digits of the number `2 ^ power`.

    >>> solution(1000)
    1366
    >>> solution(50)
    76
    >>> solution(20)
    31
    >>> solution(15)
    26
    """

    if not isinstance(power, int):
        raise TypeError("The parameter `power` should be of type int.")

    if power < 0:
        raise ValueError("The value of `power` should be greater than or equal to 0.")

    n = 2 ** power
    digits = [int(digit) for digit in str(n)]

    return sum(digits)


if __name__ == "__main__":
    power = int(input().strip())
    result = solution(power)

    print(result)
