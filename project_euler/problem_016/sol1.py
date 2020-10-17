"""
Problem 16: https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def solution(power: int = 1000) -> int:
    """Returns the sum of the digits of the number 2^power.
    >>> solution(1000)
    1366
    >>> solution(50)
    76
    >>> solution(20)
    31
    >>> solution(15)
    26
    """
    num = 2 ** power
    string_num = str(num)
    list_num = list(string_num)
    sum_of_num = 0

    for i in list_num:
        sum_of_num += int(i)

    return sum_of_num


if __name__ == "__main__":
    power = int(input("Enter the power of 2: ").strip())
    print("2 ^ ", power, " = ", 2 ** power)
    result = solution(power)
    print("Sum of the digits is: ", result)
