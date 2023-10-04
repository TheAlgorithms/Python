"""
Project Euler Problem 206: https://projecteuler.net/problem=206

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.

-----

Instead of computing every single permutation of that number and going
through a 10^9 search space, we can narrow it down considerably.

If the square ends in a 0, then the square root must also end in a 0. Thus,
the last missing digit must be 0 and the square root is a multiple of 10.
We can narrow the search space down to the first 8 digits and multiply the
result of that by 10 at the end.

Now the last digit is a 9, which can only happen if the square root ends
in a 3 or 7. From this point, we can try one of two different methods to find
the answer:

1. Start at the lowest possible base number whose square would be in the
format, and count up. The base we would start at is 101010103, whose square is
the closest number to 10203040506070809. Alternate counting up by 4 and 6 so
the last digit of the base is always a 3 or 7.

2. Start at the highest possible base number whose square would be in the
format, and count down. That base would be 138902663, whose square is the
closest number to 1929394959697989. Alternate counting down by 6 and 4 so the
last digit of the base is always a 3 or 7.

The solution does option 2 because the answer happens to be much closer to the
starting point.
"""


def is_square_form(num: int) -> bool:
    """
    Determines if num is in the form 1_2_3_4_5_6_7_8_9

    >>> is_square_form(1)
    False
    >>> is_square_form(112233445566778899)
    True
    >>> is_square_form(123456789012345678)
    False
    """
    digit = 9

    while num > 0:
        if num % 10 != digit:
            return False
        num //= 100
        digit -= 1

    return True


def solution() -> int:
    """
    Returns the first integer whose square is of the form 1_2_3_4_5_6_7_8_9_0
    """
    num = 138902663

    while not is_square_form(num * num):
        if num % 10 == 3:
            num -= 6  # (3 - 6) % 10 = 7
        else:
            num -= 4  # (7 - 4) % 10 = 3

    return num * 10


if __name__ == "__main__":
    print(f"{solution() = }")
