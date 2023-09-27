"""
Problem 112: https://projecteuler.net/problem=112

Working from left-to-right if no digit is exceeded by the digit to its left it is
called an increasing number; for example, 134468.
Similarly if no digit is exceeded by the digit to its right it is called a decreasing
number; for example, 66420.
We shall call a positive integer that is neither increasing nor decreasing a "bouncy"
number, for example, 155349.
Clearly there cannot be any bouncy numbers below one-hundred, but just over half of
the numbers below one-thousand (525) are bouncy. In fact, the least number for which
the proportion of bouncy numbers first reaches 50% is 538.
Surprisingly, bouncy numbers become more and more common and by the time we reach
21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""


def check_bouncy(n: int) -> bool:
    """
    Returns True if number is bouncy, False otherwise
    >>> check_bouncy(6789)
    False
    >>> check_bouncy(-12345)
    False
    >>> check_bouncy(0)
    False
    >>> check_bouncy(6.74)
    Traceback (most recent call last):
        ...
    ValueError: check_bouncy() accepts only integer arguments
    >>> check_bouncy(132475)
    True
    >>> check_bouncy(34)
    False
    >>> check_bouncy(341)
    True
    >>> check_bouncy(47)
    False
    >>> check_bouncy(-12.54)
    Traceback (most recent call last):
        ...
    ValueError: check_bouncy() accepts only integer arguments
    >>> check_bouncy(-6548)
    True
    """
    if not isinstance(n, int):
        raise ValueError("check_bouncy() accepts only integer arguments")
    str_n = str(n)
    sorted_str_n = "".join(sorted(str_n))
    return str_n not in {sorted_str_n, sorted_str_n[::-1]}


def solution(percent: float = 99) -> int:
    """
    Returns the least number for which the proportion of bouncy numbers is
    exactly 'percent'
    >>> solution(50)
    538
    >>> solution(90)
    21780
    >>> solution(80)
    4770
    >>> solution(105)
    Traceback (most recent call last):
        ...
    ValueError: solution() only accepts values from 0 to 100
    >>> solution(100.011)
    Traceback (most recent call last):
        ...
    ValueError: solution() only accepts values from 0 to 100
    """
    if not 0 < percent < 100:
        raise ValueError("solution() only accepts values from 0 to 100")
    bouncy_num = 0
    num = 1

    while True:
        if check_bouncy(num):
            bouncy_num += 1
        if (bouncy_num / num) * 100 >= percent:
            return num
        num += 1


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{solution(99)}")
