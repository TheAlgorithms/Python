"""
Problem 7: https://projecteuler.net/problem=7

By listing the first six prime numbers:

    2, 3, 5, 7, 11, and 13

We can see that the 6th prime is 13. What is the Nth prime number?
"""


def isprime(number: int) -> bool:
    """Determines whether the given number is prime or not"""
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def solution(nth: int = 10001) -> int:
    """Returns the n-th prime number.

    >>> solution(6)
    13
    >>> solution(1)
    2
    >>> solution(3)
    5
    >>> solution(20)
    71
    >>> solution(50)
    229
    >>> solution(100)
    541
    >>> solution()
    104743
    >>> solution(3.4)
    5
    >>> solution(0)
    Traceback (most recent call last):
        ...
    ValueError: Parameter nth must be greater or equal to one.
    >>> solution(-17)
    Traceback (most recent call last):
        ...
    ValueError: Parameter nth must be greater or equal to one.
    >>> solution([])
    Traceback (most recent call last):
        ...
    TypeError: Parameter nth must be int or passive of cast to int.
    >>> solution("asd")
    Traceback (most recent call last):
        ...
    TypeError: Parameter nth must be int or passive of cast to int.
    """
    try:
        nth = int(nth)
    except (TypeError, ValueError):
        raise TypeError(
            "Parameter nth must be int or passive of cast to int."
        ) from None
    if nth <= 0:
        raise ValueError("Parameter nth must be greater or equal to one.")
    primes = []
    num = 2
    while len(primes) < nth:
        if isprime(num):
            primes.append(num)
            num += 1
        else:
            num += 1
    return primes[len(primes) - 1]


if __name__ == "__main__":
    print(solution(int(input().strip())))
