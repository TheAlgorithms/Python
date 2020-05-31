"""
Python3 program to evaluate a prefix expression.
"""

calc = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


def is_operand(c):
    """
    Return True if the given char c is an operand, e.g. it is a number

    >>> is_operand("1")
    True
    >>> is_operand("+")
    False
    """
    return c.isdigit()


def evaluate(expression):
    """
    Evaluate a given expression in prefix notation.
    Asserts that the given expression is valid.

    >>> evaluate("+ 9 * 2 6")
    21
    >>> evaluate("/ * 10 2 + 4 1 ")
    4.0
    """
    stack = []

    # iterate over the string in reverse order
    for c in expression.split()[::-1]:

        # push operand to stack
        if is_operand(c):
            stack.append(int(c))

        else:
            # pop values from stack can calculate the result
            # push the result onto the stack again
            o1 = stack.pop()
            o2 = stack.pop()
            stack.append(calc[c](o1, o2))

    return stack.pop()


# Driver code
if __name__ == "__main__":
    test_expression = "+ 9 * 2 6"
    print(evaluate(test_expression))

    test_expression = "/ * 10 2 + 4 1 "
    print(evaluate(test_expression))
