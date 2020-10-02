# flake8: noqa

"""
Sieve of Eratosthenes

Input : n =10
Output: 2 3 5 7

Input : n = 20
Output: 2 3 5 7 11 13 17 19

you can read in detail about this at
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""


def prime_sieve_eratosthenes(num):
    """
    print the prime numbers up to n

    >>> prime_sieve_eratosthenes(10)
    2,3,5,7,
    >>> prime_sieve_eratosthenes(20)
    2,3,5,7,11,13,17,19,
    """

    m=(n-1)//2
    b=[True]*m
    i,p,primess = 0,3,[2]
    while p*p < n:
        if b[i]:
            primes.append(p)
            j = 2*i*i + 6*i + 3
            while j < m:
                b[j] = False
                j = j + 2*i + 3
        i+=1; p+=2
    while i < m:
        if b[i]:
            primes.append(p)
        i+=1; p+=2
    print(*primes)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    num = int(input())

    prime_sieve_eratosthenes(num)
