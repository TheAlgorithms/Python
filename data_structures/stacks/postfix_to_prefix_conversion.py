"""
Functions:
- postfix_to_prefix(expression): Converts a postfix expression to a prefix expression.
"""

from .stack import Stack


def postfix_to_prefix(expression_str: str) -> str:
    """
    Converts a postfix expression to a prefix expression.

    Args:
        expression (str): A string representing a postfix expression.

    Returns:
        str: A string representing the equivalent prefix expression.

    Raises:
        IndexError: If the expression is invalid or contains an invalid operator.

    Example:
        >>> postfix_to_prefix('23+5*')
        '*+235'
    """
    stack: Stack[str] = Stack()
    operators = {"+", "-", "*", "/", "^"}

    for char in expression_str:
        if char not in operators:
            stack.push(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.push(char + operand2 + operand1)

    return stack.pop()


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    postfix_expression = "ab+c*"

    print("Postfix to infix demo\n")
    print("Postfix expression:", postfix_expression)
    prefix_expression = postfix_to_prefix(postfix_expression)
    print("Prefix expression:", prefix_expression)
