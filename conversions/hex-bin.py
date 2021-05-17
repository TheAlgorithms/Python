#convert hexadecimal into binary
from doctest import testmod
import math


hex_str = input("").strip()

try:
    num : int = int(hex_str, 16)
except:
    print("An exception occured")
    
bin_str: str = ""


"""
Here, we have used " >> " bitwise operator
Bitwise right shift: 
Shifts the bits of the number to the right and fills 0 on voids left as a result. 
Similar effect as of dividing the number with some power of two.
Example: 
a = 10
a >> 1 = 5 

"""

def convert(num: int, bin_str: str) -> str:
    """
    >>> AC
    >>> 10101100
    
    """
    while num > 0:
        mnum = str(num % 2)
        bin_str = mnum + bin_str
        num=num>>1
    
    return str(bin_str)

print(convert(num, bin_str))

if __name__ == "__main__":
    testmod(name = 'convert', verbose = True)

