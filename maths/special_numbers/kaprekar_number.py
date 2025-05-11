def is_kaprekar_number(n: int) -> bool:
    """
    Determine whether a number is a Kaprekar number.

    A Kaprekar number is one where the square can be split into parts
    that sum to the original number.

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
    """
    square = str(n ** 2)
    for i in range(1, len(square)):
        left, right = square[:i], square[i:]
        if int(right) == 0:
            continue
        if n == int(left or "0") + int(right):
            return True
    return n == 1


if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
