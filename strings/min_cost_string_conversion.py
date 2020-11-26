"""
Algorithm for calculating the most cost-efficient sequence for converting one string
into another.
The only allowed operations are
---Copy character with cost cC
---Replace character with cost cR
---Delete character with cost cD
---Insert character with cost cI
"""
import sys
from tempfile import TemporaryFile


def compute_transform_tables(
    X: list[str], Y: list[str], cC: int, cR: int, cD: int, cI: int
):
    X = list(X)
    Y = list(Y)
    m = len(X)
    n = len(Y)

    costs = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    ops = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        costs[i][0] = i * cD
        ops[i][0] = "D%c" % X[i - 1]

    for i in range(1, n + 1):
        costs[0][i] = i * cI
        ops[0][i] = "I%c" % Y[i - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                costs[i][j] = costs[i - 1][j - 1] + cC
                ops[i][j] = "C%c" % X[i - 1]
            else:
                costs[i][j] = costs[i - 1][j - 1] + cR
                ops[i][j] = "R%c" % X[i - 1] + str(Y[j - 1])

            if costs[i - 1][j] + cD < costs[i][j]:
                costs[i][j] = costs[i - 1][j] + cD
                ops[i][j] = "D%c" % X[i - 1]

            if costs[i][j - 1] + cI < costs[i][j]:
                costs[i][j] = costs[i][j - 1] + cI
                ops[i][j] = "I%c" % Y[j - 1]

    return costs, ops


def assemble_transformation(ops: list[list[str]], i: int, j: int):
    if i == 0 and j == 0:
        seq = []
        return seq
    else:
        if ops[i][j][0] == "C" or ops[i][j][0] == "R":
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


def run_algorithm(
    str1: str, str2: str, copy: int, replace: int, delete: int, insert: int
):
    _, operations = compute_transform_tables(str1, str2, copy, replace, delete, insert)

    m = len(operations)
    n = len(operations[0])
    sequence = assemble_transformation(operations, m - 1, n - 1)

    string = list(str1)
    i = 0
    cost = 0

    with TemporaryFile("w") as file:
        for op in sequence:
            print("".join(string))

            if op[0] == "C":
                file.write("%-16s" % "Copy %c" % op[1])
                file.write("\t\t\t" + "".join(string))
                file.write("\r\n")

                cost += copy
            elif op[0] == "R":
                string[i] = op[2]

                file.write("%-16s" % ("Replace %c" % op[1] + " with " + str(op[2])))
                file.write("\t\t" + "".join(string))
                file.write("\r\n")

                cost += replace
            elif op[0] == "D":
                string.pop()  # putting `i` would raise out of range

                file.write("%-16s" % "Delete %c" % op[1])
                file.write("\t\t\t" + "".join(string))
                file.write("\r\n")

                cost += delete
            else:
                string.insert(i, op[1])

                file.write("%-16s" % "Insert %c" % op[1])
                file.write("\t\t\t" + "".join(string))
                file.write("\r\n")

                cost += insert

            i += 1

        print("".join(string))
        print("Cost: ", cost)

        file.write("\r\nMinimum cost: " + str(cost))

    return cost


if __name__ == "__main__":  # pragma: no cover
    args_length = len(sys.argv)

    str1 = sys.argv[1] if args_length >= 2 else "Python"
    str2 = sys.argv[2] if args_length >= 3 else "Algorithms"

    default_costs = [0, 1, 2, 3]
    user_costs = list(map(int, sys.argv[3:])) if args_length >= 7 else []

    copy, replace, delete, insert = user_costs[:4] or default_costs

    min_cost = run_algorithm(str1, str2, copy, replace, delete, insert)
    print(f"Min Cost: {min_cost}")
