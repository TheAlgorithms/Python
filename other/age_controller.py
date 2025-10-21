"""Age Controller Module
This module provides functionality to validate and process age input.
Related to issue #12809.
"""


def validate_age(age: float | str) -> int:
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
        ValueError: Age must be between 0 and 150 years
        >>> validate_age('invalid')
        Traceback (most recent call last):
            ...
        ValueError: Invalid age format
        >>> validate_age(25.5)
        Traceback (most recent call last):
            ...
        ValueError: Age must be a whole number
    """
    # Convert age to appropriate numeric type
    age_int = int(age) if isinstance(age, int | float) else int(str(age))

    # Validate that the age is a whole number if it was a float
    if isinstance(age, float) and age != age_int:
        msg = "Age must be a whole number"
        raise ValueError(msg)

    # Validate age is positive
    if age_int < 0:
        msg = "Age must be a positive number"
        raise ValueError(msg)

    # Validate age is within reasonable range
    if age_int > 150:
        msg = "Age must be between 0 and 150 years"
        raise ValueError(msg)

    return age_int
