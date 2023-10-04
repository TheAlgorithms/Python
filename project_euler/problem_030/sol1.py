""" Problem Statement (Digit Fifth Powers): https://projecteuler.net/problem=30

Surprisingly there are only three numbers that can be written as the sum of fourth
powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their
digits.

9^5 = 59049
59049 * 7 = 413343 (which is only 6 digit number)
So, numbers greater than 999999 are rejected
and also 59049 * 3 = 177147 (which exceeds the criteria of number being 3 digit)
So, number > 999
and hence a number between 1000 and 1000000
"""


DIGITS_FIFTH_POWER = {str(digit): digit**5 for digit in range(10)}


def digits_fifth_powers_sum(number: int) -> int:
    """
    >>> digits_fifth_powers_sum(1234)
    1300
    """
    return sum(DIGITS_FIFTH_POWER[digit] for digit in str(number))


def solution() -> int:
    return sum(
        number
        for number in range(1000, 1000000)
        if number == digits_fifth_powers_sum(number)
    )


if __name__ == "__main__":
    print(solution())
