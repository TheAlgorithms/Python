"""
This module provides a division function with input validation.

The divide_numbers function performs division between two numbers
with explicit validation for zero denominators, providing clearer
error messages for educational purposes.
"""


def divide_numbers(a: float, b: float) -> float:
    """
    Divide two numbers with validation for zero denominator.

    This function performs division between two numbers and includes
    explicit validation to prevent division by zero, providing a
    user-friendly error message that is especially helpful for
    beginners learning about error handling.

    Args:
        a: The dividend (numerator) - the number to be divided.
        b: The divisor (denominator) - the number to divide by.

    Returns:
        The result of dividing a by b.

    Raises:
        ValueError: If b (denominator) is zero.

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
        ValueError: Cannot divide by zero. Please provide a non-zero denominator.

        >>> divide_numbers(0, 5)
        0.0
    """
    if b == 0:
        raise ValueError(
            "Cannot divide by zero. Please provide a non-zero denominator."
        )
    return a / b


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
