"""
Project Euler Problem 60: https://projecteuler.net/problem=60

Problem Statement:
The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in any order
the result will always be prime.

For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest
sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which
any two primes concatenate to produce another prime.

Solution:
    Simply check all prime numbers till the limit.

"""

from math import floor, sqrt


def primes_till(number: int) -> set[int]:
    """
    Returns a set of prime numbers till the number "number"

    >>> primes_till(10)
    {2, 3, 5, 7}
    >>> primes_till(20)
    {2, 3, 5, 7, 11, 13, 17, 19}
    """

    marked = [0] * (number + 1)
    value = 3
    s = {2}
    while value < number + 1:
        if marked[value] == 0:
            s.add(value)
            i = value
            while i < number + 1:
                marked[i] = 1
                i += value
        value += 2
    return s


def is_prime(number: int) -> bool:
    """
    Returns True if "number" is a prime number. Else, returns False

    >>> is_prime(10)
    False
    >>> is_prime(23)
    True
    """

    if number >= 2:
        for i in range(2, floor(sqrt(number) + 1)):
            if number % i == 0:
                return False
        return True
    else:
        return False


def prime_pair_test(number1: int, number2: int) -> bool:
    """
    Checks whether "number1number2" and "number2number1" are both prime numbers or not

    >>> prime_pair_test(7, 109)
    True
    >>> prime_pair_test(15, 8)
    False
    """
    return is_prime(int(str(number1) + str(number2))) and is_prime(
        int(str(number2) + str(number1))
    )


def solution(limit: int = 10_000) -> int:
    """
    Checks for all prime numbers till 5 that satisfy "prime_pair_test" are collected

    >>> solution()
    26033
    """

    set_of_primes = list(primes_till(limit))

    for a in range(len(set_of_primes)):
        prime_a = set_of_primes[a]
        for b in range(a + 1, len(set_of_primes)):
            prime_b = set_of_primes[b]
            if prime_pair_test(prime_a, prime_b):
                for c in range(b + 1, len(set_of_primes)):
                    prime_c = set_of_primes[c]
                    if prime_pair_test(prime_b, prime_c) and prime_pair_test(
                        prime_a, prime_c
                    ):
                        for d in range(c + 1, len(set_of_primes)):
                            prime_d = set_of_primes[d]
                            if (
                                prime_pair_test(prime_c, prime_d)
                                and prime_pair_test(prime_b, prime_d)
                                and prime_pair_test(prime_a, prime_d)
                            ):
                                for e in range(d + 1, len(set_of_primes)):
                                    prime_e = set_of_primes[e]
                                    if (
                                        prime_pair_test(prime_d, prime_e)
                                        and prime_pair_test(prime_c, prime_e)
                                        and prime_pair_test(prime_b, prime_e)
                                        and prime_pair_test(prime_a, prime_e)
                                    ):
                                        return (
                                            prime_a
                                            + prime_b
                                            + prime_c
                                            + prime_d
                                            + prime_e
                                        )
    return 0


if __name__ == "__main__":
    print(solution())
