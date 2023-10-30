"""
In this problem, we find all subsequences of a given list using backtracking.
Time Complexity: O(2^n), where n is the list's length.

Functions:
- generate_all_subsequences: Initiates backtracking and prints subsequences.
- create_state_space_tree: Recursively builds a state-space tree for subsequences.
"""

from __future__ import annotations
from typing import Any

def generate_all_subsequences(sequence: list[Any]) -> None:
    """Kickstarts the backtracking algorithm.

    Args:
    - sequence (list[Any]): Input list of elements.

    Returns:
    None: Outputs all subsequences to stdout.
    """
    create_state_space_tree(sequence, [], 0)

def create_state_space_tree(
    sequence: list[Any], current_subsequence: list[Any], index: int
) -> None:
    """Recursively constructs a state-space tree for subsequences.

    Args:
    - sequence (list[Any]): Original list.
    - current_subsequence (list[Any]): Current subsequence.
    - index (int): Current index in the original list.

    Returns:
    None: Outputs subsequences when reaching the end of the list.
    """
    if index == len(sequence):
        print(current_subsequence)
        return

    # Exclude current element
    create_state_space_tree(sequence, current_subsequence, index + 1)
    
    # Include current element
    current_subsequence.append(sequence[index])
    create_state_space_tree(sequence, current_subsequence, index + 1)
    
    # Backtracke it
    current_subsequence.pop()

if __name__ == "__main__":
    seq: list[Any] = [3, 1, 2, 4]
    generate_all_subsequences(seq)

    seq.clear()
    seq.extend(["A", "B", "C"])
    generate_all_subsequences(seq)
