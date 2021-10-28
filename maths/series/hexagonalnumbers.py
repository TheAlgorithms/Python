# hexagonalnumbers.py

"""
A hexagonal number seqeunce is a sequence of figurate numbers
where the nth hexagonal number hₙ is the number of distinct dots
in a pattern of dots consisting of the outlines of regular
hexagons with sides up to n dots, when the hexagons are overlaid
so that they share one vertex.

1. Calculates the hexagonal numbers sequence with a formula
    hₙ = n(2n-1)
    where:
    hₙ --> is nth element of the sequence
    n --> is the number of element in the sequence
    reference-->"Hexagonal number" Wikipedia
    <https://en.wikipedia.org/wiki/Hexagonal_number>

2. Checks if a number is a hexagonal number with a formula
    n = (sqrt(8x+1)+1)/4
    where:
    x --> is the number to check
    n --> is a integer if x is a hexagonal number

    reference-->"Hexagonal number" Wikipedia
    <https://en.wikipedia.org/wiki/Hexagonal_number>
"""


class Error(Exception):
    """Base class for other exceptions"""


class ValueLessThanZero(Error):
    """Raised when the input value is less than zero"""


class ValueIsZero(Error):
    """Raised when the input value is zero"""


def len_check(len):
    if len < 0:
        raise ValueLessThanZero
    elif len == 0:
        raise ValueIsZero


def hexagonal_numbers(len: int):
    """
    :param len: max number of elements
    :type len: int
    :return: Hexagonal numbers as a list

    Tests:
    >>> hexagonal_numbers(10)
    [0, 1, 6, 15, 28, 45, 66, 91, 120, 153]
    >>> hexagonal_numbers(5)
    [0, 1, 6, 15, 28]
    """

    len_check(len)
    hexagonal_numbers_list = []
    for n in range(len):
        num = n * (2 * n - 1)
        hexagonal_numbers_list.append(num)
    return hexagonal_numbers_list


def check_if_hexagonal_number(num: int):
    """
    :param num: number to check
    :type num: int
    :return: boolean

    Tests:
    >>> check_if_hexagonal_number(120)
    True
    >>> check_if_hexagonal_number(5)
    False
    """

    n = (((8 * num + 1) ** 1 / 2) + 1) / 4
    isInt = True
    try:
        int(n)
    except ValueError:
        isInt = False
    return isInt


if __name__ == "__main__":
    len = 5
    hexagonal_numbers_list = hexagonal_numbers(len)
    print(hexagonal_numbers_list)

    num = 120
    check = check_if_hexagonal_number(num)
    print(check)
