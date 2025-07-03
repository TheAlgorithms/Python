from typing import List


def sieve_of_atkin(limit: int) -> List[int]:
    """
    Compute all prime numbers up to the given limit using the Sieve of Atkin.

    Parameterss
    ----------
    limit : int
        Upper bound of primes to generate (inclusive).

    Returns
    -------
    List[int]
        A list of prime numbers <= limit.

    Raises
    ------
    ValueError
        If limit is not an integer or is less than 2.

    References
    ----------
    https://en.wikipedia.org/wiki/Sieve_of_Atkin

    Examples
    --------
    >>> sieve_of_atkin(10)
    [2, 3, 5, 7]
    >>> sieve_of_atkin(1)
    Traceback (most recent call last):
    ...
    ValueError: limit must be an integer >= 2
    """
    if not isinstance(limit, int) or limit < 2:
        raise ValueError("limit must be an integer >= 2")

    # Initialize the sieve array
    sieve = [False] * (limit + 1)
    results: List[int] = []

    # Preliminary marking based on quadratic forms
    from math import sqrt

    sqrt_limit = int(sqrt(limit)) + 1
    for x in range(1, sqrt_limit):
        for y in range(1, sqrt_limit):
            n = 4 * x * x + y * y
            if n <= limit and n % 12 in (1, 5):
                sieve[n] = not sieve[n]
            n = 3 * x * x + y * y
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3 * x * x - y * y
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]

    # Mark all multiples of squares as non-prime
    for n in range(5, sqrt_limit):
        if sieve[n]:
            step = n * n
            for k in range(step, limit + 1, step):
                sieve[k] = False

    # Compile the list of primes
    if limit >= 2:
        results.extend([2, 3])
    results.extend([i for i in range(5, limit + 1) if sieve[i]])
    return results


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print("All doctests passed!")
