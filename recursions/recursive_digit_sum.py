"""
The super digit problem is defined as follows:
Given an integer represented as a string and an integer k,
the goal is to find the super digit of the number formed by concatenating
the integer n k times.

The super digit of a number is defined recursively:
- If the number has only one digit, that digit is the super digit.
- Otherwise, the super digit is the super digit of the sum of its digits.

For example, for n = "9875" and k = 4, the concatenated number is:
super_digit(9875987598759875), which can be reduced by summing its digits.
"""

from __future__ import annotations


def superDigit(n: str, k: int) -> int:
    """
    Computes the super digit of a number formed by concatenating n k times.

    Parameters:
    n (str): The string representation of the integer.
    k (int): The number of times to concatenate n.

    Returns:
    int: The super digit of the concatenated number.

    >>> superDigit("148", 3)
    3
    >>> superDigit("9875", 4)
    8
    >>> superDigit("123", 3)
    9
    """

    # Calculate the initial sum of the digits in n
    digit_sum = sum(int(digit) for digit in n)

    # Multiply the sum by k
    total_sum = digit_sum * k

    # Recursive function to find the super digit
    while total_sum >= 10:
        total_sum = sum(int(digit) for digit in str(total_sum))

    return total_sum


if __name__ == "__main__":
    # Read input and split it into n and k
    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]  # n as a string
    k = int(first_multiple_input[1])  # k as an integer

    # Call the superDigit function and print the result
    result = superDigit(n, k)
    print(result)
