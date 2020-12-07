"""
How many 20 digit numbers n (without any leading zero) exist such that no three
consecutive digits of n have a sum greater than 9?
"""

from typing import Dict


def last_2_digits_sum(n: int) -> int:
    """
    Return the sum of the last 2 digits of n.
    >>> last_2_digits_sum(3)
    3
    >>> last_2_digits_sum(20)
    2
    >>> last_2_digits_sum(145)
    9
    >>> last_2_digits_sum(1000010)
    1
    """
    n %= 100
    return (n % 10) + (n // 10)


def solution(num_digits: int = 20) -> int:
    """
    Return the number of integers with num_digits digits that contain no 3 consecutive
    digits whose sum exceeds 9.
    >>> solution(1)
    9
    >>> solution(2)
    45
    >>> solution(30)
    6541579102690304285086
    """
    freq_dict: Dict[int, int] = {i: 0 for i in range(1000)}
    freq_dict.update({i: 1 for i in range(1, 10)})
    n: int
    freq_count_dict: Dict[int, int]
    last_3_digits: int
    freq: int
    next_idx_stub: int
    last_2_digit_sum: int
    digs: int

    for n in range(num_digits - 1):
        freq_count_dict = {i: 0 for i in range(1000)}

        for last_3_digits, freq in freq_dict.items():
            next_idx_stub = (last_3_digits % 100) * 10
            last_2_dig_sum = last_2_digits_sum(last_3_digits)

            for digs in range(next_idx_stub, next_idx_stub + 10 - last_2_dig_sum):
                freq_count_dict[digs] += freq

        freq_dict = freq_count_dict

    return sum(freq_dict.values())


if __name__ == "__main__":
    print(f"{solution() = }")
