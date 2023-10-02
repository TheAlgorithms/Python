def add_numbers(int_1: int, int_2: int) -> int:
    """
    Add two integers using bitwise operations.

    Args:
        int_1 (int): The first integer.
        int_2 (int): The second integer.

    Returns:
        int: The sum of the two integers.
    """
    while int_2 > 0:
        carry = int_1 & int_2
        int_1 = int_1 ^ int_2  # Sum
        int_2 = carry << 1
    return int_1
