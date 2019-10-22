"""Implementation of Basic Math in Python."""
import math


def prime_factors(n):
    """Find Prime Factors."""
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


def number_of_divisors(n):
    """Calculate Number of Divisors of an Integer."""
    div = 1

    temp = 1
    while n % 2 == 0:
        temp += 1
        n = int(n / 2)
    div = div * (temp)

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        temp = 1
        while n % i == 0:
            temp += 1
            n = int(n / i)
        div = div * (temp)

    return div


def sum_of_divisors(n):
    """Calculate Sum of Divisors."""
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

    return s


def euler_phi(n):
    """Calculte Euler's Phi Function."""
    l = prime_factors(n)
    l = set(l)
    s = n
    for x in l:
        s *= (x - 1) / x
    return s


def main():
    """Print the Results of Basic Math Operations."""
    print(prime_factors(100))
    print(number_of_divisors(100))
    print(sum_of_divisors(100))
    print(euler_phi(100))


if __name__ == "__main__":
    main()
