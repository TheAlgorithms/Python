def is_odd(number: int) -> bool:
    """
    return true if the input integer is odd
    Explanation: Let us take a look at the following deicmal to binary conversions
    7 ==> 111
    14 ==> 10111
    50 ==> 110010
    112 ==> 1110000
    89 ==> 1011001
    529 ==> 1000010001
    From all the above examples we can observe that
    for all the odd integers there is always 1 set bit at the end
    Also, in binary, we can represent 1 as 001, 00001, or 0000001
    So we can infer that for any odd integer n, n&1 is always equals 1 (True),
    else the integer is even (False)
    Basically, The idea is to check whether the last bit of the number is set or not. 
    If last bit is set then the number is odd, otherwise even.

    >>> is_odd(5)
    True
    >>> is_odd(8)
    False
    >>> is_odd(20)
    False
    >>> is_odd(57)
    True
    >>> is_odd(1000)
    False
    >>> is_odd(1)
    True
    """
    return number & 1 == 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()