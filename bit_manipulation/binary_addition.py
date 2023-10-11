def AND(input1: str, input2: str) -> str:
    """
    AND gate logic.
    >>> AND('0','1')
    '0'
    >>> AND('0','0')
    '0'
    >>> AND('1','1')
    '1'
    >>> AND('1','0')
    '0'
    """
    if(input1 == '1' and input2 == '1'):
        return '1'
    else:
        return '0'
    
def OR(input1: str, input2: str) -> str:
    """
    OR gate logic.
    >>> OR('0','1')
    '1'
    >>> OR('0','0')
    '0'
    >>> OR('1','1')
    '1'
    >>> OR('1','0')
    '1'
    """
    if(input1 == '1' or input2 == '1'):
        return '1'
    else:
        return '0'
    
def XOR(input1: str, input2: str) -> str:
    """
    XOR gate logic.
    >>> XOR('0','1')
    '1'
    >>> XOR('0','0')
    '0'
    >>> XOR('1','1')
    '0'
    >>> XOR('1','0')
    '1'
    """
    if(input1 == input2):
        return '0'
    else:
        return '1'
    
def addition(number_1: str, number_2: str, number_of_bits:int) -> (str,str):
    """
    return tuple with ('sum','carry')
    The length of (number of bits in) 'sum' is same as the value of integer argument number_of_bits passed to the function. (i.e, if number_of_bits = 5, the length of 'sum' will also be 5 irrespective of the number of bits of number_1 and number_2).

    Explanation: The formula of sum and carry for each bit in binary operations are:
    carry:    C5 C4 C3 C2 C1 C0
    number_1:    A4 A3 A2 A1 A0
    number_2:  + B4 B3 B2 B1 B0
    ----------------------------
    answer:   C5 S4 S3 S2 S1 S0

    The formula for sum is:
    S0 = A0 XOR B0 XOR C0
    S1 = A1 XOR B1 XOR C1
    .
    .
    and so on.

    The formula for carry is:
    C1 = A0 AND B0 OR ((A0 XOR B0) AND C0)
    C2 = A1 AND B1 OR ((A1 XOR B1) AND C1)
    .
    .
    and so on.

    The numbers are reversed before operation so that the individual bits are traversed from right to left(using for loop) as we perform in addition by hand. Finally, the resultant sum is reversed again to retain the original format.

    >>> addition('1010','1101', 4)
    ('0111', '1')
    >>> addition('11111','00000', 5)
    ('11111', '0')
    >>> addition('0011','1111', 5)
    ('10010', '0')
    >>> addition('10011','110001', 6)
    ('000100', '1')
    >>> addition('10011','110001', 7)
    ('1000100', '0')
    >>> addition('1001','111', 4)
    ('0000', '1')
    >>> addition('1001','111', 5)
    ('10000', '0')
    >>> addition('101','10', 3)
    ('111', '0')

    Do not perform an operation as this  >>> addition('101','10', 2)  since adding 3-bit number with any other number results to atleast 3 bit number but you are expecting a 2 bit number which is not possible.
    """
    number_1 = number_1.zfill(number_of_bits) #zero padding at front
    number_2 = number_2.zfill(number_of_bits) #zero padding at front
    reversed_number_1 = number_1[::-1] # reverse for right to left traversal of bits using for loop
    reversed_number_2 = number_2[::-1] # reverse for right to left traversal of bits using for loop
    carry = '0' # initial carry in (C0) = 0
    sum = ''
    for i in range(number_of_bits):
        sum = sum + XOR(XOR(reversed_number_1[i],reversed_number_2[i]),carry)
        intermediate_xor = XOR(reversed_number_1[i], reversed_number_2[i])
        intermediate_and = AND(reversed_number_1[i], reversed_number_2[i])
        carry = OR(intermediate_and, AND(intermediate_xor,carry))
    sum = sum[::-1]
    return sum, carry


if __name__ == "__main__":
    import doctest

    doctest.testmod()