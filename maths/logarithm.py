"""
https://en.wikipedia.org/wiki/Logarithm
"""


def logarithm(end: float, base: float, err: float = 0.000001) -> float:
    """
    Return the logarithm with base base of x
    :param end: the number
    :param base: the base of the exponential
    :return:
    
    >>> logarithm(2, 9)
    0.31546499999999994
    >>> logarithm(9, 2)
    3.1699250000000005
    >>> logarithm(0.2, 0.9)
    15.275499999999994
    >>> logarithm(0.9, 0.2)
    0.065464
    >>> logarithm(0.2, 9)
    -0.7324849999999997
    >>> logarithm(2, 0.9)
    -6.578809999999997
    >>> logarithm(9, 0.2)
    -1.3652123999999999
    >>> logarithm(0.9, 2)
    -0.15200200000000003
    >>> logarithm(0, 1)
    Traceback (most recent call last):
    ...
    ValueError: logarithm() takes 2 positive values
    >>> logarithm(-1, 1)
    Traceback (most recent call last):
    ...
    ValueError: logarithm() takes 2 positive values
    >>> logarithm(1, 0)
    Traceback (most recent call last):
    ...
    ValueError: logarithm() takes 2 positive values
    >>> logarithm(-1, 0)
    Traceback (most recent call last):
    ...
    ValueError: logarithm() takes 2 positive values
    """
    
    if base <= 0 or end <= 0:
        raise ValueError('logarithm() takes 2 positive values')
    
    frac = False
    
    accuracy = 1
    
    if end < 1 and base < 1:
        accuracy = 1
        frac = True
    elif base < 1:
        accuracy = -1
    elif end < 1:
        accuracy = -1
        frac = True
    

    if base == 0:
        return 1
    start = 0
    prev = 0
    while True:
        start = prev + accuracy
        _curr = base ** start

        if abs(_curr - end) <= err:
            return start
        if frac:
            if _curr < end:
                accuracy /= 10
            else:
                prev = start
        else:
            if _curr > end:
                accuracy /= 10
            else:
                prev = start


if __name__ == "__main__":
    print(f"{logarithm(2, 9) = }")
    print(logarithm(9, 2))
    print(logarithm(0.2, 0.9))
    print(logarithm(0.9, 0.2))
    print(logarithm(0.2, 9))
    print(logarithm(2, 0.9))
    print(logarithm(9, 0.2))
    print(logarithm(0.9, 2))
