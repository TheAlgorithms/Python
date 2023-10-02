def is_odd(number: int) -> bool:
    """
    return true if the input integer is odd
    Explanation: Lets take a look at the following deicmal to binary conversions
    2 => 10
    14 => 1110
    100 => 1100100
    3 => 11
    13 => 1101
    101 => 1100101
    from the above examples we can observe that
    for all the odd integers there is always 1 set bit at the end
    also, 1 in binary can be represented as 001, 00001, or 0000001
    so for any odd integer n => n&1 is always equals 1 else the integer is even

    >>> is_odd(1)
    True
    >>> is_odd(4)
    False
    >>> is_odd(9)
    True
    >>> is_odd(15)
    True
    >>> is_odd(40)
    False
    >>> is_odd(100)
    False
    >>> is_odd(101)
    True
    """
    return number & 1 == 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
