def is_even(number: int) -> bool:
    """
    return true if the input integer is even
    Explanation: Lets take a look at the following decimal to binary conversions
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

    >>> is_even(1)
    False
    >>> is_even(4)
    True
    >>> is_even(9)
    False
    >>> is_even(15)
    False
    >>> is_even(40)
    True
    >>> is_even(100)
    True
    >>> is_even(101)
    False
    """
    return number & 1 == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
