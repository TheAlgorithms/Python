def is_happy_number(number: int) -> bool:
    """
    A happy number is a number which eventually reaches 1 when replaced by the sum of
    the squares of its digits.

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
    ValueError: Input must be a positive integer, got 0.
    >>> is_happy_number(-19)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a positive integer, got -19.
    >>> is_happy_number(19.1)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a positive integer, got 19.1.
    >>> is_happy_number("happy")
    Traceback (most recent call last):
        ...
    ValueError: Input must be a positive integer, got 'happy'.
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError(f"Input must be a positive integer, got {number}.")

    seen = set()
    while number != 1 and number not in seen:
        seen.add(number)
        number = sum(int(digit) ** 2 for digit in str(number))
    return number == 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
