"""
Given a string s, partition s such that every substring of the
partition is a palindrome.
Find the minimum cuts needed for a palindrome partitioning of s.

Time Complexity: O(n^2)
Space Complexity: O(n^2)
For other explanations refer to: https://www.youtube.com/watch?v=_H8V5hJUGd0
"""


def find_minimum_partitions(string: str) -> int:
    """
    Returns the minimum cuts needed for a palindrome partitioning of string

    >>> find_minimum_partitions("aab")
    1
    >>> find_minimum_partitions("aaa")
    0
    >>> find_minimum_partitions("ababbbabbababa")
    3
    """
    length = len(string)
    cut = [0] * length
    is_palindromic = [[False for i in range(length)] for j in range(length)]
    for i, c in enumerate(string):
        mincut = i
        for j in range(i + 1):
            if c == string[j] and (i - j < 2 or is_palindromic[j + 1][i - 1]):
                is_palindromic[j][i] = True
                mincut = min(mincut, 0 if j == 0 else (cut[j - 1] + 1))
        cut[i] = mincut
    return cut[length - 1]


if __name__ == "__main__":
    s = input("Enter the string: ").strip()
    ans = find_minimum_partitions(s)
    print(f"Minimum number of partitions required for the '{s}' is {ans}")
