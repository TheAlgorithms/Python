def bin_exp(num, expo) -> int:
    """
    This function calculates the exponent of 'num' over 'expo' and
    returns a positive number.
    This function does binary exponential hence O(log N) time complexity.
    So, It is faster than normal exponential function for huge numbers.
    >>> bin_exp(2, 5)
    32
    """
    result = 1
    while expo:
        if expo % 2:
            result *= num
            expo = expo - 1
        else:
            num *= num
            expo /= 2
    return result


# call the testmod function
if __name__ == "__main__":
    from doctest import testmod

    testmod()
