"""
Project Euler Problem 134: https://projecteuler.net/problem=134

Consider the consecutive primes p1 = 19, p2 = 23.
It can be verified that 1219 is the smallest number such
that the last digits are formed by p1 whilst also being divisible by p2.

In fact, with the exception of p1 = 3 and p2 = 5,
for every pair of consecutive primes, p2 > p1, there exist values of n
for which the last digits are formed by p1 and n is divisible by p2.
Let S be the smallest of these values of n.

Find the sum of all S for every pair of consecutive primes with 5 < p1 < 1000000.
"""

from math import log10, sqrt


def extended_euclid(number1: int, number2: int) -> tuple:
    """
    Return the solution to the diophantine equation a*x + b*y = gcd(a, b)
    >>> extended_euclid(3, 11)
    (1, 4, -1)
    """
    a, b = number1, number2
    if b == 0:
        # a, x, y
        return a, 1, 0

    d, x1, y1 = extended_euclid(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return d, x, y


def modular_inverse(number1: int, number2: int) -> int:
    """
    Find the integer x (modular n) such that a * x + n * y = 1
    >>> modular_inverse(3, 11)
    4
    """
    a, n = number1, number2
    d, x, y = extended_euclid(a, n)
    if d != 1:
        return -1
    return (x + n) % n


def chinese_reminder(reminders: list[int], modulos: list[int]) -> int:
    """
    Find chinese reminder of the system a1,...,an (integer list a)
    modular p1,...,pn (integer list p)
    >>> chinese_reminder([2, 3, 2], [3, 5, 7])
    23
    """
    a, p = reminders, modulos
    k = len(p)
    inv = [list(range(k)) for _ in range(k)]
    for i in range(k):
        for j in range(k):
            if i != j:
                inv[i][j] = modular_inverse(p[i], p[j])

    x = list(range(k))
    for i in range(k):
        x[i] = a[i]
        for j in range(i):
            x[i] = inv[j][i] * (x[i] - x[j])
            x[i] %= p[i]
            if x[i] < 0:
                x[i] += p[i]

    ans = x[0]
    prod = 1
    total_prod = 1
    for i in range(k):
        total_prod *= p[i]

    for i in range(1, k):
        prod *= p[i - 1]
        ans += x[i] * prod
        ans %= total_prod
    return ans


def segmented_sieve(left: int, right: int) -> list[int]:
    """
    Find prime numbers in the range [left, right] by applying sieve algorithm
    >>> segmented_sieve(1000000, 1000100)
    [1000003, 1000033, 1000037, 1000039, 1000081, 1000099]
    """
    q = int(sqrt(right)) + 1
    mark = [True] * q
    primes = []
    for p in range(2, q):
        if mark[p]:
            primes.append(p)
            for j in range(p * p, q, p):
                mark[j] = False

    mark = [True] * (right - left + 1)
    for p in primes:
        start = max(p, (left + p - 1) // p) * p
        for j in range(start, right + 1, p):
            mark[j - left] = False
    if left == 1:
        mark[0] = False

    ans = []
    for i in range(left, right + 1):
        if mark[i - left]:
            ans.append(i)
    return ans


def get_s(p1: int, p2: int) -> int:
    """
    Find the smallest number such that the last digits are
    formed by p1 and divisible by p2
    >>> get_s(19, 23)
    1219
    """
    k = int(log10(p1)) + 1
    a = [0, p1]
    p = [p2, 10**k]
    return chinese_reminder(a, p)


def solution(left: int = 5, right: int = 1000000) -> int:
    """
    Find the sum of all S for every pair of consecutive primes
    in the range [left, right].
    >>> solution(5, 100)
    69155
    """
    primes = segmented_sieve(left, right + 500)
    n = len(primes)
    res = 0
    for i in range(n - 1):
        if left <= primes[i] <= right:
            res += get_s(primes[i], primes[i + 1])
    return res


if __name__ == "__main__":
    print(f"{solution() = }")
