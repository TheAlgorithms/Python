def sum_of_digits(number: int) -> int:
    """
    Return the sum of decimal digits of a non-negative integer.

    Parameters:
        number (int): A non-negative integer whose digits will be summed.

    Returns:
        int: Sum of the decimal digits of `number`.

    Examples:
    >>> sum_of_digits(0)
    0
    >>> sum_of_digits(9)
    9
    >>> sum_of_digits(12345)
    15
    """
    if number < 0:
        raise ValueError("number must be a non-negative integer")

    total = 0
    while number:
        total += number % 10
        number //= 10
    return total


if __name__ == "__main__":
    # simple demonstration
    print(sum_of_digits(12345))  # expected 15
