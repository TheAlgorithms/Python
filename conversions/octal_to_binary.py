def octal_to_binary(octal_number):
    """
    /**
    * Converts any Octal Number to a Binary Number
    *
    * @author Bama Charan Chhandogi
    */
    Convert an octal number to binary.

    Args:
        octal_number (str): The octal number as a string.

    Returns:
        str: The binary representation of the octal number.

    Examples:
        >>> octal_to_binary("34")
        '0b11100'
        >>> octal_to_binary("777")
        '0b111111111'
    """
    decimal_number = int(octal_number, 8)
    binary_number = bin(decimal_number)
    return binary_number

if __name__ == "__main__":
    import doctest
    doctest.testmod()
