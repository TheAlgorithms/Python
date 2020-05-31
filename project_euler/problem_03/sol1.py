"""
Problem:
The prime factors of 13195 are 5,7,13 and 29. What is the largest prime factor
of a given number N?

e.g. for 10, largest prime factor = 5. For 17, largest prime factor = 17.
"""
import math


def isprime(no):
    if no == 2:
        return True
    elif no % 2 == 0:
        return False
    sq = int(math.sqrt(no)) + 1
    for i in range(3, sq, 2):
        if no % i == 0:
            return False
    return True


def solution(n):
    """Returns the largest prime factor of a given number n.

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
    maxNumber = 0
    if isprime(n):
        return n
    else:
        while n % 2 == 0:
            n = n / 2
        if isprime(n):
            return int(n)
        else:
            n1 = int(math.sqrt(n)) + 1
            for i in range(3, n1, 2):
                if n % i == 0:
                    if isprime(n / i):
                        maxNumber = n / i
                        break
                    elif isprime(i):
                        maxNumber = i
            return maxNumber


if __name__ == "__main__":
    print(solution(int(input().strip())))
