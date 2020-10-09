"""
Converts decimal number to its binary equivalent using recursion
~$ python Decimal_to_binary_using_recursion.py
Enter a decimal number to be converted to binary form: 0
'0b0'
~$ python Decimal_to_binary_using_recursion.py
Enter a decimal number to be converted to binary form: 40
'0b101000'
~$ python Decimal_to_binary_using_recursion.py
Enter a decimal number to be converted to binary form: -40
'-0b101000'
~$ python Decimal_to_binary_using_recursion.py
Enter a decimal number to be converted to binary form: forty
'The value entered is not a decimal number'

"""
import sys

def bin_recursive(decimal: int) -> str:
    """
    Converts a positive integer decimal number to its binary equivalent using recursion
    >>>bin_recursive(0)
    '0b0'
    >>>bin_recursive(40)
    '0b101000'
    """

    if decimal == 1 or decimal == 0: return str(decimal)
    
    half = decimal // 2
    remainder = decimal % 2
    return bin_recursive(half) + str(remainder)
    
try:
    number = int(input("Enter a decimal number to be converted to binary form: ").strip())
except:
    print("The value entered is not a decimal number")
    sys.exit()

if number < 0:
    number = -number
    print("-0b" + bin_recursive(number))
else: print("0b" + bin_recursive(number))
