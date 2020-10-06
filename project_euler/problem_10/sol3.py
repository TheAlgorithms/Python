"""
https://projecteuler.net/problem=10

Problem Statement:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def solution(n: int = 2000000) -> int:
    """Returns the sum of all the primes below n using Sieve of Eratosthenes:

    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    The sieve of Eratosthenes is one of the most efficient ways to find all primes
    smaller than n when n is smaller than 10 million.  Only for positive numbers.

    >>> solution(2_000_000)
    142913828922
    >>> solution(1_000)
    76127
    >>> solution(5_000)
    1548136
    >>> solution(10_000)
    5736396
    >>> solution(7)
    10
    >>> solution(7.1)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: 'float' object cannot be interpreted as an integer
    >>> solution(-7)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    IndexError: list assignment index out of range
    >>> solution("seven")  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: can only concatenate str (not "int") to str
    """
    primality_list = [0 for i in range(n + 1)]
    primality_list[0] = 1
    primality_list[1] = 1

    for i in range(2, int(n ** 0.5) + 1):
        if primality_list[i] == 0:
            for j in range(i * i, n + 1, i):
                primality_list[j] = 1
    sum_of_primes = 0
    for i in range(n):
        if primality_list[i] == 0:
            sum_of_primes += i
    return sum_of_primes


if __name__ == "__main__":
    print(solution(int(input().strip())))
