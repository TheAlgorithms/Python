"""
Problem:
The prime factors of 13195 are 5,7,13 and 29. What is the largest prime factor
of a given number N?

e.g. for 10, largest prime factor = 5. For 17, largest prime factor = 17.
"""
from math import sqrt, ceil


def solution(n):
    """Returns the largest prime factor of a given number n.

    What unique about this solution?
    This solution is at least double of speed than previous solutions.
    It increment by 2 after the first primary.

    >>> solution(13195)
    29
    >>> solution(10)
    5
    >>> solution(17)
    17
    >>> solution(3.4)
    3
    >>> solution(0)
    Traceback (most recent call last):
        ...
    ValueError: Parameter n must be greater or equal to one.
    >>> solution(-17)
    Traceback (most recent call last):
        ...
    ValueError: Parameter n must be greater or equal to one.
    >>> solution([])
    Traceback (most recent call last):
        ...
    TypeError: Parameter n must be int or passive of cast to int.
    >>> solution("asd")
    Traceback (most recent call last):
        ...
    TypeError: Parameter n must be int or passive of cast to int.
    """
    try:
        n = int(n)
    except (TypeError, ValueError):
        raise TypeError("Parameter n must be int or passive of cast to int.")
    if n <= 0:
        raise ValueError("Parameter n must be greater or equal to one.")
    p, s = 2, set()
    while p <= ceil(sqrt(n)):
        while n % p == 0:
            s.add(p)
            n //= p
        p += 1 if p == 2 else 2
    if n > 2:
        s.add(n)
    return max(s)


if __name__ == "__main__":
    print(solution(int(input().strip())))
