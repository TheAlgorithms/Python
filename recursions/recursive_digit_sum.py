"""
The super digit problem is defined as follows:
Given an integer n represented as a string and an integer k,
the goal is to find the super digit of the number formed by concatenating
the integer n k times.

The super digit of a number is defined recursively:
- If the number has only one digit, that digit is the super digit.
- Otherwise, the super digit is the super digit of the sum of its digits.

For example, for n = "9875" and k = 4, the concatenated number is:
super_digit(9875987598759875), which can be reduced by summing its digits.
"""

from __future__ import annotations


def super_digit(n_str: str, repetitions: int) -> int:
    """
    Computes the super digit of a number formed by concatenating
    n_str repetitions times.

    Parameters:
    n_str (str): The string representation of the integer.
    repetitions (int): The number of times to concatenate n_str.

    Returns:
    int: The super digit of the concatenated number.

    >>> super_digit("148", 3)
    3
    >>> super_digit("9875", 4)
    8
    >>> super_digit("123", 3)
    9
    """

    # Calculate the initial sum of the digits in n_str
    digit_sum = sum(int(digit) for digit in n_str)

    # Multiply the sum by repetitions
    total_sum = digit_sum * repetitions

    # Recursive function to find the super digit
    while total_sum >= 10:
        total_sum = sum(int(digit) for digit in str(total_sum))

    return total_sum


if __name__ == "__main__":
    # Read input and split it into n_str and repetitions
    first_multiple_input = input().rstrip().split()

    n_str = first_multiple_input[0]  # n as a string
    repetitions = int(first_multiple_input[1])  # repetitions as an integer

    # Call the super_digit function and print the result
    result = super_digit(n_str, repetitions)
    print(result)
