"""
Prime summations
Problem 77

It is possible to write ten as the sum of primes
in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written
as the sum of primes in over five thousand different ways?
"""


def solution(length=5000) -> int:
    """Ways to write sum of primes

    Keyword arguments:
    amount -- amount of different ways (default 5000)

    Passing no parameters returns the result
    >>> solution()
    71
    """

    primes = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
    ]

    target = 11
    while True:
        ways = [1] + [0] * target
        for p in primes:
            for i in range(p, target + 1):
                ways[i] += ways[i - p]
        if ways[target] > length:
            break
        target += 1
    return target


if __name__ == "__main__":
    print(solution())
