"""
Project Euler 206
https://projecteuler.net/problem=206

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
in a 3 or 7. We can either start checking for the square root from
101010103, which is the closest square root of 10203040506070809 that ends
in 3 or 7, or 138902663, the closest square root of 1929394959697989. The
problem says there's only 1 answer, so starting at either point is fine,
but the result happens to be much closer to the latter.
"""


def solution() -> int:
    """
    Returns the first integer whose square is of the form 1_2_3_4_5_6_7_8_9_0.
    """
    num = 138902663

    while not is_square_form(num * num):
        if num % 10 == 3:
            num -= 6  # (3 - 6) % 10 = 7
        else:
            num -= 4  # (7 - 4) % 10 = 3

    return num * 10


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


if __name__ == "__main__":
    print(f"{solution() = }")
