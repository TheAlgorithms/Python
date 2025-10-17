def is_armstrong_number(number: int) -> bool:
    """
    Check whether a non-negative integer is an Armstrong (narcissistic) number.

    An Armstrong number is a number that is the sum of its own digits each raised
    to the power of the number of digits in the number.

    Reference:
        Narcissistic number (Armstrong number) — Wikipedia
        https://en.wikipedia.org/wiki/Narcissistic_number

    >>> is_armstrong_number(0)
    True
    >>> is_armstrong_number(1)
    True
    >>> is_armstrong_number(153)
    True
    >>> is_armstrong_number(370)
    True
    >>> is_armstrong_number(9474)
    True
    >>> is_armstrong_number(9475)
    False
    >>> is_armstrong_number(-1)  # negative numbers are not considered Armstrong
    False
    """
    # Only non-negative integers are considered
    if number < 0:
        return False

    # Convert to string to count digits
    digits = str(number)
    power = len(digits)

    # Sum of each digit raised to the 'power'
    total = sum(int(d) ** power for d in digits)

    return total == number
