def is_happy_number(number: int) -> bool:
    """
    Check if a number is a happy number.

    :param number: The number to check for happiness.
    :return: True if the number is a happy number, False otherwise.

    A happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit.

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
    ValueError: Input must be a positive integer
    >>> is_happy_number(-19)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a positive integer
    >>> is_happy_number(19.1)
    Traceback (most recent call last):
        ...
    TypeError: Input value of [number=19.1] must be an integer
    >>> is_happy_number("happy")
    Traceback (most recent call last):
        ...
    TypeError: Input value of [number=happy] must be an integer
    """
    if not isinstance(number, int):
        msg = f"Input value of [number={number}] must be an integer"
        raise TypeError(msg)
    if number <= 0:
        raise ValueError("Input must be a positive integer")

    def get_next(number):
        next_num = 0
        while number > 0:
            number, digit = divmod(number, 10)
            next_num += digit**2
        return next_num

    seen = set()
    while number != 1 and number not in seen:
        seen.add(number)
        number = get_next(number)

    return number == 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
