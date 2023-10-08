"""
Python3 program to evaluate a prefix expression.
"""

calc = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


def is_operand(char: chr) -> bool:
    """
    Return True if the given char char is an operand, e.g. it is a number
    >>> is_operand("1")
    True
    >>> is_operand("+")
    False
    """
    return char.isdigit()


def evaluate(expression: str) -> int | float:
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
    for char in expression.split()[::-1]:
        # push operand to stack
        if is_operand(char):
            stack.append(int(char))

        else:
            # pop values from stack can calculate the result
            # push the result into the stack again
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(calc[char](operand1, operand2))

    return stack.pop()


# Driver code
if __name__ == "__main__":
    from doctest import testmod

    testmod()

    test_expression = "+ 9 * 2 6"
    print(evaluate(test_expression))

    test_expression = "/ * 10 2 + 4 1 "
    print(evaluate(test_expression))
