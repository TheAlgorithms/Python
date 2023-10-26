"""
In this problem, we aim to find all possible subsequences of a given sequence.
The algorithm employs backtracking to solve this problem.

Time Complexity: O(2^n),
where n represents the length of the given sequence.

Functions:
- generate_all_subsequences(sequence: list[Any]) -> None:
    Initiates the backtracking algorithm and prints the subsequences.

- create_state_space_tree(sequence: list[Any], current_subsequence: list[Any], index: int) -> None:
    Recursively creates the state-space tree to find all subsequences.
"""

from __future__ import annotations

from typing import Any


def generate_all_subsequences(sequence: list[Any]) -> None:
    create_state_space_tree(sequence, [], 0)
"""
    Generates all subsequences of the given sequence.

    Parameters:
    - sequence (List[Any]): The list of elements for which to generate subsequences.

    Returns:
    None: Prints all the subsequences.
"""
def create_state_space_tree(
    sequence: list[Any], current_subsequence: list[Any], index: int
) -> None:
    """
    Recursively creates a state-space tree to navigate through all possible subsequences.

    Parameters:
    - sequence (List[Any]): The original list of elements.
    - current_subsequence (List[Any]): The subsequence generated so far.
    - index (int): The index of the current element under consideration.

    Returns:
    None: Prints the subsequences when the end of the original sequence is reached.
   """

    if index == len(sequence):
        print(current_subsequence)
        return
    # Exclude the current element and move to the next.

    create_state_space_tree(sequence, current_subsequence, index + 1)
    # Include the current element in the subsequence and move to the next.

    current_subsequence.append(sequence[index])
    create_state_space_tree(sequence, current_subsequence, index + 1)
    # Backtrack to explore other possibilities.

    current_subsequence.pop()


if __name__ == "__main__":
    seq: list[Any] = [3, 1, 2, 4]
    generate_all_subsequences(seq)

    seq.clear()
    seq.extend(["A", "B", "C"])
    generate_all_subsequences(seq)
