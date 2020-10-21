import math
def count_set_bits(n):
    """
    >>> count_set_bits(8)
    1
    >>> count_set_bits(7)
    3
    >>> count_set_bits(2.5)
    Traceback (most recent call last):
        ...
    ValueError: The input should be positive integer
    >>> count_set_bits(-2)
    Traceback (most recent call last):
        ...
    ValueError: The input should be positive integer
    """
    if (n<0 or n!=math.floor(n)):
        raise ValueError("The input should be positive integer")
    c = 0
    while (n!=0):
        n=n&(n-1)
        c=c+1
    return c

if __name__ == "main":
    import doctest
    doctest.testmod()
