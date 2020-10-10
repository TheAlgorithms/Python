"""
Problem 38
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


def is_pandigital(num):
    """
    Checks whether num is 1-9 pandigital
    >>> is_pandigital(123456789)
    True
    >>> is_pandigital(214365879)
    True
    >>> is_pandigital(1)
    False
    >>> is_pandigital(556677889)
    False
    >>> is_pandigital(545754735)
    False
    >>> is_pandigital(2143887565879)
    False
    """
    num = str(num)
    for digit in range(1, 10):
        digit = str(digit)
        if digit in num:
            num = num.replace(digit, "", 1)
        else:
            return False
    return True if len(num) == 0 else False


def solution():
    for num in range(9487, 9233, -1):
        num_to_check = int(str(num * 1) + str(num * 2))
        if is_pandigital(num_to_check):
            return num_to_check


if __name__ == "__main__":
    print(solution())
