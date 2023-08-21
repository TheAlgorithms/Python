"""Convert a Decimal Number to a Binary Number."""


def decimal_to_binary_iterative(num: int) -> str:
    """
    Convert an Integer Decimal Number to a Binary Number as str.
    >>> decimal_to_binary_iterative(0)
    '0b0'
    >>> decimal_to_binary_iterative(2)
    '0b10'
    >>> decimal_to_binary_iterative(7)
    '0b111'
    >>> decimal_to_binary_iterative(35)
    '0b100011'
    >>> # negatives work too
    >>> decimal_to_binary_iterative(-2)
    '-0b10'
    >>> # other floats will error
    >>> decimal_to_binary_iterative(16.16) # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    TypeError: 'float' object cannot be interpreted as an integer
    >>> # strings will error as well
    >>> decimal_to_binary_iterative('0xfffff') # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    TypeError: 'str' object cannot be interpreted as an integer
    """

    if isinstance(num, float):
        raise TypeError("'float' object cannot be interpreted as an integer")
    if isinstance(num, str):
        raise TypeError("'str' object cannot be interpreted as an integer")

    if num == 0:
        return "0b0"

    negative = False

    if num < 0:
        negative = True
        num = -num

    binary: list[int] = []
    while num > 0:
        binary.insert(0, num % 2)
        num >>= 1

    if negative:
        return "-0b" + "".join(str(e) for e in binary)

    return "0b" + "".join(str(e) for e in binary)


def decimal_to_binary_recursive_helper(decimal: int) -> str:
    """
    Take a positive integer value and return its binary equivalent.
    >>> decimal_to_binary_recursive_helper(1000)
    '1111101000'
    >>> decimal_to_binary_recursive_helper("72")
    '1001000'
    >>> decimal_to_binary_recursive_helper("number")
    Traceback (most recent call last):
        ...
    ValueError: invalid literal for int() with base 10: 'number'
    """
    decimal = int(decimal)
    if decimal in (0, 1):  # Exit cases for the recursion
        return str(decimal)
    div, mod = divmod(decimal, 2)
    return decimal_to_binary_recursive_helper(div) + str(mod)


def decimal_to_binary_recursive(number: str) -> str:
    """
    Take an integer value and raise ValueError for wrong inputs,
    call the function above and return the output with prefix "0b" & "-0b"
    for positive and negative integers respectively.
    >>> decimal_to_binary_recursive(0)
    '0b0'
    >>> decimal_to_binary_recursive(40)
    '0b101000'
    >>> decimal_to_binary_recursive(-40)
    '-0b101000'
    >>> decimal_to_binary_recursive(40.8)
    Traceback (most recent call last):
        ...
    ValueError: Input value is not an integer
    >>> decimal_to_binary_recursive("forty")
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
    return f"{negative}0b{decimal_to_binary_recursive_helper(int(number))}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(decimal_to_binary_recursive(input("Input a decimal number: ")))
