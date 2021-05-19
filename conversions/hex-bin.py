#  CONVERT HEXADECIMAL TO BINARY
import math
from typing import Union


def convert(num: str) ->Union[bool, int]:
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
    
    >>> convert("AC")
    10101100
    >>> convert("9A4")
    100110100100
    >>> convert("   12f   ")
    100101111
    >>> convert("FfFf")
    1111111111111111
    >>> convert("F-f")
    False
    >>> convert("")
    False
    """

    bin_str :str = ""
    hex_str :str = num.strip()
    
    if not hex_str:
        return False
    
    is_negative : bool = hex_str[0] == "-"
     
    if is_negative:
        hex_string = hex_str[1:]
    try:
        int_num :int = int(hex_str, 16)
    except ValueError:
        return False
    
    while int_num > 0:
        str_num :str = str(int_num % 2)
        bin_str = str_num + bin_str
        int_num = int_num >> 1
        
    return int("-" + "".join(bin_str)) if is_negative else int(bin_str)
    
        

if __name__ == "__main__":
    import doctest

    doctest.testmod()
