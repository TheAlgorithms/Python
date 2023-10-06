def update_bit(n: int, pos: int, value: int) -> int:
    '''
    It is a program to update a bit at given position

    Details:update the bit at position pos of the
    number n by the value provided to it.
    and return updated integer.

    >>> update_bit(5,0,0) #0b100
    4
    >>> update_bit(10,1,0) #0b1000
    8
    >>> update_bit(15,3,0) #0b0111
    7
    >>> update_bit(5,1,1) #70b111
    7
    >>> update_bit(10,0,1) #0b1011
    11
    '''

    mask = ~(1 << pos)
    n = n & mask
    return n | (value << pos)

if __name__ == "__main__":
    import doctest

    doctest.testmod()