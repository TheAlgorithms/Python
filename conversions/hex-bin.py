#convert hexadecimal into binary
from doctest import testmod
import math

def convert(num: str) -> str:
    
    """
    Convert a hexadecimal value to its decimal equivalent
    #https://stackoverflow.com/questions/1425493/convert-hex-to-binary
    >>> convert("AC")
    10101100
    >>> convert("9A4")
    100110100100
    >>> convert("   12f   ")
    100101111
    >>> convert("FfFf")
    1111111111111111
    >>> convert("F-f")
    Traceback (most recent call last):
    ...
    ValueError: invalid literal for int() with base 16:
    >>> convert()
    Traceback (most recent call last):
    ...
    ValueError: Empty string was passed to the function:
    
    """

    bin_str : str=""
    flag :bool = 0
    hex_str :str = num.strip()
    
    if not hex_str:
        raise ValueError("Empty string was passed to the function")
    is_negative : bool= hex_str[0] == "-"
     
    if is_negative:
        flag = 1
        hex_string = hex_str[1:]
    
    num2 :int = int(hex_str, 16)

    """
    Here, we have used " >> " bitwise operator
    Bitwise right shift: 
    Shifts the bits of the number to the right and fills 0 on voids left as a result. 
    Similar effect as of dividing the number with some power of two.
    Example: 
    a = 10
    a >> 1 = 5 

    """
    
    while num2>0:
        num3 :str = str(num2%2)
        bin_str = num3 + bin_str
        num2=num2>>1

    if flag: 
        return "-"+bin_str
    else:
        return bin_str
        

if __name__ == "__main__":
    testmod(name = 'convert', verbose = True)

