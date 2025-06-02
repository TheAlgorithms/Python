"""
Project Euler Problem 127: https://projecteuler.net/problem=127

abc-hits

It takes about 10 minutes to run.
'Brute-force' solution that uses the following simplifications:
- if gcd(a, b) = 1 then gcd(a, c) = 1 and gcd(b, c) = 1
- rad(a*b*c) = rad(a) * rad(b) * rad(c), for gcd(a, b) = 1
- if a is even, b cannot b even for gcd(a, b) = 1 to be true.

>>> solution(1000)
12523
"""

from numpy import sqrt

N = 120000


def generate_primes(n: int) -> list[bool]:
    """
    Generates primes boolean array up to n.

    >>> generate_primes(2)
    [False, False, True]
    >>> generate_primes(5)
    [False, False, True, True, False, True]
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(sqrt(n + 1)) + 1):
        if primes[i]:
            j = i * i
            while j <= n:
                primes[j] = False
                j += i
    return primes


def rad(n: int, primes_list: list[int]) -> int:
    """
    Calculated rad - product of unique prime factors for n, using prime numbers
    list primes_list.

    >>> rad(1, [1])
    1
    >>> rad(12, [2, 3])
    6
    """
    f = 1
    for p in primes_list:
        if p > n:
            break
        if n % p == 0:
            f *= p
    return f


def gcd(a: int, b: int) -> int:
    """
    Calculates greatest common divisor of a and b.

    >>> gcd(1, 10)
    1
    >>> gcd(14, 48)
    2
    """
    while b:
        a, b = b, a % b
    return a


def solution(c_less: int = 120000) -> int:
    """
    Calculates all primes, rads, and then loops over a, b checking the conditions.

    >>> solution(10)
    9
    >>> solution(100)
    316
    """
    primes_bool = generate_primes(c_less)
    primes_list = []
    for i in range(2, len(primes_bool)):
        if primes_bool[i]:
            primes_list += [i]

    rads = [1] * (c_less + 1)
    for i in range(c_less + 1):
        rads[i] = rad(i, primes_list)

    sum_c = 0
    for a in range(1, c_less):
        rad_a = rads[a]
        if a % 2 == 1:
            r = range(1, min(a, c_less - a))
        else:
            r = range(1, min(a, c_less - a), 2)
        for b in r:
            c = a + b
            if rad_a * rads[b] * rads[c] < c and gcd(rad_a, rads[b]) == 1:
                sum_c += c

    return sum_c


if __name__ == "__main__":
    print(f"{solution() = }")
