import math

def count_set_bits(n):

    """
    The function accepts a whole number stored in the variable n
    return the number of set bits which means the number of 1's in the binary representation
    this value is stored in the variable count initialized to 0
    The function uses Brian Kerninghan's Algorithm to achieve the same
    The primary expression is n=n&(n-1) which returns the leftmost set bit
    Some examples : Binary representation of 10 = 1010
    Sample I/O:
    >>> count_set_bits(7)
    3
    >>> count_set_bits(8)
    1
    Traceback (most recent call last):
    File "bin1.py", line 44, in <module>
    count_set_bits(-2)
    File "bin1.py", line 37, in count_set_bits
    raise my_error
    ValueError: The input should neither be a negative nor a fractional number
    >>> count_set_bits(6.8)
    Traceback (most recent call last):
    File "bin1.py", line 44, in <module>
    count_set_bits(6.8)
    File "bin1.py", line 36, in count_set_bits
    raise my_error
    ValueError: The input should neither be a negative nor a fractional number

    """


    if (n<0 or n!=math.floor(n)):
        my_error = ValueError("The input should neither be a negative nor a fractional number")
        raise my_error
    count = 0
    while (n!=0):
        n = n&(n-1)
        count = count + 1
    return (count)



if __name__ == "__main__" :
    import doctest

    doctest.testmod()


