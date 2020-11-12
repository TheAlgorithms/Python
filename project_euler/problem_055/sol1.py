"""
Lychrel numbers
Problem 55: https://projecteuler.net/problem=55

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,
349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337
That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196,
never produce a palindrome. A number that never forms a palindrome through the
reverse and add process is called a Lychrel number. Due to the theoretical nature
of these numbers, and for the purpose of this problem, we shall assume that a number
is Lychrel until proven otherwise. In addition you are given that for every number
below ten-thousand, it will either (i) become a palindrome in less than fifty
iterations, or, (ii) no one, with all the computing power that exists, has managed
so far to map it to a palindrome. In fact, 10677 is the first number to be shown
to require over fifty iterations before producing a palindrome:
4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers;
the first example is 4994.
How many Lychrel numbers are there below ten-thousand?
"""


def is_palindrome(n: int) -> bool:
    """
    Returns True if a number is palindrome.
    >>> is_palindrome(12567321)
    False
    >>> is_palindrome(1221)
    True
    >>> is_palindrome(9876789)
    True
    """
    return str(n) == str(n)[::-1]


def sum_reverse(n: int) -> int:
    """
    Returns the sum of n and reverse of n.
    >>> sum_reverse(123)
    444
    >>> sum_reverse(3478)
    12221
    >>> sum_reverse(12)
    33
    """
    return int(n) + int(str(n)[::-1])


def solution(limit: int = 10000) -> int:
    """
    Returns the count of all lychrel numbers below limit.
    >>> solution(10000)
    249
    >>> solution(5000)
    76
    >>> solution(1000)
    13
    """
    lychrel_nums = []
    for num in range(1, limit):
        iterations = 0
        a = num
        while iterations < 50:
            num = sum_reverse(num)
            iterations += 1
            if is_palindrome(num):
                break
        else:
            lychrel_nums.append(a)
    return len(lychrel_nums)


if __name__ == "__main__":
    print(f"{solution() = }")
