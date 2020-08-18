from typing import List, Tuple

"""
Algorithm for calculating the most cost-efficient sequence for converting one string
into another.
The only allowed operations are
---Copy character with cost cC
---Replace character with cost cR
---Delete character with cost cD
---Insert character with cost cI
"""


def compute_transform_tables(
    X: str, Y: str, cC: int, cR: int, cD: int, cI: int
) -> Tuple[List[int], List[str]]:
    X: List[str] = list(X)
    Y: List[str] = list(Y)
    m: int = len(X)
    n: int = len(Y)

    costs: List[List[int]] = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    ops: List[List[int]] = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

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


def assemble_transformation(ops: List[str], i: int, j: int) -> List[str]:
    if i == 0 and j == 0:
        seq: List = []
        return seq
    else:
        if ops[i][j][0] == "C" or ops[i][j][0] == "R":
            seq: List = assemble_transformation(ops, i - 1, j - 1)
            seq.append(ops[i][j])
            return seq
        elif ops[i][j][0] == "D":
            seq: List = assemble_transformation(ops, i - 1, j)
            seq.append(ops[i][j])
            return seq
        else:
            seq: List = assemble_transformation(ops, i, j - 1)
            seq.append(ops[i][j])
            return seq


if __name__ == "__main__":
    _, operations = compute_transform_tables("Python", "Algorithms", -1, 1, 2, 2)

    m: int = len(operations)
    n: int = len(operations[0])
    sequence: List = assemble_transformation(operations, m - 1, n - 1)

    string: List[str] = list("Python")
    i: int = 0
    cost: int = 0

    with open("min_cost.txt", "w") as file:
        for op in sequence:
            print("".join(string))

            if op[0] == "C":
                file.write("%-16s" % "Copy %c" % op[1])
                file.write("\t\t\t" + "".join(string))
                file.write("\r\n")

                cost -= 1
            elif op[0] == "R":
                string[i] = op[2]

                file.write("%-16s" % ("Replace %c" % op[1] + " with " + str(op[2])))
                file.write("\t\t" + "".join(string))
                file.write("\r\n")

                cost += 1
            elif op[0] == "D":
                string.pop(i)

                file.write("%-16s" % "Delete %c" % op[1])
                file.write("\t\t\t" + "".join(string))
                file.write("\r\n")

                cost += 2
            else:
                string.insert(i, op[1])

                file.write("%-16s" % "Insert %c" % op[1])
                file.write("\t\t\t" + "".join(string))
                file.write("\r\n")

                cost += 2

            i += 1

        print("".join(string))
        print("Cost: ", cost)

        file.write("\r\nMinimum cost: " + str(cost))
