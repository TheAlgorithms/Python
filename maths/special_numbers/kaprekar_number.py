import math


def is_kaprekar_number(number: int) -> bool:
    """
    Determine whether a number is a Kaprekar number (excluding powers of 10).

    A Kaprekar number is a positive number such that:
    number^2 = q * 10^m + r, for some m >= 1, q >= 0, 0 <= r < 10^m,
    and number = q + r, with the restriction that it is not a power of 10.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if it's a Kaprekar number, else False.

    Examples:
        >>> is_kaprekar_number(45)
        True
        >>> is_kaprekar_number(9)
        True
        >>> is_kaprekar_number(10)
        False
        >>> is_kaprekar_number(1)
        True
    """
    if number == 1:
        return True
    if number <= 0 or math.log10(number).is_integer():
        return False  # Disallow powers of 10 (e.g., 10, 100, 1000)

    square = str(number**2)
    for i in range(1, len(square)):
        left, right = square[:i], square[i:]
        if number == int(left or "0") + int(right):
            return True
    return False
