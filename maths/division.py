"""
This module provides a division function with input validation.

The divide_numbers function performs division between two numbers
with explicit validation for zero denominators, providing clearer
error messages for educational purposes.
"""


def divide_numbers(numerator: float, denominator: float) -> float:
    """
    Divide two numbers with validation for zero denominator.

    This function performs division between two numbers and includes
    explicit validation to prevent division by zero, providing a
    user-friendly error message that is especially helpful for
    beginners learning about error handling.

    Args:
        numerator: The dividend - the number to be divided.
        denominator: The divisor - the number to divide by.

    Returns:
        The result of dividing numerator by denominator.

    Raises:
        ValueError: If denominator is zero.

    Examples:
        >>> divide_numbers(10, 2)
        5.0

        >>> divide_numbers(15, 3)
        5.0

        >>> divide_numbers(-10, 2)
        -5.0

        >>> divide_numbers(7, 2)
        3.5

        >>> divide_numbers(10, 0)
        Traceback (most recent call last):
            ...
        ValueError: Cannot divide by zero. Please provide a non-zero
        denominator.

        >>> divide_numbers(0, 5)
        0.0
    """
    if denominator == 0:
        raise ValueError(
            "Cannot divide by zero. Please provide a non-zero denominator."
        )
    return numerator / denominator


if __name__ == "__main__":
    # Example usage
    print("Division Examples:")
    print(f"10 / 2 = {divide_numbers(10, 2)}")
    print(f"15 / 3 = {divide_numbers(15, 3)}")
    print(f"-10 / 2 = {divide_numbers(-10, 2)}")
    print(f"7 / 2 = {divide_numbers(7, 2)}")
    print(f"0 / 5 = {divide_numbers(0, 5)}")

    # Test zero division error
    try:
        divide_numbers(10, 0)
    except ValueError as e:
        print(f"Error caught: {e}")
