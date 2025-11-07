"""
This module provides a function for dividing two numbers with proper input validation.

The divide_numbers function includes validation to prevent division by zero errors,
providing clear error messages for better user experience.
"""


def divide_numbers(a: float, b: float) -> float:
    """
    Divide two numbers with input validation for zero denominator.

    Args:
        a: The numerator (dividend)
        b: The denominator (divisor)

    Returns:
        float: The result of a divided by b

    Raises:
        ValueError: If b is zero

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
    if b == 0:
        raise ValueError(
            "Cannot divide by zero. Please provide a non-zero denominator."
        )
    return a / b


if __name__ == "__main__":
    import doctest

    doctest.testmod()
