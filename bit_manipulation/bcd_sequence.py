def bcd_sequence(num: int) ->str:
    """
    Find binary coded decimal(bcd) of integer base 10.
    Each digit of number is represented by 4 bits binary.
    Example:
    >>> bcd_sequence(0)
    '0b0000'
    >>> bcd_sequence(3)
    '0b0011'
    >>> bcd_sequence(2)
    '0b0010'
    >>> bcd_sequence(12)
    '0b00010010'
    >>> bcd_sequence(987)
    '0b100110000111'
    """
    bcd = ""
    while num>0 :
        digit = num%10
        num = int(num/10)
        bin_seq = str(bin(digit))[2:]
        bin_seq = "0"*max(0,4-len(bin_seq)) + bin_seq
        bcd = bin_seq + bcd
    if bcd == "":
        bcd = "0"*4
    bcd = "0b" + bcd
    return bcd

   

if __name__ == "__main__":
    import doctest

    doctest.testmod()