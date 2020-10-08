"""
PROJECT EULER
Problem 38


What is a 'pandigital' number?

For the purposes of this problem, we define a pandigital number as a number
which has each of the digits 1-9 exactly once.  For example, the number
192384576 is a pandigital number.


What is a 'concatenated product'?

Given an positive integer, f, and an ordered sequence of positive integers,
(1, 2, 3, ... n) where n > 1, the concatenated product is the number formed
by concatenating the digits of the product of f with each of the numbers
in the sequence in order.  For example, the concatenated product of 24
and (1, 2, 3, 4) is 24487296.


What is this problem asking?

What is the largest nine-digit pandigital number that can be formed as the
concatenated product of an integer with the ordered sequence, (1, 2, ..., n),
where n > 1?
"""


def concatenated_product(factor: int, upper_limit: int) -> int:
    """
    This function calculates the integer wihich is the concatenated product
    of the integer 'factor' with the ordered sequence (1, ..., 'upper_limit').
    >>> concatenated_product(9, 5)
    918273645
    >>> concatenated_product(192, 3)
    192384576
    """
    product_string = ''
    for i in range(1, upper_limit + 1):
        product = i * factor
        product_string += str(product)
    return int(product_string)

def is_pandigital(test_number: int) -> bool:
    """
    This function tests whether 'test_number' is a 1-9 nine-digit
    pandigital number.
    >>> is_pandigital(123456789)
    True
    >>> is_pandigital(10234567)
    False
    """
    test_number_string = str(test_number)
    # First check if test_number is a nine-digit number
    if len(test_number_string) != 9:
        return False
    """
    This list is used to count the number of occurrances of
    each digit in test_number.
    The index of the list corresponds to the digit being
    counted.
    Thus the value at index 0 is unused.
    """
    count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    reduced_number = test_number
    for i in range(9):
        digit = reduced_number % 10
        reduced_number = reduced_number // 10
        count_list[digit] += 1
    for i in range(1, 10):
        if count_list[i] != 1:
            return False
    return True

def get_max_pandigital_for_n(n: int) -> int:
    """
    For a given ordered integer sequence, (1, ..., n), find the largest
    pandigital number that can be formed as the concatenated product
    of an integer with that sequence.  If no pandigital number exists
    for a given value of n, the function returns 0.
    >>> get_max_pandigital_for_n(2)
    932718654
    >>> get_max_pandigital_for_n(4)
    0
    """
    test_number = 0
    concat_product = 0
    max_concat_product = 0
    is_too_long = False
    while not is_too_long:
        test_number += 1
        concat_product = concatenated_product(test_number, n)
        if len(str(concat_product)) > 9:
            is_too_long = True
        elif (is_pandigital(concat_product) and 
        concat_product > max_concat_product):
            max_concat_product = concat_product
    return max_concat_product

def get_max_pandigital() -> int:
    """
    This is the primary function for this problem.  It calculates the
    maximum pandigital number possible formed as the concatenated
    product of an integer and the ordered sequence (1, ..., n) for
    n > 1.
    """
    max_pandigital = 0
    """
    n must be < 10 for a nine digit number formed as a concatenated
    product
    """
    for n in range(2, 10):
        max_pandigital_for_n = get_max_pandigital_for_n(n)
        if max_pandigital_for_n > max_pandigital:
            max_pandigital = max_pandigital_for_n
    return max_pandigital


if __name__ == '__main__':
    absolute_max_pandigital_number = get_max_pandigital()
    print(f"Max pandigital number: {absolute_max_pandigital_number}")
