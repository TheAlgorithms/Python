def int_to_base(number, base_of_interest):
    """
    Return base "base_of_interest" representation for int "number".

    https://en.wikipedia.org/wiki/Radix

    Parameters:
        number (int): The original number in base 10.
        base_of_interest (int): The base to convert "number" from base 10 to.

    Returns:
        str: "number" expressed in base "base_of_interest".

    Examples:
    >>> int_to_base(235543, 23)
    'J860'
    >>> int_to_base(56, 2)
    '111000'
    >>> int_to_base(45, 10)
    '45'
    >>> int_to_base(873.6, 13)
    Traceback (most recent call last):
        ...
    TypeError: number must be an integer from base 2 to 36
    >>> int_to_base("657", 13)
    Traceback (most recent call last):
        ...
    TypeError: number must be an integer from base 2 to 36
    >>> int_to_base(23, "23")
    Traceback (most recent call last):
        ...
    TypeError: base_of_interest must be an integer from 2 to 36

    Note:
    - "base_of_interest" most be between 2 and 36 inclusive
    """

    if isinstance(number, int):
        raise TypeError("number must be an integer from base 2 to 36")
    if isinstance(base_of_interest, int):
        raise TypeError("base_of_interest must be an integer from 2 to 36")
    if (base_of_interest > 36) or (base_of_interest < 2):
        raise ValueError("base_of_number must be between 2 and 36 inclusive")

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while number > 0:
        number, remainder = divmod(number, base_of_interest)
        result = digits[remainder] + result

    if result == "":
        result = "0"

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
