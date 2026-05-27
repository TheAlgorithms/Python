"""
In this problem, we want to determine all possible permutations
of the given sequence. We use backtracking to solve this problem.

Time complexity: O(n! * n),
where n denotes the length of the given sequence.
"""

from __future__ import annotations

MAX_SEQUENCE_LENGTH = 8


def generate_all_permutations(sequence: list[int | str]) -> None:
    """
    Generate and print all permutations of the given sequence.

    Raises ValueError if the sequence exceeds MAX_SEQUENCE_LENGTH elements
    to prevent excessive CPU/memory usage (permutation count is O(n!)).

    >>> generate_all_permutations([1, 2, 3])
    [1, 2, 3]
    [1, 3, 2]
    [2, 1, 3]
    [2, 3, 1]
    [3, 1, 2]
    [3, 2, 1]
    >>> generate_all_permutations([1] * 9)
    Traceback (most recent call last):
        ...
    ValueError: Input sequence too long (max 8 elements).
    """
    if len(sequence) > MAX_SEQUENCE_LENGTH:
        raise ValueError(
            f"Input sequence too long (max {MAX_SEQUENCE_LENGTH} elements)."
        )
    create_state_space_tree(sequence, [], 0, [0 for i in range(len(sequence))])


def create_state_space_tree(
    sequence: list[int | str],
    current_sequence: list[int | str],
    index: int,
    index_used: list[int],
) -> None:
    """
    Generate a state space tree for the given sequence.
    We know that each state has exactly len(sequence) - index children.
    It terminates when it reaches the end of the given sequence.

    >>> create_state_space_tree([1, 2, 3], [], 0, [0, 0, 0])
    [1, 2, 3]
    [1, 3, 2]
    [2, 1, 3]
    [2, 3, 1]
    [3, 1, 2]
    [3, 2, 1]
    >>> create_state_space_tree(["a", "b", "c"], [], 0, [0, 0, 0])
    ['a', 'b', 'c']
    ['a', 'c', 'b']
    ['b', 'a', 'c']
    ['b', 'c', 'a']
    ['c', 'a', 'b']
    ['c', 'b', 'a']
    >>> create_state_space_tree([2, 2, 2], [], 0, [0, 0, 0])
    [2, 2, 2]
    [2, 2, 2]
    [2, 2, 2]
    [2, 2, 2]
    [2, 2, 2]
    [2, 2, 2]
    """
    if index == len(sequence):
        print(current_sequence)
        return

    for i in range(len(sequence)):
        if index_used[i] == 0:
            current_sequence.append(sequence[i])
            index_used[i] = 1
            create_state_space_tree(sequence, current_sequence, index + 1, index_used)
            current_sequence.pop()
            index_used[i] = 0


"""
remove the comment to take an input from the user

print("Enter the elements")
raw = input().split()
if len(raw) > MAX_SEQUENCE_LENGTH:
    raise ValueError(f"Input sequence too long (max {MAX_SEQUENCE_LENGTH} elements).")
# Try to convert each token to int; keep as str if conversion is not possible.
# This supports both integer and string elements, matching the function's type hints.
sequence: list[int | str] = []
for token in raw:
    try:
        sequence.append(int(token))
    except ValueError:
        sequence.append(token)
generate_all_permutations(sequence)
"""

sequence: list[int | str] = [3, 1, 2, 4]
generate_all_permutations(sequence)
