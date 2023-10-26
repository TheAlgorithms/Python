# https://stackoverflow.com/questions/1322510/given-an-integer-how-do-i-find-the-next-largest-power-of-two-using-bit-twiddlin


def find_previous_power_of_two(number: int) -> int:
    """
    Find the largest power of two that is less than or equal to a given integer.

    >>> find_previous_power_of_two(10)
    8
    >>> find_previous_power_of_two(16)
    16
    >>> find_previous_power_of_two(5)
    4
    >>> find_previous_power_of_two(1)
    1
    >>> find_previous_power_of_two(0)
    0
    >>> find_previous_power_of_two(-5)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a non-negative integer
    >>> find_previous_power_of_two(10.5)
    Traceback (most recent call last):
        ...
    TypeError: Input must be an integer
    """

    if not isinstance(number, int):
        raise TypeError("Input must be an integer")

    if number < 0:
        raise ValueError("Input must be a non-negative integer")

    if number == 0:
        return 0

    power = 1
    while power <= number:
        power <<= 1  # Equivalent to multiplying by 2

    return power >> 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
