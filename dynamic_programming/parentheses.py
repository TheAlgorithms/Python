import math


def calculate(a, b, op) -> int:
    """
    Return the value after evaluating the expression
    """
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    else:
        return a * b


def MinandMax(M, m, i, j, operator) -> int:
    min_value = math.inf
    max_value = -math.inf
    for k in range(i, j):
        a = calculate(M[i][k], M[k + 1][j], operator[k])
        b = calculate(M[i][k], m[k + 1][j], operator[k])
        c = calculate(m[i][k], M[k + 1][j], operator[k])
        d = calculate(m[i][k], m[k + 1][j], operator[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value


def parentheses(operand, operator) -> int:
    """
    Return the maximum value of the expression
    >>> 1+5
    6
    >>> 5-8+7*4-8+9
    200
    """
    n = len(operand)
    m = [[None for x in range(n)] for x in range(n)]
    M = [[None for x in range(n)] for x in range(n)]
    for i in range(n):
        m[i][i] = operand[i]
        M[i][i] = operand[i]
    for s in range(1, n):
        for i in range(0, n - s):
            j = i + s
            m[i][j], M[i][j] = MinandMax(M, m, i, j, operator)
    return M[0][n - 1]


expression = input()
operator, operand = [], []
for i in expression:
    if i in ("+", "-", "*"):
        operator.append(i)
    else:
        operand.append(int(i))
answer = parentheses(operand, operator)
f"{answer}"
