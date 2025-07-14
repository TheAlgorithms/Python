def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def goldbach(n: int) -> tuple[int, int] | None:
    """
    Returns a pair of prime numbers that sum to the given even integer n,
    according to Goldbach's Conjecture.

    Example:
        goldbach(10) -> (3, 7)
    """
    if n <= 2 or n % 2 != 0:
        return None
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            return (i, n - i)
    return None
