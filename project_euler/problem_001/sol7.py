"""
Problem Statement:
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below N.
"""


def solution(n: int = 1000) -> int:
    """Returns the sum of all the multiples of 3 or 5 below n.

    >>> solution(3)
    0
    >>> solution(4)
    3
    >>> solution(10)
    23
    >>> solution(600)
    83700
    """

    result = 0
    for i in range(n):
        if i % 3 == 0:
            result += i
        elif i % 5 == 0:
            result += i
    return result


if __name__ == "__main__":
    print(solution(int(input().strip())))
