"""
https://en.wikipedia.org/wiki/Logarithm
"""


def logarithm(end: int, base: int) -> float:
    """
    Return the logarithm with base base of x
    :param end: the number
    :param base: the base of the exponential
    :return:

    >>> logarithm(32, 2)
    5
    >>> logarithm(100, 10)
    2
    >>> logarithm(2937846, 3)
    13.556363215077281
    """
    if base < 0 or end < 0:
        raise ValueError('logarithm() takes 2 positive values')
    
    if base == 0:
        return 1
    start = 0
    prev = 0
    accuracy = 1
    e = 0.000001
    while True:
        start = prev + accuracy
        _curr = base ** start

        if _curr >= end:
            error = _curr - end
        else:
            error = end - _curr

        if error <= e:
            return start

        if _curr > end:
            accuracy /= 10
        else:
            prev = start


if __name__ == "__main__":
    pass
