# Optimized Sieve of Eratosthenes: An efficient algorithm to compute all prime numbers up to n.
# This version skips even numbers after 2, improving both memory and time usage.
# It is particularly efficient for larger n (e.g., up to 10**8 on typical hardware).
# Wikipedia URL - https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

from math import isqrt

def optimized_sieve(n: int) -> list[int]:
    """
    Compute all prime numbers up to and including n using an optimized Sieve of Eratosthenes.

    This implementation skips even numbers after 2 to reduce memory and runtime by about 50%.

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
    >>> optimized_sieve(10)
    [2, 3, 5, 7]
    >>> optimized_sieve(1)
    []
    >>> optimized_sieve(2)
    [2]
    >>> optimized_sieve(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    if n < 2:
        return []

    # Handle 2 separately, then consider only odd numbers
    primes = [2] if n >= 2 else []

    # Only odd numbers from 3 to n
    size = (n - 1) // 2
    is_prime = [True] * (size + 1)
    limit = isqrt(n)

    for i in range((limit - 1) // 2 + 1):
        if is_prime[i]:
            p = 2 * i + 3
            # Start marking from p^2, converted to index
            start = (p * p - 3) // 2
            for j in range(start, size + 1, p):
                is_prime[j] = False

    primes.extend(2 * i + 3 for i in range(size + 1) if is_prime[i])
    return primes


if __name__ == "__main__":

    print(optimized_sieve(50))
