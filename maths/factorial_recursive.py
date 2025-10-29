"""
Recursive factorial implementation.

Reference: https://en.wikipedia.org/wiki/Factorial
"""

def factorial(number: int) -> int:
    """
    Calculate the factorial of a non-negative integer recursively.

    Parameters:
        number (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the input number.

    Raises:
        ValueError: If the input number is negative.

    Examples:
        >>> factorial(0)
        1
        >>> factorial(1)
        1
        >>> factorial(5)
        120
    """
    if number < 0:
        raise ValueError("number must be non-negative")
    if number <= 1:
        return 1
    return number * factorial(number - 1)


if __name__ == "__main__":
    print(factorial(5))
