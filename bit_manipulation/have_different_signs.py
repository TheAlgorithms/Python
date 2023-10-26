# https://www.geeksforgeeks.org/detect-if-two-integers-have-opposite-signs/


def have_different_signs(number1: int, number2: int) -> bool:
    """
    Check if two integers have different signs.

    >>> have_different_signs(5, -3)
    True
    >>> have_different_signs(-2, 8)
    True
    >>> have_different_signs(0, -5)
    True
    >>> have_different_signs(3, 7)
    False
    >>> have_different_signs(-10, -20)
    False
    >>> have_different_signs(0, 0)
    False
    """

    # Check if the signs of the two numbers are different
    return (number1 < 0 and number2 >= 0) or (number1 >= 0 and number2 < 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
