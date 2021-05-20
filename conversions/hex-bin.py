#  CONVERT HEXADECIMAL TO BINARY
import math


def hex_to_bin(hex_num: str) -> int:
    """
    Convert a hexadecimal value to its decimal equivalent
    #https://stackoverflow.com/questions/1425493/convert-hex-to-binary
    Here, we have used " >> " bitwise operator
    Bitwise right shift: 
    Shifts the bits of the number to the right and fills 0 on voids left as a result. 
    Similar effect as of dividing the number with some power of two.
    Example: 
    a = 10
    a >> 1 = 5 
    
    >>> hex_to_bin("AC")
    10101100
    >>> hex_to_bin("9A4")
    100110100100
    >>> hex_to_bin("   12f   ")
    100101111
    >>> hex_to_bin("FfFf")
    1111111111111111
    >>> hex_to_bin("F-f")
    Traceback (most recent call last):
    ...
    ValueError: Invalid value was passed to the function
    >>> hex_to_bin("")
    Traceback (most recent call last):
    ...
    ValueError: No value was passed to the function
    """

    bin_str: str = ""
    hex_str: str = hex_num.strip()

    if not hex_str:
        raise ValueError("No value was passed to the function")

    is_negative: bool = hex_str[0] == "-"

    if is_negative:
        hex_str = hex_str[1:]
    try:
        int_num: int = int(hex_str, 16)
    except ValueError:
        raise ValueError("Invalid value was passed to the function")
    while int_num > 0:
        str_num: str = str(int_num % 2)
        bin_str = str_num + bin_str
        int_num = int_num >> 1

    return int("-" + "".join(bin_str)) if is_negative else int(bin_str)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
