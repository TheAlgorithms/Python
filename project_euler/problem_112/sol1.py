"""
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
    >>> check_bouncy(6.74)
    False
    >>> check_bouncy(132475)
    True
    >>> check_bouncy(-6548)
    True
    """
    if not isinstance(n, int):
        return False
    return "".join(sorted(str(n))) != str(n) and "".join(sorted(str(n)))[::-1] != str(n)


def solution(percent: int = 99) -> int:
    """
    Returns the least number for which the proportion of bouncy numbers is
    exactly 'percent'
    >>> solution(50)
    538
    >>> solution(90)
    21780
    >>> solution(80)
    4770
    """
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
