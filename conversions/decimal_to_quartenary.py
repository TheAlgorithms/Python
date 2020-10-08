def decimal_to_quartenary(num):
    '''
    Convert a decimal number to it's quartenary equivalent (without any external libraries).

    >>> decimal_to_quartenary(10)
    '22'
    >>> decimal_to_quartenary(5)
    '11'
    >>> decimal_to_quartenary(1000)
    '33220'
    '''

    if not(str(num).isnumeric()):
        raise TypeError("The number entered has to be a decimal number.")

    quartenary = ''
    while num != 0:
        quartenary += str(num % 4)
        num //= 4
    return quartenary[::-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()