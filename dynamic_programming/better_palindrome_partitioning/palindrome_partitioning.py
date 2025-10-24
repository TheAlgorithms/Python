"""Palindrome partitioning module.

Given a string s, partition s such that every substring of the partition is a palindrome.
Find the minimum cuts needed for a palindrome partitioning of s.

Time complexity: O(n^2)
Space complexity: O(n^2) [can be optimized to O(n)]
"""

from typing import List, Tuple, Union


def find_minimum_partitions(
    s: str, return_partitions: bool = False
) -> Union[int, Tuple[int, List[str]]]:
    """Return minimum cuts and optionally one valid partitioning."""
    n = len(s)
    if n <= 1 or s == s[::-1]:
        return (0, [s]) if return_partitions else 0

    # DP tables
    cuts = [0] * n
    is_palindrome = [[False] * n for _ in range(n)]
    parent = [-1] * n  # tracks where to jump back for reconstruction

    for i in range(n):
        min_cuts = i
        for j in range(i + 1):
            if s[j] == s[i] and (i - j <= 1 or is_palindrome[j + 1][i - 1]):
                is_palindrome[j][i] = True
                if j == 0:
                    min_cuts = 0
                    parent[i] = -1
                else:
                    candidate = cuts[j - 1] + 1
                    if candidate < min_cuts:
                        min_cuts = candidate
                        parent[i] = j - 1
        cuts[i] = min_cuts

    if not return_partitions:
        return cuts[-1]

    # Reconstruct one valid partitioning
    partitions: List[str] = []
    i = n - 1
    while i >= 0:
        start = parent[i] + 1 if parent[i] != -1 else 0
        partitions.append(s[start : i + 1])
        if parent[i] == -1:
            break
        i = parent[i]

    partitions.reverse()
    return (cuts[-1], partitions)


if __name__ == "__main__":
    s = input("enter the string:").strip()
    cuts, partitions = find_minimum_partitions(s, return_partitions=True)
    print(f"Minimum cuts required: {cuts}")
    print("One possible palindrome partitioning:")
    print(" | ".join(partitions))
