import math
from operator import add, sub, mul


operators = {"+": add, "-": sub, "*": mul}


def calculate(first_operand, second_operand, operator) -> int:
    """
    Return the value after evaluating the expression
    """
    return operators[operator](first_operand, second_operand)


def MinandMax(maximum_numbers, minimum_numbers, i, j, operator) -> int:
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


def parentheses(operand, operator) -> int:
    """
    Return the maximum value of the expression
    """
    number_of_operands = len(operand)
    minimum_numbers = [
        [None for x in range(number_of_operands)] for x in range(number_of_operands)
    ]
    maximum_numbers = [
        [None for x in range(number_of_operands)] for x in range(number_of_operands)
    ]
    for i in range(number_of_operands):
        minimum_numbers[i][i] = operand[i]
        maximum_numbers[i][i] = operand[i]
    for s in range(1, number_of_operands):
        for i in range(0, number_of_operands - s):
            j = i + s
            minimum_numbers[i][j], maximum_numbers[i][j] = MinandMax(
                maximum_numbers, minimum_numbers, i, j, operator
            )
    return maximum_numbers[0][number_of_operands - 1]


expression = input().strip()
operator, operand = [], []
for i in expression:
    if i in operators.keys():
        operator.append(i)
    else:
        operand.append(int(i))
answer = parentheses(operand, operator)
f"{answer}"
