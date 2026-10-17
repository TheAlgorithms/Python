"""
Sieve of Sundaram algorithm for finding prime numbers up to a given limit.

The Sieve of Sundaram generates prime numbers by eliminating integers
of the form i + j + 2ij.

Time Complexity: O(n log n)
Space Complexity: O(n)

Reference: https://en.wikipedia.org/wiki/Sieve_of_Sundaram
"""


def sieve_of_sundaram(limit: int) -> list[int]:
    """
    Generate all prime numbers up to a given limit.

    Args:
        limit: Upper bound for finding primes (inclusive).

    Returns:
        List of prime numbers up to the given limit.

    Raises:
        ValueError: If limit is negative.

    Examples:
        >>> sieve_of_sundaram(20)
        [2, 3, 5, 7, 11, 13, 17, 19]
        >>> sieve_of_sundaram(10)
        [2, 3, 5, 7]
        >>> sieve_of_sundaram(2)
        [2]
        >>> sieve_of_sundaram(1)
        []
        >>> sieve_of_sundaram(0)
        []
        >>> sieve_of_sundaram(-1)
        Traceback (most recent call last):
        ...
        ValueError: -1: Invalid input, please enter a non-negative integer.
    """
    if limit < 0:
        msg = f"{limit}: Invalid input, please enter a non-negative integer."
        raise ValueError(msg)

    if limit < 2:
        return []

    upper_bound = (limit - 1) // 2
    marked = [False] * (upper_bound + 1)

    for i in range(1, upper_bound + 1):
        j = i
        while i + j + 2 * i * j <= upper_bound:
            marked[i + j + 2 * i * j] = True
            j += 1

    primes = [2]

    for value in range(1, upper_bound + 1):
        if not marked[value]:
            prime = 2 * value + 1
            if prime <= limit:
                primes.append(prime)

    return primes
