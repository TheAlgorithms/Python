def is_armstrong_number(number: int) -> bool:
    """
    Check if a number is an Armstrong number.
    An Armstrong number is a number that is equal to the sum
    of its own digits each raised to the power of the number of digits.

    Wikipedia: https://en.wikipedia.org/wiki/Narcissistic_number

    >>> is_armstrong_number(153)
    True
    >>> is_armstrong_number(123)
    False
    """
    digits = str(number)
    power = len(digits)
    return number == sum(int(digit) ** power for digit in digits)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
