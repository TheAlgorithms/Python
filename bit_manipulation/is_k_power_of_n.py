def is_power(base: int, number: int) -> bool:
    """
    Checks if a given integer `number` is a power of another integer `base`.

    This function determines if there exists an integer x such that base^x = number.
    It handles positive integers only and raises an error for non-positive inputs.
    For more information, see: https://en.wikipedia.org/wiki/Power_of_two

    Args:
        base: The base integer (must be a positive integer).
        number: The number to check if it's a power of base
            (must be a positive integer).

    Returns:
        True if number is a power of base, False otherwise.

    Raises:
        ValueError: If base or number are not positive integers.

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
    ValueError: Both base and number must be positive integers
    >>> is_power(4, -16)
    Traceback (most recent call last):
        ...
    ValueError: Both base and number must be positive integers
    """
    if base <= 0 or number <= 0:
        raise ValueError("Both base and number must be positive integers")

    if base == 1:
        return number == 1

    # Repeatedly divide number by base until it's no longer divisible.
    while number % base == 0:
        number //= base

    # If number has been reduced to 1, it was a power of base.
    return number == 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
