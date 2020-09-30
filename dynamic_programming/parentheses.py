import math
from typing import List
from operator import add, sub, mul


operators = {"+": add, "-": sub, "*": mul}


def calculate(first_operand: int, second_operand: int, operator: str) -> int:
    """
    Evaluate the expression and return the result.

    >>> calculate(2,2,"+")  # add()
    4
    >>> calculate(2,2,"-")  # sub()
    0
    >>> calculate(2,2,"*")  # mul()
    4
    """
    return operators[operator](first_operand, second_operand)


def MinandMax(minimum_numbers: List[List[int]], maximum_numbers: List[List[int]],
              i: int, j: int, operator: List[str]) -> int:
    """
    Return the minimum and maximum value obtained.

    >>> MinandMax([[1, None], [None, 5]], [[1, None], [None, 5]], 0, 1, ['+'])
    6 6
    >>> MinandMax([[2, 5, None], [None, 3, -3], [None, None, 6]],
    [[2, 5, None], [None, 3, -3], [None, None, 6]],0, 2, ['+', '-'])
    -1 -1
    """
    min_value = math.inf
    max_value = -math.inf
    for k in range(i, j):
        a = calculate(maximum_numbers[i][k], maximum_numbers[k + 1][j], operator[k])
        b = calculate(maximum_numbers[i][k], minimum_numbers[k + 1][j], operator[k])
        c = calculate(minimum_numbers[i][k], maximum_numbers[k + 1][j], operator[k])
        d = calculate(minimum_numbers[i][k], minimum_numbers[k + 1][j], operator[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value


def parentheses(operands: List[int], operator: List[str]) -> int:
    """
    Return the maximum value of the expression.

    >>> parentheses([1, 5], ['+'])
    6
    >>> parentheses([2, 3, 6], ['+', '-'])
    -1
    >>> parentheses([5, 8, 7, 4, 8, 9], ['-', '+', '*', '-', '+'])
    200
    """
    number_of_operands = len(operands)
    minimum_numbers = [
        [None for x in range(number_of_operands)] for x in range(number_of_operands)
    ]
    maximum_numbers = [
        [None for x in range(number_of_operands)] for x in range(number_of_operands)
    ]
    for i in range(number_of_operands):
        minimum_numbers[i][i] = operands[i]
        maximum_numbers[i][i] = operands[i]
    for s in range(1, number_of_operands):
        for i in range(0, number_of_operands - s):
            j = i + s
            minimum_numbers[i][j], maximum_numbers[i][j] = MinandMax(
                minimum_numbers, maximum_numbers, i, j, operator
            )
    return maximum_numbers[0][number_of_operands - 1]


if __name__ == "__main__":
    expression = input("Please provide a mathematical expression... ").strip()
    operator, operands = [], []
    expression = expression.replace(" ", "")
    digits = ""
    for c in expression:
        if c in operators:
            operands.append(int(digits))
            digits = ""
            operator.append(c)
        else:
            digits += c
    operands.append(int(digits))
    print(f"The result is {parentheses(operands, operator)}")
