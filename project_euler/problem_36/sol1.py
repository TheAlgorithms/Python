"""
Double-base palindromes
Problem 36
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""
def is_palindrome(n):
    n = str(n)

    if n == n[::-1]:
        return True
    else:
        return False


def solution(n):
    """Return the sum of all numbers, less than n , which are palindromic in
    base 10 and base 2.

    >>> solution(1000000)
    872187
    >>> solution(500000)
    286602
    >>> solution(100000)
    286602
    >>> solution(1000)
    1772
    >>> solution(100)
    157
    >>> solution(10)
    25
    >>> solution(2)
    1
    >>> solution(1)
    0
    """
    total = 0

    for i in range(1, n):
        if is_palindrome(i) and is_palindrome(bin(i).split("b")[1]):
            total += i
    return total


if __name__ == "__main__":
    print(solution(int(str(input().strip()))))
