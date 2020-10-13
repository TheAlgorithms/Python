"""
Problem 50
Url:https://projecteuler.net/problem=50
Statement:
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of
the most consecutive primes?
"""


def is_prime(n: int) -> bool:
    """
    Return True if n is a prime number else False
    >>> is_prime(97)
    True
    >>> is_prime(98)
    False
    """
    for i in range(2, int((n ** 0.5) // 1)):
        if not (n % i):
            return False
    return True


def sieve(n: int) -> list:
    """
    Implements of Sieve of Eratosthenes
    Returns a list of primes numbes above n
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    >>> sieve(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    limit = int((n ** 0.5) // 1)
    primes = range(2, n)
    for i in primes:
        if i == limit:
            break
        else:
            # Remove multiples of N from primes
            primes = list(filter(lambda n: (n % i) or (i == n), primes))
    return primes


def solution(n: int = 1000) -> int:
    """Returns the longgest sum of consecutive primes below n.
    >>> solution(1000)
    961
    >>> solution(1000000)
    997651
    """
    primes = sieve(n)
    l_primes = len(primes)
    j = 0
    longgest = []
    for i in range(int(l_primes // 2), 2, -1):
        j = 0
        while j + i <= l_primes:
            primes_slice = primes[j : j + i]
            sum_slice = sum(primes_slice)
            len_slice = len(primes_slice)
            if sum_slice > n:
                break
            if is_prime(sum_slice) and (sum_slice < n) and (len_slice > len(longgest)):
                longgest = primes_slice
                break
            j += 1
        if longgest:
            # print(f"{longgest}\t{len_l}\t{sum_l}")
            return sum_slice
            break


if __name__ == "__main__":
    print(solution(int(input().strip())))
