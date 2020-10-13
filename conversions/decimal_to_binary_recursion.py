def binary_recursive(decimal: int) -> str:
    """
    This takes in a positive integer value
    and returns its binary equivalent.
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
    result = binary_recursive(decimal // 2) + str(decimal % 2)
    return str(result)


def main(number: str) -> str:
    """
    This function takes a parameter "number",
    raises a ValueError for wrong inputs,
    calls the function above and returns the output
    with prefix "0b" & "-0b" for positive
    and negative integers respectively.
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
