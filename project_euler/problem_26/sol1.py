"""
Euler Problem 26
https://projecteuler.net/problem=26
Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
"""


def find_digit(numerator: int, digit: int) -> int:
    """
    Considering any range can be provided,
    because as per the problem, the digit d < 1000
    >>> find_digit(1, 10)
    7
    >>> find_digit(10, 100)
    97
    >>> find_digit(10, 1000)
    983
    """
    the_digit = 1
    longest_list_length = 0

    for divide_by_number in range(numerator, digit + 1):
        has_been_divided = []
        now_divide = numerator
        for division_cycle in range(1, digit + 1):
            if now_divide in has_been_divided:
                if longest_list_length < len(has_been_divided):
                    longest_list_length = len(has_been_divided)
                    the_digit = divide_by_number
            else:
                has_been_divided.append(now_divide)
                now_divide = now_divide * 10 % divide_by_number

    return the_digit


# Tests
if __name__ == "__main__":
    import doctest

    doctest.testmod()
