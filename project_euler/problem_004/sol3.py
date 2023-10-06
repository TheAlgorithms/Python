"""
Palindrome Six-Digit Numbers

This program finds six-digit numbers that 
are palindromes and can be
expressed as the product of 
two three-digit numbers.

References:
    - https://en.wikipedia.org/wiki/Palindrome
"""


def is_palindrome(number: int) -> bool:
    """
    Checks if a given number is a palindrome.
    Returns boolean indicating if the number is a palindrome.

    >>> is_palindrome(121)
    True
    >>> is_palindrome(123)
    False
    >>> is_palindrome(999999)
    True
    >>> is_palindrome(100001)
    True
    >>> is_palindrome(123456)
    False
    """

    str_num = str(number)
    return str_num == str_num[::-1]


def solution(n: int = 998001) -> int:
    """
    Returns the largest palindrome made from the product of two 3-digit
    numbers which is less than n.

    >>> solution(20000)
    19591
    >>> solution(30000)
    29992
    >>> solution(40000)
    39893
    """

    answer = 0
    for i in range(999, 99, -1):  # 3 digit numbers range from 999 down to 100
        for j in range(999, 99, -1):
            product = i * j
            if is_palindrome(product) and product < n:
                answer = max(answer, product)
    return answer


if __name__ == "__main__":
    print(f"{solution() = }")
