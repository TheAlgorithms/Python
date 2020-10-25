#!/usr/bin/env python3
"""
Project Euler Problem 38: https://projecteuler.net/problem=38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product of
9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


def solution() -> int:
    """
    Return largest 1 to 9 pandigital 9-digit number as description.

    >>> solution()
    932718654
    """
    max_value = 0
    for i in range(1, 987654321 // 2 + 1):
        number_string = ""
        for j in range(1, 10):
            number_string += str(i * j)
            number_set = set(number_string)
            if j == 1 and number_string[0] != "9":
                # we already know 9 x [1, 2, 3, 4, 5] => 918273645
                break
            elif (
                len(number_set) != len(number_string)
                or len(number_string) > 9
                or "0" in number_string
            ):
                break
            elif len(number_string) < 9:
                continue
            else:
                number = int(number_string)
                if number > max_value:
                    max_value = number
    return max_value


if __name__ == "__main__":
    print(solution())
