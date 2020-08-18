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
    
    if isinstance(a, float) or isinstance(b, float):
        raise TypeError("'Float' object cannot be implemented as an integer")
    if isinstance(a, str) or isinstance(b,str):
        raise TypeError("'str' object cannot be implemented as an integer")
    if a < 0 or b < 0:
        raise ValueError("the value of both input must be positive")
    """
    a_binary and b_binary are the binary of a and b in str format
    """
    a_binary = str(bin(a))[2:]
    b_binary = str(bin(b))[2:]
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
    


if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
