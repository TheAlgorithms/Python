"""
Project Euler problem 112: https://projecteuler.net/problem=112

Working from left-to-right if no digit is exceeded by the digit to its left it is
called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a
decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a
"bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over
half of the numbers below one-thousand (525) are bouncy. In fact, the least
number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we
reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""

from typing import Optional


def choose(n: int, r: int) -> int:
    """
    Calculate the binomial coefficient c(n,r) using the multiplicative formula.
    >>> choose(4,2)
    6
    >>> choose(5,3)
    10
    >>> choose(20,6)
    38760
    """
    ret = 1.0
    for i in range(1, r + 1):
        ret *= (n + 1 - i) / i
    return round(ret)


def non_bouncy_exact(n: int) -> int:
    """
    Calculate the number of non-bouncy numbers with at most n digits.
    >>> non_bouncy_exact(1)
    9
    >>> non_bouncy_exact(6)
    7998
    >>> non_bouncy_exact(10)
    136126
    """
    return choose(8 + n, n) + choose(9 + n, n) - 10


def non_bouncy_upto(n: int) -> int:
    """
    Calculate the number of non-bouncy numbers with at most n digits.
    >>> non_bouncy_upto(1)
    9
    >>> non_bouncy_upto(6)
    12951
    >>> non_bouncy_upto(10)
    277032
    """
    return sum(map(non_bouncy_exact, range(1, n + 1)))


def is_bouncy(n: int) -> bool:
    """
    Checks whether n is bouncy.
    >>> is_bouncy(134468)
    False
    >>> is_bouncy(66420)
    False
    >>> is_bouncy(155349)
    True
    """
    string: str = str(n)
    size: int = len(string)
    flag: Optional[str] = None
    idx: int = 1

    while idx < size:
        # first check whether the number might possibly be increasing or decreasing
        if string[idx] < string[idx - 1]:
            flag = "down"
            break
        if string[idx] > string[idx - 1]:
            flag = "up"
            break
        idx += 1

    if flag is None:
        # the digits are constant, e.g. 55555
        return False
    elif flag == "up":
        # n might be increasing, so for bounciness we need to find a decreasing
        # pair of adjacent digits
        while idx < size:
            if string[idx] < string[idx - 1]:
                return True
            idx += 1
        return False
    else:
        # n might be decreasing, so for bounciness we need to find an increasing
        # pair of adjacent digits
        while idx < size:
            if string[idx] > string[idx - 1]:
                return True
            idx += 1
        return False


def solution(thresh: float = 0.99) -> int:
    """
    Find th least number for which the proportion of bouncy numbers is exactly thresh.
    >>> solution(0.5)
    538
    >>> solution(0.9)
    21780
    >>> solution(0.95)
    63720

    Explanation:
        Since the function non_bouncy_upto runs in basically linear time (it's actually
        linear in the length of the integer, so logarithmic, but it's still basically
        instant) we can first use that function to get the number of digits of the
        answer. We stop that loop once we exceed the threshold. Then we can start going
        through the answers one by one, checking for bounciness using is_bouncy.
    """
    num_digits: int = 1
    checked_so_far: int = 9
    num_bouncy: int = checked_so_far - non_bouncy_upto(num_digits)
    while num_bouncy < thresh * checked_so_far:
        num_digits += 1
        checked_so_far = 10 * checked_so_far + 9
        num_bouncy = checked_so_far - non_bouncy_upto(num_digits)

    num_digits -= 1
    checked_so_far = (checked_so_far - 9) // 10

    num_bouncy = checked_so_far - non_bouncy_upto(num_digits)

    while num_bouncy != checked_so_far * thresh:
        checked_so_far += 1
        if is_bouncy(checked_so_far):
            num_bouncy += 1

    return checked_so_far


if __name__ == "__main__":
    print(f"{solution() = }")
