"""
Problem Statement:
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3,5,6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below N.
"""


def solution(n):
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
    return sum(set(range(0, n, 3)).union(set(range(0, n, 5))))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(solution(int(input().strip())))
