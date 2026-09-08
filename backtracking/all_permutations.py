"""
In this problem, we want to determine all possible permutations
of the given sequence. We use backtracking to solve this problem.

Time complexity: O(n! * n),
where n denotes the length of the given sequence.
"""

from __future__ import annotations

from itertools import permutations


def permutation_tuple_to_list(arr: list[int | str]) -> list[list[int | str]]:
    """
    Default permutation output is list of tuples
    >>> permutation_tuple_to_list([1,2])
    [[1, 2], [2, 1]]
    >>> permutation_tuple_to_list(['a', 'b'])
    [['a', 'b'], ['b', 'a']]
    """
    return [list(output_tuple) for output_tuple in permutations(arr)]


def generate_all_permutations(sequence: list[int | str]) -> list[list[int | str]]:
    """
    >>> generate_all_permutations([])
    [[]]
    >>> generate_all_permutations([1])
    [[1]]
    >>> generate_all_permutations([1, 2])
    [[1, 2], [2, 1]]
    >>> generate_all_permutations([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> generate_all_permutations([-1, 2])
    [[-1, 2], [2, -1]]
    >>> generate_all_permutations([1, -2])
    [[1, -2], [-2, 1]]
    >>> generate_all_permutations(['a', 'b'])
    [['a', 'b'], ['b', 'a']]
    >>> from itertools import permutations
    >>> test_arr = [num for num in range(0, 6)]
    >>> generate_all_permutations(test_arr) == permutation_tuple_to_list(test_arr)
    True
    """
    output: list[list[int | str]] = []
    create_state_space_tree(sequence, [], 0, [0 for i in range(len(sequence))], output)
    return output


def create_state_space_tree(
    sequence: list[int | str],
    current_sequence: list[int | str],
    index: int,
    index_used: list[int],
    output: list[list[int | str]],
) -> None:
    """
    Creates a state space tree to iterate through each branch using DFS.
    We know that each state has exactly len(sequence) - index children.
    It terminates when it reaches the end of the given sequence.

    :param sequence: The input sequence for which permutations are generated.
    :param current_sequence: The current permutation being built.
    :param index: The current index in the sequence.
    :param index_used: list to track which elements are used in permutation.

    Example 1:
    >>> sequence = [1, 2, 3]
    >>> current_sequence = []
    >>> index_used = [False, False, False]
    >>> create_state_space_tree(sequence, current_sequence, 0, index_used)
    [1, 2, 3]
    [1, 3, 2]
    [2, 1, 3]
    [2, 3, 1]
    [3, 1, 2]
    [3, 2, 1]

    Example 2:
    >>> sequence = ["A", "B", "C"]
    >>> current_sequence = []
    >>> index_used = [False, False, False]
    >>> create_state_space_tree(sequence, current_sequence, 0, index_used)
    ['A', 'B', 'C']
    ['A', 'C', 'B']
    ['B', 'A', 'C']
    ['B', 'C', 'A']
    ['C', 'A', 'B']
    ['C', 'B', 'A']

    Example 3:
    >>> sequence = [1]
    >>> current_sequence = []
    >>> index_used = [False]
    >>> create_state_space_tree(sequence, current_sequence, 0, index_used)
    [1]
    """

    if index == len(sequence):
        # Copying b/c popping current_sequence is part of this recursive algo.
        # Can't have pointer to that arr
        current_sequence_copy = list(current_sequence)
        output.append(current_sequence_copy)
        return

    for i in range(len(sequence)):
        if not index_used[i]:
            current_sequence.append(sequence[i])
            index_used[i] = True
            # function spaced like this b/c linter 88 char limit
            create_state_space_tree(
                sequence, current_sequence, index + 1, index_used, output
            )
            current_sequence.pop()
            index_used[i] = False


"""
remove the comment to take an input from the user

print("Enter the elements")
sequence = list(map(int, input().split()))
"""

sequence: list[int | str] = [3, 1, 2, 4]
generate_all_permutations(sequence)

sequence_2: list[int | str] = ["A", "B", "C"]
generate_all_permutations(sequence_2)

if __name__ == "__main__":
    from doctest import testmod

    testmod()
