def gcd_iterative(first_number: int, second_number: int) -> int:
    """
    Compute the greatest common divisor (GCD) of two numbers iteratively.

    Examples:
    >>> gcd_iterative(48, 18)
    6
    >>> gcd_iterative(7, 5)
    1
    """
    while second_number != 0:
        first_number, second_number = second_number, first_number % second_number
    return first_number
