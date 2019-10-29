"""Implementation of Basic Math in Python."""
import math


def prime_factors(n: int) -> list:
    """Find Prime Factors.
    >>> prime_factors(100)
    [2, 2, 5, 5]
    """
    pf = []
    while n % 2 == 0:
        pf.append(2)
        n = int(n / 2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            pf.append(i)
            n = int(n / i)
    if n > 2:
        pf.append(n)
    return pf


def number_of_divisors(n: int) -> int:
    """Calculate Number of Divisors of an Integer.
    >>> number_of_divisors(100)
    9
    """
    div = 1
    temp = 1
    while n % 2 == 0:
        temp += 1
        n = int(n / 2)
    div *= temp
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        temp = 1
        while n % i == 0:
            temp += 1
            n = int(n / i)
        div *= temp
    return div


def sum_of_divisors(n: int) -> int:
    """Calculate Sum of Divisors.
    >>> sum_of_divisors(100)
    217
    """
    s = 1
    temp = 1
    while n % 2 == 0:
        temp += 1
        n = int(n / 2)
    if temp > 1:
        s *= (2 ** temp - 1) / (2 - 1)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        temp = 1
        while n % i == 0:
            temp += 1
            n = int(n / i)
        if temp > 1:
            s *= (i ** temp - 1) / (i - 1)
    return int(s)


def euler_phi(n: int) -> int:
    """Calculte Euler's Phi Function.
    >>> euler_phi(100)
    40
    """
    l = prime_factors(n)
    l = set(l)
    s = n
    for x in l:
        s *= (x - 1) / x
    return int(s)


if __name__ == "__main__":
    print(prime_factors(100))
    print(number_of_divisors(100))
    print(sum_of_divisors(100))
    print(euler_phi(100))
