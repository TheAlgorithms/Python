"""
Algorithm for calculating the most cost-efficient sequence for converting one string
into another.
The only allowed operations are
--- Cost to copy a character is copy_cost
--- Cost to replace a character is replace_cost
--- Cost to delete a character is delete_cost
--- Cost to insert a character is insert_cost
"""


def compute_transform_tables(
    source_string: str,
    destination_string: str,
    copy_cost: int,
    replace_cost: int,
    delete_cost: int,
    insert_cost: int,
) -> tuple[list[list[int]], list[list[str]]]:
    """
    Compute transformation tables for string alignment.

    Args:
        source_string (str): The source string.
        destination_string (str): The destination string.
        copy_cost (int): Cost of copying a character.
        replace_cost (int): Cost of replacing a character.
        delete_cost (int): Cost of deleting a character.
        insert_cost (int): Cost of inserting a character.

    Returns:
        tuple[list[list[int]], list[list[str]]]: A tuple containing two lists:
        - The first list is a table of minimum costs for transformations.
        - The second list is a table of transformation operations.

    Example:
        >>> costs, ops = compute_transform_tables("Python", "Algorithms", -1, 1, 2, 2)
        >>> len(costs)
        7
        >>> len(ops)
        7
        >>> len(costs[0])
        11
        >>> len(ops[0])
        11
    """

    source_seq = list(source_string)
    destination_seq = list(destination_string)
    len_source_seq = len(source_seq)
    len_destination_seq = len(destination_seq)

    costs = [
        [0 for _ in range(len_destination_seq + 1)] for _ in range(len_source_seq + 1)
    ]
    ops = [
        ["0" for _ in range(len_destination_seq + 1)] for _ in range(len_source_seq + 1)
    ]

    for i in range(1, len_source_seq + 1):
        costs[i][0] = i * delete_cost
        ops[i][0] = f"D{source_seq[i - 1]:c}"

    for i in range(1, len_destination_seq + 1):
        costs[0][i] = i * insert_cost
        ops[0][i] = f"I{destination_seq[i - 1]:c}"

    for i in range(1, len_source_seq + 1):
        for j in range(1, len_destination_seq + 1):
            if source_seq[i - 1] == destination_seq[j - 1]:
                costs[i][j] = costs[i - 1][j - 1] + copy_cost
                ops[i][j] = f"C{source_seq[i - 1]:c}"
            else:
                costs[i][j] = costs[i - 1][j - 1] + replace_cost
                ops[i][j] = f"R{source_seq[i - 1]:c}" + str(destination_seq[j - 1])

            if costs[i - 1][j] + delete_cost < costs[i][j]:
                costs[i][j] = costs[i - 1][j] + delete_cost
                ops[i][j] = f"D{source_seq[i - 1]:c}"

            if costs[i][j - 1] + insert_cost < costs[i][j]:
                costs[i][j] = costs[i][j - 1] + insert_cost
                ops[i][j] = f"I{destination_seq[j - 1]:c}"

    return costs, ops


def assemble_transformation(ops: list[list[str]], i: int, j: int) -> list[str]:
    """
    Assemble a list of transformation operations.

    Args:
        ops (list[list[str]]): The table of transformation operations.
        i (int): The current row.
        j (int): The current column.

    Returns:
        list[str]: A list of transformation operations.

    Example:
        >>> ops = [["0", "0", "0"], ["0", "Ct", "Dh"], ["0", "Ie", "Ri"]]
        >>> assemble_transformation(ops, 2, 2)
        ['Ri', 'Ie', 'Ct', 'Dh']
        >>> assemble_transformation(ops, 1, 1)
        ['Ct', 'Dh']
        >>> assemble_transformation(ops, 0, 0)
        []
    """
    if i == 0 and j == 0:
        return []
    else:
        if ops[i][j][0] in {"C", "R"}:
            seq = assemble_transformation(ops, i - 1, j - 1)
            seq.append(ops[i][j])
            return seq
        elif ops[i][j][0] == "D":
            seq = assemble_transformation(ops, i - 1, j)
            seq.append(ops[i][j])
            return seq
        else:
            seq = assemble_transformation(ops, i, j - 1)
            seq.append(ops[i][j])
            return seq


if __name__ == "__main__":
    _, operations = compute_transform_tables("Python", "Algorithms", -1, 1, 2, 2)

    m = len(operations)
    n = len(operations[0])
    sequence = assemble_transformation(operations, m - 1, n - 1)

    string = list("Python")
    i = 0
    cost = 0

    for op in sequence:
        print("".join(string))
        if op[0] == "C":
            print("%-16s" % "Copy %c" % op[1])
            cost -= 1
        elif op[0] == "R":
            string[i] = op[2]
            print("%-16s" % ("Replace %c" % op[1] + " with " + str(op[2])))
            cost += 1
        elif op[0] == "D":
            string.pop(i)
            print("%-16s" % "Delete %c" % op[1])
            cost += 2
        else:
            string.insert(i, op[1])
            print("%-16s" % "Insert %c" % op[1])
            cost += 2

        i += 1

    print("".join(string))
    print("Cost: ", cost)
    print("Minimum cost: " + str(cost))
    import doctest

    doctest.testmod()
