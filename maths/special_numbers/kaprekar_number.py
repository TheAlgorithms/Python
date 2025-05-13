def is_kaprekar_number(n: int) -> bool:
    """
    Determine whether a number is a Kaprekar number (excluding powers of 10).

    A Kaprekar number is a positive number n such that:
    n^2 = q * 10^m + r, for some m >= 1, q >= 0, 0 <= r < 10^m,
    and n = q + r, with the restriction that n is not a power of 10.

    Args:
        n (int): The number to check.

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
    if n == 1:
        return True
    if n <= 0 or (n % 10 == 0 and n == 10 ** len(str(n))):
        return False  # Disallow powers of 10 (e.g., 10, 100)

    square = str(n ** 2)
    for i in range(1, len(square)):
        left, right = square[:i], square[i:]
        if n == int(left or "0") + int(right):
            return True
    return False
