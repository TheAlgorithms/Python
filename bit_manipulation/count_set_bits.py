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


    """


    if (n<0 or n!=math.floor(n)):
        my_error = ValueError("The input should neither be a negative nor a fractional number")
        raise my_error
    count = 0
    while (n!=0):
        n = n&(n-1)
        count = count + 1
    return (count)

count_set_bits(8)

if __name__ == "__main__" :
    import doctest

    doctest.testmod()


