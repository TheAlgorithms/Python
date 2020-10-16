from typing import Any, List

"""
        In this problem, we want to determine all possible subsequences
        of the given sequence. We use backtracking to solve this problem.

        Time complexity: O(2^n),
        where n denotes the length of the given sequence.
"""


def generate_all_subsequences(sequence: List[Any]) -> None:
    create_state_space_tree(sequence, [], 0)


def create_state_space_tree(
    sequence: List[Any], current_subsequence: List[Any], index: int
) -> None:
    """
    Creates a state space tree to iterate through each branch using DFS.
    We know that each state has exactly two children.
    It terminates when it reaches the end of the given sequence.
    """

    if index == len(sequence):
        print(current_subsequence)
        return

    create_state_space_tree(sequence, current_subsequence, index + 1)
    current_subsequence.append(sequence[index])
    create_state_space_tree(sequence, current_subsequence, index + 1)
    current_subsequence.pop()


"""
remove the comment to take an input from the user

print("Enter the elements")
sequence = list(map(int, input().split()))
"""

sequence = [3, 1, 2, 4]
generate_all_subsequences(sequence)

sequence = ["A", "B", "C"]
generate_all_subsequences(sequence)
