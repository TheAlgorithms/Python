def find_previous_power_of_two(number: int) -> int:
    """
    Find the largest power of two that is less than or equal to a given integer.
    https://stackoverflow.com/questions/1322510

    >>> [find_previous_power_of_two(i) for i in range(18)]
    [0, 1, 2, 2, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 16, 16]
    >>> find_previous_power_of_two(-5)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a non-negative integer
    >>> find_previous_power_of_two(10.5)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a non-negative integer
    """
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer")
    if number == 0:
        return 0
    power = 1
    while power <= number:
        power <<= 1  # Equivalent to multiplying by 2
    return power >> 1 if number > 1 else 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
