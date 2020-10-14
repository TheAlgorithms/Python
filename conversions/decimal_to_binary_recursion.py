def binary_recursive(decimal: int) -> str:
    """
    Take a positive integer value and return its binary equivalent.
    >>> binary_recursive(1000)
    '1111101000'
    >>> binary_recursive("72")
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for //: 'str' and 'int'
    >>> binary_recursive("number")
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for //: 'str' and 'int'
    """
    # Initialize exit base of the recursion function
    if decimal == 1 or decimal == 0:
        return str(decimal)
    return binary_recursive(decimal // 2) + str(decimal % 2)


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
    negative = False

    if number.startswith("-"):
        negative = True
        number = number[1:]

    if number.isnumeric():
        if negative:
            binary = "-0b" + binary_recursive(int(number))
        else:
            binary = "0b" + binary_recursive(int(number))
        return binary
    else:
        raise ValueError("Input value is not an integer")


if __name__ == "__main__":
    from doctest import testmod

    testmod()
