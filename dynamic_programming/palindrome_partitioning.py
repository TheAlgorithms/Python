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
    n = len(string)
    cut = [0] * n
    ispalindrome = [[False for i in range(n)] for j in range(n)]
    for i in range(n):
        mincut = i
        for j in range(i + 1):
            if string[i] == string[j] and (i - j < 2 or ispalindrome[j + 1][i - 1]):
                ispalindrome[j][i] = True
                mincut = min(mincut, 0 if j == 0 else (cut[j - 1] + 1))
        cut[i] = mincut
    return cut[n - 1]


if __name__ == "__main__":
    s = input("Enter the string: ").strip()
    ans = find_minimum_partitions(s)
    print(f"Minimum number of partitions required for the string is {ans}")
