def add_numbers(a: int, b: int) -> int:
    """
    Add two integers using bitwise operations.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of the two integers.
    """
    while b > 0:
        carry = a & b
        a = a ^ b  # Sum
        b = carry << 1
    return a
