"""
"https://projecteuler.net/problem=125"

Name: Palindromic sums


The palindromic number 595 is interesting because it can be written as
the sum of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.
There are exactly eleven palindromes below one-thousand that can be written as
consecutive square sums, and the sum of these palindromes is 4164.

Note that 1 = 0^2 + 1^2 has not been included as this problem is concerned with
the squares of positive integers.

Find the sum of all the numbers less than 10^8
that are both palindromic and can be written as the sum of consecutive squares.

"""


import math


def gen_square_sums(limit: int) -> list:
    """
    Generates and returns thee square sums till n.
    Using the formula 1^2 + 2^2 + .. + n^2 = n * (n + 1) * (2n + 1) / 6
    """
    square_sums = []
    for n in range(limit):
        square_sum = (n * (n + 1) * (2 * n + 1)) // 6
        square_sums.append(square_sum)
    return square_sums


def gen_palindromic_square_sums(square_sums) -> list:
    """
    Filters and returns the palindromic square sums
    Difference between any two index gives the sum of squares in that range.
    """
    palindromic_square_sums = set()
    for i in range(len(square_sums) - 2):
        for j in range(i + 2, len(square_sums)):
            diff = square_sums[j] - square_sums[i]
            if is_palindrome(diff):
                palindromic_square_sums.add(diff)
    return sorted(palindromic_square_sums)


def is_palindrome(n: int) -> bool:
    """
    Returns if the number is palindrome or not
    """
    return str(n) == str(n)[::-1]


def solution(limit: int = 1e8) -> int:
    """
    Returns the sum of palindromic squares sums till 10^8.
    """
    square_sums = gen_square_sums(int(math.sqrt(limit)))
    palindromic_square_sums = gen_palindromic_square_sums(square_sums)

    res = index = 0
    while palindromic_square_sums[index] <= limit:
        res += palindromic_square_sums[index]
        index += 1
    return res


if __name__ == "__main__":
    print(solution())
