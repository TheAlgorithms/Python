"""
The number 197 is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73,
79, and 97.
How many circular primes are there below one million?

To solve this problem in an efficient manner, we will first mark all the primes
below 1 million using the Seive of Eratosthenes.  Then, out of all these primes,
we will rule out the numbers which contain an even digit.  After this we will
generate each circular combination of the number and check if all are prime.
"""
from __future__ import annotations

seive = [True] * 1000001
i = 2
while i * i <= 1000000:
    if seive[i]:
        for j in range(i * i, 1000001, i):
            seive[j] = False
    i += 1


def is_prime(n: int) -> bool:
    """
    For 2 <= n <= 1000000, return True if n is prime.
    >>> is_prime(87)
    False
    >>> is_prime(23)
    True
    >>> is_prime(25363)
    False
    """
    return seive[n]


def contains_an_even_digit(n: int) -> bool:
    """
    Return True if n contains an even digit.
    >>> contains_an_even_digit(0)
    True
    >>> contains_an_even_digit(975317933)
    False
    >>> contains_an_even_digit(-245679)
    True
    """
    return any(digit in "02468" for digit in str(n))


def find_circular_primes(limit: int = 1000000) -> list[int]:
    """
    Return circular primes below limit.
    >>> len(find_circular_primes(100))
    13
    >>> len(find_circular_primes(1000000))
    55
    """
    result = [2]  # result already includes the number 2.
    for num in range(3, limit + 1, 2):
        if is_prime(num) and not contains_an_even_digit(num):
            str_num = str(num)
            list_nums = [int(str_num[j:] + str_num[:j]) for j in range(len(str_num))]
            if all(is_prime(i) for i in list_nums):
                result.append(num)
    return result


if __name__ == "__main__":
    print(f"{len(find_circular_primes()) = }")
