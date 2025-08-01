def is_power(n: int, k: int) -> bool:
    """
    Checks if a given integer k is a power of another integer n.

    This function determines if there exists an integer x such that n^x = k.
    It handles positive integers only and raises an error for non-positive inputs.
    For more information, see: https://en.wikipedia.org/wiki/Power_of_two

    Args:
        n: The base integer (must be a positive integer).
        k: The number to check if it's a power of n (must be a positive integer).

    Returns:
        True if k is a power of n, False otherwise.

    Raises:
        ValueError: If n or k are not positive integers.

    Examples:
    >>> is_power(2, 8)
    True
    >>> is_power(3, 81)
    True
    >>> is_power(10, 1)
    True
    >>> is_power(5, 120)
    False
    >>> is_power(1, 1)
    True
    >>> is_power(1, 5)
    False
    >>> is_power(0, 5)
    Traceback (most recent call last):
        ...
    ValueError: Both n and k must be positive integers
    >>> is_power(4, -16)
    Traceback (most recent call last):
        ...
    ValueError: Both n and k must be positive integers
    """
    if n <= 0 or k <= 0:
        raise ValueError("Both n and k must be positive integers")

    if n == 1:
        return k == 1

    # Repeatedly divide k by n until it's no longer divisible.
    while k % n == 0:
        k //= n

    # If k has been reduced to 1, it was a power of n.
    return k == 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
