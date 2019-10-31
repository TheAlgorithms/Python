import math


def perfect_square(num: int) -> bool:
    """
    Check if a number is perfect square number or not
    :param num: the number to be checked
    :return: True if number is square number, otherwise False

    >>> perfect_square(9)
    True
    >>> perfect_square(16)
    True
    >>> perfect_square(1)
    True
    >>> perfect_square(0)
    True
    >>> perfect_square(10)
    False
    """
    return math.sqrt(num) * math.sqrt(num) == num


if __name__ == '__main__':
    import doctest

    doctest.testmod()
