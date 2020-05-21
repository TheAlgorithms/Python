"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def solution(power):
    """Returns the sum of the digits of the number 2^power.

    >>> solution(1000)
    1366
    >>> solution(50)
    76
    >>> solution(20)
    31
    >>> solution(15)
    26
    """
    n = 2 ** power
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r


if __name__ == "__main__":
    print(solution(int(str(input()).strip())))
