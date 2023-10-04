"""
Problem 125: https://projecteuler.net/problem=125

The palindromic number 595 is interesting because it can be written as the sum
of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

There are exactly eleven palindromes below one-thousand that can be written as
consecutive square sums, and the sum of these palindromes is 4164. Note that
1 = 0^2 + 1^2 has not been included as this problem is concerned with the
squares of positive integers.

Find the sum of all the numbers less than 10^8 that are both palindromic and can
be written as the sum of consecutive squares.
"""

LIMIT = 10**8


def is_palindrome(n: int) -> bool:
    """
    Check if an integer is palindromic.
    >>> is_palindrome(12521)
    True
    >>> is_palindrome(12522)
    False
    >>> is_palindrome(12210)
    False
    """
    if n % 10 == 0:
        return False
    s = str(n)
    return s == s[::-1]


def solution() -> int:
    """
    Returns the sum of all numbers less than 1e8 that are both palindromic and
    can be written as the sum of consecutive squares.
    """
    answer = set()
    first_square = 1
    sum_squares = 5
    while sum_squares < LIMIT:
        last_square = first_square + 1
        while sum_squares < LIMIT:
            if is_palindrome(sum_squares):
                answer.add(sum_squares)
            last_square += 1
            sum_squares += last_square**2
        first_square += 1
        sum_squares = first_square**2 + (first_square + 1) ** 2

    return sum(answer)


if __name__ == "__main__":
    print(solution())
