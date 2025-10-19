# disarium.py


def is_disarium(num):
    """
    Check if a number is Disarium.

    >>> is_disarium(89)
    True
    >>> is_disarium(75)
    False
    >>> is_disarium(135)
    True
    """
    digits = list(str(num))
    total = 0
    for i in range(len(digits)):
        total += int(digits[i]) ** (i + 1)
    return total == num


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
