"""
Problem Statement:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def sum_of_primes(n):
    if n > 2:
        sumOfPrimes = 2
    else:
        return 0

    for i in range(3, n, 2):
        if is_prime(i):
            sumOfPrimes += i

    return sumOfPrimes


def solution(n):
    """Returns the sum of all the primes below n.

    # The code below has been commented due to slow execution affecting Travis.
    # >>> solution(2000000)
    # 142913828922
    >>> solution(1000)
    76127
    >>> solution(5000)
    1548136
    >>> solution(10000)
    5736396
    >>> solution(7)
    10
    """
    return sum_of_primes(n)


if __name__ == "__main__":
    print(solution(int(input().strip())))
