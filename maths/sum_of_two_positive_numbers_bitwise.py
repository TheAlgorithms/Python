"""
Calculates the sum of two positive numbers using bitwise operator
Wikipedia explanation: https://en.wikipedia.org/wiki/Binary_number
"""

def sum_of_two_positive_numbers_bitwise(
    number: int, other_number: int
) -> int:
    """ "
    >>> sum_of_two_positive_numbers_bitwise(4, 5)
    9
    >>> sum_of_two_positive_numbers_bitwise(8, 9)
    17
    >>> sum_of_two_positive_numbers_bitwise(0, 4)
    4
    >>> sum_of_two_positive_numbers_bitwise(4.5, 9)
    Traceback (most recent call last):
        ...
    TypeError: Both parameters MUST be in integer type!
    >>> sum_of_two_positive_numbers_bitwise('4', 9)
    Traceback (most recent call last):
        ...
    TypeError: Both parameters MUST be in integer type!
    >>> sum_of_two_positive_numbers_bitwise('4.5', 9)
    Traceback (most recent call last):
        ...
    TypeError: Both parameters MUST be in integer type!
    >>> sum_of_two_positive_numbers_bitwise(-1, 9)
    Traceback (most recent call last):
        ...
    ValueError: Both parameters MUST be in positive value!
    >>> sum_of_two_positive_numbers_bitwise(1, -9)
    Traceback (most recent call last):
        ...
    ValueError: Both parameters MUST be in positive value!
    """

    if isinstance(number, int) is False or isinstance(other_number, int) is False:
        raise TypeError('Both parameters MUST be in integer type!')

    if number < 0 or other_number < 0:
        raise ValueError('Both parameters MUST be in positive value!')

    # Base case
    sum = number ^ other_number
    carry = number & other_number

    if (carry) == 0:
        return sum

    # Recursive case
    return sum_of_two_positive_numbers_bitwise(sum, carry << 1)

if __name__ == '__main__':
    import doctest

    doctest.testmod()