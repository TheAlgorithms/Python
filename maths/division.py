"""
This module provides a function for dividing two numbers with proper input validation.

The divide_numbers function includes validation to prevent division by zero errors,
providing clear error messages for better user experience.
"""


def divide_numbers(numerator: float, denominator: float) -> float:
    """
    Divide two numbers with input validation for zero denominator.

    Args:
        numerator: The numerator (dividend)
        denominator: The denominator (divisor)

    Returns:
        float: The result of numerator divided by denominator

    Raises:
        ValueError: If denominator is zero

    Examples:
        >>> divide_numbers(10, 2)
        5.0
        >>> divide_numbers(15, 3)
        5.0
        >>> divide_numbers(10, 0)
        Traceback (most recent call last):
            ...
        ValueError: Cannot divide by zero. Please provide a non-zero denominator.
    """
    if denominator == 0:
        raise ValueError(
            "Cannot divide by zero. Please provide a non-zero denominator."
        )
    return numerator / denominator


if __name__ == "__main__":
    import doctest

    doctest.testmod()
