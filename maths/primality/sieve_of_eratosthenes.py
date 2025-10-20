# Sieve of Eratosthenes: an efficient algorithm to compute all prime numbers up to n.
# It repeatedly marks multiples of each prime as non-prime, starting from 2.
# This method is suitable for n up to about 10**7 on typical hardware.
# Wikipedia URL - https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def sieve_of_eratosthenes(n: int) -> list[int]:
    """
    Compute all prime numbers up to and including n using the Sieve of Eratosthenes.

    Parameters
    ----------
    n : int
        Upper bound (inclusive) of the range in which to find prime numbers.
        Expected to be a non-negative integer. If n < 2 the function returns an empty list.

    Returns
    -------
    list[int]
        A list of primes in ascending order that are <= n.

    Examples
    --------
    >>> sieve_of_eratosthenes(10)
    [2, 3, 5, 7]
    >>> sieve_of_eratosthenes(1)
    []
    >>> sieve_of_eratosthenes(2)
    [2]
    >>> sieve_of_eratosthenes(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    if n < 2:
        return []

    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    return [p for p in range(2, n + 1) if prime[p]]


if __name__ == "__main__":
    print(sieve_of_eratosthenes(35))
