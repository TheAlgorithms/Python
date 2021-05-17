#convert hexadecimal into binary
from doctest import testmod
import math


hex_str = input("").strip()
if not hex_str:
    raise ValueError("Empty string was passed to the function")
is_negative:bool = hex_str[0] == "-"
if is_negative:
    hex_string = hex_str[1:]
    
num: int = int(hex_str, 16)
bin: str = ""


"""
Here, we have used " >> " bitwise operator
Bitwise right shift: 
Shifts the bits of the number to the right and fills 0 on voids left as a result. 
Similar effect as of dividing the number with some power of two.
Example: 
a = 10
a >> 1 = 5 

"""

def convert(num: int, bin_str: str, is_negative: bool) ->str :
    """

    Convert a hexadecimal value to its decimal equivalent
    #https://stackoverflow.com/questions/1425493/convert-hex-to-binary
    >>> convert(AC, bin_str)
    10101100
    >>> convert(9A4, bin_str)
    100110100100
    >>> convert("   12f   ", bin_str)
    100101111
    >>> convert(FfFf, bin_str)
    1111111111111111
    >>> convert(F-f, bin_str)
    Traceback (most recent call last):
    ...
    ValueError: invalid literal for int() with base 16:
    >>> convert(,bin_str)
    Traceback (most recent call last):
    ...
    ValueError: Empty string was passed to the function:
    
    """

    while num>0:
        mnum: str = str(n%2)
        bin_str = mnum + bin_str
        num=num>>1
    mnum = bin_str
    if is_negative:
        sign = "-"
        return sign+bin_str   
    else:
        return bin_str

if __name__ == "__main__":
    testmod(name = 'convert', verbose = True)

