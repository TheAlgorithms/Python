def is_happy_number(number: int) -> bool:
    """
    Check if a number is a happy number.
    https://en.wikipedia.org/wiki/Happy_number
    A happy number is defined by the following process:
    1. Starting with any positive integer, replace the number by
       the sum of the squares of its digits.
    2. Repeat the process until the number equals 1 (happy) or
       it loops endlessly in a cycle (not happy).

    Args:
        number (int): The number to check for happiness.

    Returns:
        bool: True if the number is a happy number, False otherwise.

    Examples:
    >>> is_happy_number(19)
    True
    >>> is_happy_number(4)
    False
    >>> is_happy_number(23)
    True
    >>> is_happy_number(0)
    False
    >>> is_happy_number(-19)
    False
    >>> is_happy_number(19.1)
    False
    >>> is_happy_number("Happy")
    False
    """

    # Create a set to store seen numbers and detect cycles
    seen = set()

    while number != 1 and number not in seen:
        seen.add(number)
        number = sum(int(digit) ** 2 for digit in str(number))

    return number == 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
