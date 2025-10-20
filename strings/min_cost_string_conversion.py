"""
Algorithm for calculating the most cost-efficient sequence for converting one string
into another (Levenshtein distance).
The allowed operations are insertion, deletion, or substitution of a single character.
"""

import doctest


def min_cost_string_conversion(str1: str, str2: str) -> int:
    """
    Calculates the minimum cost (standard Levenshtein distance) to convert str1 to str2.
    The cost of insertion, deletion, and substitution is 1. The cost of a copy is 0.

    This is a user-friendly wrapper around the more detailed compute_transform_tables.

    Args:
        str1: The source string.
        str2: The target string.

    Returns:
        The minimum number of operations required to convert str1 to str2.

    Doctests:
        >>> min_cost_string_conversion("apple", "apply")
        1
        >>> min_cost_string_conversion("sunday", "saturday")
        3
        >>> min_cost_string_conversion("test", "test")
        0
        >>> min_cost_string_conversion("", "")
        0
        >>> min_cost_string_conversion("kitten", "sitting")
        3
    """
    costs, _ = compute_transform_tables(
        source_string=str1,
        destination_string=str2,
        copy_cost=0,
        replace_cost=1,
        delete_cost=1,
        insert_cost=1,
    )
    return costs[-1][-1]


def compute_transform_tables(
    source_string: str,
    destination_string: str,
    copy_cost: int,
    replace_cost: int,
    delete_cost: int,
    insert_cost: int,
) -> tuple[list[list[int]], list[list[str]]]:
    """
    Finds the most cost efficient sequence for converting one string into another
    using dynamic programming with specified costs.
    """
    len_source_seq = len(source_string)
    len_destination_seq = len(destination_string)
    costs = [
        [0 for _ in range(len_destination_seq + 1)] for _ in range(len_source_seq + 1)
    ]
    ops = [
        ["0" for _ in range(len_destination_seq + 1)] for _ in range(len_source_seq + 1)
    ]

    for i in range(1, len_source_seq + 1):
        costs[i][0] = i * delete_cost
        ops[i][0] = f"D{source_string[i - 1]}"

    for j in range(1, len_destination_seq + 1):
        costs[0][j] = j * insert_cost
        ops[0][j] = f"I{destination_string[j - 1]}"

    for i in range(1, len_source_seq + 1):
        for j in range(1, len_destination_seq + 1):
            if source_string[i - 1] == destination_string[j - 1]:
                costs[i][j] = costs[i - 1][j - 1] + copy_cost
                ops[i][j] = f"C{source_string[i - 1]}"
            else:
                costs[i][j] = costs[i - 1][j - 1] + replace_cost
                ops[i][j] = f"R{source_string[i - 1]}{destination_string[j - 1]}"

            if costs[i - 1][j] + delete_cost < costs[i][j]:
                costs[i][j] = costs[i - 1][j] + delete_cost
                ops[i][j] = f"D{source_string[i - 1]}"

            if costs[i][j - 1] + insert_cost < costs[i][j]:
                costs[i][j] = costs[i][j - 1] + insert_cost
                ops[i][j] = f"I{destination_string[j - 1]}"

    return costs, ops


def assemble_transformation(ops: list[list[str]], i: int, j: int) -> list[str]:
    """
    Assembles the list of transformations based on the ops table.
    """
    if i == 0 and j == 0:
        return []
    op_code = ops[i][j][0]
    if op_code in {"C", "R"}:
        seq = assemble_transformation(ops, i - 1, j - 1)
    elif op_code == "D":
        seq = assemble_transformation(ops, i - 1, j)
    else:  # op_code == "I"
        seq = assemble_transformation(ops, i, j - 1)
    seq.append(ops[i][j])
    return seq


if __name__ == "__main__":
    doctest.testmod()