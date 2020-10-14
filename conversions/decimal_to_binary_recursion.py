def binary_recursive(decimal: int) -> str:
    """
    Take a positive integer value and return its binary equivalent.
    >>> binary_recursive(1000)
    '1111101000'
    >>> binary_recursive("72")
    '1001000'
    >>> binary_recursive("number")
    Traceback (most recent call last):
    ...
    ValueError: invalid literal for int() with base 10: 'number'
    """
    decimal = int(decimal)
    if decimal in (0, 1):  # Exit cases for the recursion
        return str(decimal)
    div, mod = divmod(decimal, 2)
    return binary_recursive(div) + str(mod)


def main(number: str) -> str:
    """
    Take an integer value and raise ValueError for wrong inputs,
    call the function above and return the output with prefix "0b" & "-0b"
    for positive and negative integers respectively.
    >>> main(0)
    '0b0'
    >>> main(40)
    '0b101000'
    >>> main(-40)
    '-0b101000'
    >>> main(40.8)
    Traceback (most recent call last):
    ...
    ValueError: Input value is not an integer
    >>> main("forty")
    Traceback (most recent call last):
    ...
    ValueError: Input value is not an integer
    """
    number = str(number).strip()
    if not number:
        raise ValueError("No input value was provided")
    negative = "-" if number.startswith("-") else ""
    number = number.lstrip("-")
    if not number.isnumeric():
        raise ValueError("Input value is not an integer")
    return f"{negative}0b{binary_recursive(int(number))}"


if __name__ == "__main__":
    from doctest import testmod

    testmod()
