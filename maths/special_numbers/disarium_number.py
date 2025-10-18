def is_disarium(num: int) -> bool:
    """
    Check if a number is a Disarium number.

    A Disarium number is a number in which the sum of its digits
    powered with their respective positions is equal to the number itself.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if num is a Disarium number, False otherwise.

    Examples:
    >>> is_disarium(135)
    True
    >>> is_disarium(89)
    True
    >>> is_disarium(75)
    False
    >>> is_disarium(9)
    True
    """
    digits = str(num)
    total = 0
    position = 1

    for i in digits:
        total += int(i) ** position
        position += 1

    return total == num


if __name__ == "__main__":
    import doctest

    doctest.testmod()
