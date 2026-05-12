"""
Armstrong Number (Narcissistic Number) Checker

An Armstrong number is a number that is equal to the sum of its own digits
each raised to the power of the number of digits.

For example:
- 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 (3 digits)
- 9474 = 9^4 + 4^4 + 7^4 + 4^4 = 6561 + 256 + 2401 + 256 = 9474 (4 digits)

Author: Rukaiya Khan
"""


def is_armstrong_number(number: int) -> bool:
    """
    Check if a number is an Armstrong number.

    Args:
        number: The number to check (must be non-negative)

    Returns:
        True if the number is an Armstrong number, False otherwise

    Examples:
        >>> is_armstrong_number(0)
        True
        >>> is_armstrong_number(1)
        True
        >>> is_armstrong_number(153)
        True
        >>> is_armstrong_number(370)
        True
        >>> is_armstrong_number(371)
        True
        >>> is_armstrong_number(407)
        True
        >>> is_armstrong_number(9474)
        True
        >>> is_armstrong_number(123)
        False
        >>> is_armstrong_number(100)
        False
    """
    if number < 0:
        return False

    # Convert to string to easily get digits
    num_str = str(number)
    num_digits = len(num_str)

    # Calculate sum of each digit raised to power of number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)

    return sum_of_powers == number


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Test with some examples
    print("Armstrong numbers up to 1000:")
    for num in range(1000):
        if is_armstrong_number(num):
            print(num, end=" ")
    print()
