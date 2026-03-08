def is_happy_number(number: int) -> bool:
    """
    A happy number is a number which eventually reaches 1 when replaced by the sum of
    the square of each digit.

    :param number: The number to check for happiness.
    :return: True if the number is a happy number, False otherwise.

    >>> is_happy_number(19)
    True
    >>> is_happy_number(2)
    False
    >>> is_happy_number(23)
    True
    >>> is_happy_number(1)
    True
    >>> is_happy_number(0)
    Traceback (most recent call last):
        ...
    ValueError: number=0 must be a positive integer
    >>> is_happy_number(-19)
    Traceback (most recent call last):
        ...
    ValueError: number=-19 must be a positive integer
    >>> is_happy_number(19.1)
    Traceback (most recent call last):
        ...
    ValueError: number=19.1 must be a positive integer
    >>> is_happy_number("happy")
    Traceback (most recent call last):
        ...
    ValueError: number='happy' must be a positive integer
    """
    if not isinstance(number, int) or number <= 0:
        msg = f"{number=} must be a positive integer"
        raise ValueError(msg)

    seen = set()
    while number != 1 and number not in seen:
        seen.add(number)
        number = sum(int(digit) ** 2 for digit in str(number))
    return number == 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
