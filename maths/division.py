"""
Division Algorithm with input validation for zero denominator.

This module provides a function to perform division with proper
error handling for edge cases, especially for beginners learning
algorithms.
"""


def divide_numbers(a: int | float, b: int | float) -> float:
    """
    Divide two numbers with validation for zero denominator.

    This function performs division of 'a' by 'b' with explicit validation
    to raise a ValueError when attempting to divide by zero. This makes the
    function more user-friendly and helps beginners understand error handling.

    Args:
        a: The dividend (numerator)
        b: The divisor (denominator)

    Returns:
        float: The result of dividing a by b

    Raises:
        ValueError: If b (denominator) is zero

    Examples:
        >>> divide_numbers(10, 2)
        5.0
        >>> divide_numbers(7, 2)
        3.5
        >>> divide_numbers(5, 0)
        Traceback (most recent call last):
            ...
        ValueError: Cannot divide by zero. Please provide a non-zero denominator.
    """
    if b == 0:
        raise ValueError(
            "Cannot divide by zero. Please provide a non-zero denominator."
        )
    return a / b
