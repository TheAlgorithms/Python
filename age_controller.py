"""Age Controller Module

This module provides functionality to validate and process age input.
Related to issue #12809.
"""


def validate_age(age):
    """Validate and process age input.

    This function validates that the provided age is a valid positive integer
    within a reasonable range (0-150 years).

    Args:
        age: The age input to validate (can be int, str, or float)

    Returns:
        int: The validated age as an integer

    Raises:
        ValueError: If age is invalid, negative, or out of range
        TypeError: If age cannot be converted to a number

    Examples:
        >>> validate_age(25)
        25
        >>> validate_age('30')
        30
        >>> validate_age(45.0)
        45
        >>> validate_age(-5)
        Traceback (most recent call last):
            ...
        ValueError: Age must be a positive number
        >>> validate_age(200)
        Traceback (most recent call last):
            ...
        ValueError: Age must be between 0 and 150
        >>> validate_age('invalid')
        Traceback (most recent call last):
            ...
        ValueError: Age must be a valid number
    """
    try:
        # Convert to float first to handle string numbers
        age_float = float(age)

        # Check if it's a whole number
        if age_float != int(age_float):
            age_int = int(age_float)
        else:
            age_int = int(age_float)

    except (ValueError, TypeError):
        raise ValueError("Age must be a valid number")

    # Validate range
    if age_int < 0:
        raise ValueError("Age must be a positive number")

    if age_int > 150:
        raise ValueError("Age must be between 0 and 150")

    return age_int


if __name__ == "__main__":
    import doctest

    doctest.testmod()
