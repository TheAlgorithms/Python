from doctest import testmod
from math import sqrt


def factors_of_a_number(num: int) -> list:
    """
    >>> factors_of_a_number(1)
    [1]
    >>> factors_of_a_number(5)
    [1, 5]
    >>> factors_of_a_number(24)
    [1, 2, 3, 4, 6, 8, 12, 24]
    >>> factors_of_a_number(-24)
    []
    """
    facs: list[int] = []
    if num < 1:
        return facs
    facs.append(1)
    if num == 1:
        return facs
    facs.append(num)
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:  # If i is a factor of num
            facs.append(i)
            d = num // i  # num//i is the other factor of num
            if d != i:  # If d and i are distinct
                facs.append(d)  # we have found another factor
    facs.sort()
    return facs


if __name__ == "__main__":
    testmod(name="factors_of_a_number", verbose=True)
