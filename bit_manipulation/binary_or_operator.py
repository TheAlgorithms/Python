# -*- coding: utf-8 -*-
"""
https://www.tutorialspoint.com/python3/bitwise_operators_example.htm
This function takes in 2 integer, convert them to binary and returns a binary
in str format that is the result of an Binary OR operation from the 2 integer
input.

Returns a binary resulted from 2 integer input in str format
>>> Binary_OR_Operator(25,32)
'0b111001'

>>> Binary_OR_Operator(37,50)
'0b110111'

>>> Binary_OR_Operator(21,30)
'0b11111'

>>> Binary_OR_Operator(58,73)
'0b1111011'
"""


def Binary_OR_Operator (a : int, b : int):
    
    if type(a) == float or type(b) == float:
        raise TypeError("'Float' object cannot be implemented as an integer")
    if type(a) == str or type(b) == str:
        raise TypeError("'str' object cannot be implemented as an integer")
    if a <0 or b < 0:
        raise ValueError("the value of both input must be positive")
    """
    a_binary and b_binary are the binary of a and b in str format
    """
    a_binary = convert_to_binary(a)
    b_binary = convert_to_binary(b)
    binary = []
    if len(a_binary) > len(b_binary):
        greater = len(a_binary)
        for i in range(greater - len(b_binary)):
            b_binary= "0" + b_binary
    else:
        greater = len(b_binary)
        for i in range(greater - len(a_binary)):
            a_binary= "0" + a_binary
    for i in range(greater):
        if a_binary[i] == "1" or b_binary[i] == "1":
            binary.append("1")
        else:
            binary.append("0")
    return "0b" + "".join(binary)
    

"""
The function below converts the integer input from decimal to binary and 
returns the binary in str format
"""
def convert_to_binary(num: int)-> str:

    first = True
    while num > 0:
        if first:
            binarynumber = str(num%2)
            first = False
        else:
            binarynumber = str(num%2) + binarynumber
        num = int(num / 2)
    return binarynumber

if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
