"""Sieve of Eratosthones."""

import math

N = int(input("Enter n: "))


def sieve(n):
    """Sieve of Eratosthones."""
    l = [True] * (n + 1)
    prime = []
    start = 2
    end = int(math.sqrt(n))
    while start <= end:
        if l[start] is True:
            prime.append(start)
            for i in range(start * start, n + 1, start):
                if l[i] is True:
                    l[i] = False
        start += 1

    for j in range(end + 1, n + 1):
        if l[j] is True:
            prime.append(j)

    return prime


print(sieve(N))
