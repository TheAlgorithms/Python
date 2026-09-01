"""Prime number checker."""


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    >>> is_prime(2)
    True
    >>> is_prime(17)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
