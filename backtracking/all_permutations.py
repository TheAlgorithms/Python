"""
Backtracking: generate all permutations of a sequence.

Time complexity: O(n! * n), where n is length of sequence.
"""

from __future__ import annotations
from typing import List, Union

Element = Union[int, str]


def generate_all_permutations(sequence: List[Element]) -> List[List[Element]]:
    """
    Generate and return all permutations of the given sequence.

    :param sequence: The input sequence.
    :return: A list of permutations (each permutation is a list).

    Example 1 (integers):
    >>> generate_all_permutations([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    Example 2 (strings):
    >>> generate_all_permutations(["A", "B", "C"])
    [['A', 'B', 'C'], ['A', 'C', 'B'], ['B', 'A', 'C'], ['B', 'C', 'A'], ['C', 'A', 'B'], ['C', 'B', 'A']]

    Example 3 (single element):
    >>> generate_all_permutations([1])
    [[1]]

    Example 4 (empty sequence):
    >>> generate_all_permutations([])
    [[]]
    """
    result: List[List[Element]] = []
    index_used = [False] * len(sequence)
    create_state_space_tree(sequence, [], 0, index_used, result)
    return result


def create_state_space_tree(
    sequence: List[Element],
    current_sequence: List[Element],
    index: int,
    index_used: List[bool],
    result: List[List[Element]],
) -> None:
    """
    Backtracking helper that appends permutations into result.

    Example:
    >>> res = []
    >>> create_state_space_tree([1, 2], [], 0, [False, False], res)
    >>> res
    [[1, 2], [2, 1]]
    """
    if index == len(sequence):
        # append a shallow copy
        result.append(current_sequence[:])
        return

    for i in range(len(sequence)):
        if not index_used[i]:
            current_sequence.append(sequence[i])
            index_used[i] = True
            create_state_space_tree(
                sequence, current_sequence, index + 1, index_used, result
            )
            current_sequence.pop()
            index_used[i] = False


if __name__ == "__main__":
    # example usage; kept under __main__ so it doesn't run on import/tests
    print(generate_all_permutations([3, 1, 2, 4]))
    print(generate_all_permutations(["A", "B", "C"]))
