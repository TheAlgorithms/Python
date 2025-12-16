import random


def miller_rabin_primality_test(n: int, k: int = 5) -> bool:
    """
    Probabilistic primality test using Miller-Rabin algorithm.

    Args:
        n (int): Number to test for primality.
        k (int): Number of iterations for accuracy.

    Returns:
        bool: True if n is probably prime, False if composite.

    Examples:
    >>> miller_rabin_primality_test(2)
    True
    >>> miller_rabin_primality_test(15)
    False
    >>> miller_rabin_primality_test(17)
    True
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
