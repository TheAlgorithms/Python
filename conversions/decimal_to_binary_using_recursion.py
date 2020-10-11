# This function converts positive integer values to their binary equivalent
def bin_recursive(decimal: int) -> str:
    """
    The funtion takes in an integer number via the parameter "decimal"
    and returns a string.
    >>> bin_recursive(1000)
    '1111101000'
    >>> bin_recursive("72")
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for //: 'str' and 'int'
    >>> bin_recursive("number")
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for //: 'str' and 'int'
    """
    # Initialize exit base of the recursion function
    if decimal == 1 or decimal == 0:
        return str(decimal)
    # Start recursion and return output
    binary = bin_recursive(decimal // 2) + str(decimal % 2)
    return binary


# This funtion handles wrong inputs, calls the funtion above
# and then prints out the output with prefix "0b" and "-0b".
def main(number: int) -> str:
    """
    This function takes a parameter "number",
    tries converting it to an integer and handles wrong inputs,
    passes the converted input to the function above and
    prints the output with prefix "0b" & "-0b" for positive
    and negative integers respectively.
    >>> main(0)
    0b0
    >>> main(40)
    0b101000
    >>> main(-40)
    -0b101000
    >>> main(40.8)
    0b101000
    >>> main("forty")
    'Input value is not an integer'
    """
    try:
        # try converting number to an integer
        number = int(number)
    except Exception:
        # Handle exception raised and return
        return "Input value is not an integer"

    if number < 0:
        number = -number
        print(f"-0b{bin_recursive(number)}")
    else:
        print(f"0b{bin_recursive(number)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main(input(": ").strip())
