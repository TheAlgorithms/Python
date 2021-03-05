"""
https://en.wikipedia.org/wiki/Infix_notation
https://en.wikipedia.org/wiki/Reverse_Polish_notation
https://en.wikipedia.org/wiki/Shunting-yard_algorithm
"""

from .balanced_parentheses import balanced_parentheses
from .stack import Stack


def precedence(char: str) -> int:
    """
    Return integer value representing an operator's precedence, or
    order of operation.
    https://en.wikipedia.org/wiki/Order_of_operations
    """
    return {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}.get(char, -1)


def infix_to_postfix(expression_str: str) -> str:
    """
    >>> infix_to_postfix("(1*(2+3)+4))")
    Traceback (most recent call last):
    ...
    ValueError: Mismatched parentheses
    >>> infix_to_postfix("")
    ''
    >>> infix_to_postfix("3+2")
    '3 2 +'
    >>> infix_to_postfix("(3+4)*5-6")
    '3 4 + 5 * 6 -'
    >>> infix_to_postfix("(1+2)*3/4-5")
    '1 2 + 3 * 4 / 5 -'
    >>> infix_to_postfix("a+b*c+(d*e+f)*g")
    'a b c * + d e * f + g * +'
    >>> infix_to_postfix("x^y/(5*z)+2")
    'x y ^ 5 z * / 2 +'
    """
    if not balanced_parentheses(expression_str):
        raise ValueError("Mismatched parentheses")
    stack = Stack()
    postfix = []
    for char in expression_str:
        if char.isalpha() or char.isdigit():
            postfix.append(char)
        elif char == "(":
            stack.push(char)
        elif char == ")":
            while not stack.is_empty() and stack.peek() != "(":
                postfix.append(stack.pop())
            stack.pop()
        else:
            while not stack.is_empty() and precedence(char) <= precedence(stack.peek()):
                postfix.append(stack.pop())
            stack.push(char)
    while not stack.is_empty():
        postfix.append(stack.pop())
    return " ".join(postfix)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    expression = "a+b*(c^d-e)^(f+g*h)-i"

    print("Infix to Postfix Notation demonstration:\n")
    print("Infix notation: " + expression)
    print("Postfix notation: " + infix_to_postfix(expression))
