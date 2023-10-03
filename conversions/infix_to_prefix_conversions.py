"""
Infix to Prefix Expression Converter
This script defines functions to convert infix expressions to prefix expressions
using the shunting-yard algorithm. It also includes definitions for SI and Binary
unit prefixes.
Author: Arunkumar [halfhearted]
Date: 02-10-2023
"""
from __future__ import annotations


def infix_to_prefix(expression: str) -> str:
    """
    Convert an infix expression to a prefix expression.
    Args:
        expression (str): The infix expression to convert.
    Returns:
        str: The converted prefix expression.

    >>> infix_to_prefix("2+2")
    '+22'
    >>> infix_to_prefix("(1+2)*3")
    '*+123'
    >>> infix_to_prefix("a*(b+c)")
    '*a+bc'
    >>> infix_to_prefix("1+2*3")
    '+1*23'
    >>> infix_to_prefix("a * b + c / d")
    '+*ab/cd'
    """

    def precedence(operator: str) -> int:
        """
        Get the precedence of an operator.
        Args:
            operator (str): The operator.
        Returns:
            int: The precedence value.

        >>> precedence("+")
        1
        >>> precedence("-")
        1
        >>> precedence("*")
        2
        >>> precedence("/")
        2
        >>> precedence("^")
        3
        >>> precedence("%")
        0
        """
        precedence_dict = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
        return precedence_dict.get(operator, 0)

    def is_operator(char: str) -> bool:
        """
        Check if a character is an operator.
        Args:
            char (str): The character to check.
        Returns:
            bool: True if the character is an operator, False otherwise.

        >>> is_operator("+")
        True
        >>> is_operator("-")
        True
        >>> is_operator("*")
        True
        >>> is_operator("/")
        True
        >>> is_operator("^")
        True
        >>> is_operator("a")
        False
        """
        return char in "+-*/^"

    def infix_to_prefix(infix_expr: str) -> str:
        """
        Convert an infix expression to a prefix expression.
        Args:
            expression (str): The infix expression to convert.
        Returns:
            str: The converted prefix expression.

        >>> infix_to_prefix("2+2")
        '+22'
        >>> infix_to_prefix("(1+2)*3")
        '*+123'
        >>> infix_to_prefix("a*(b+c)")
        '*a+bc'
        >>> infix_to_prefix("1+2*3")
        '+1*23'
        >>> infix_to_prefix("a * b + c / d")
        '+*ab/cd'
        """
        postfix = []
        stack = []
        for char in infix_expr:
            if char.isalnum():  # Operand
                postfix.append(char)
            elif char == "(":  # Left parenthesis
                stack.append(char)
            elif char == ")":  # Right parenthesis
                while stack and stack[-1] != "(":
                    postfix.append(stack.pop())
                stack.pop()  # Pop '('
            elif is_operator(char):
                while (
                    stack
                    and stack[-1] != "("
                    and precedence(char) <= precedence(stack[-1])
                ):
                    postfix.append(stack.pop())
                stack.append(char)
        while stack:
            postfix.append(stack.pop())
        return "".join(postfix)

    # Reverse the input expression
    infix_expr = expression[::-1]
    # Swap '(' and ')' to handle correctly in reverse
    infix_expr = infix_expr.replace("(", "X").replace(")", "(").replace("X", ")")
    postfix_expr = infix_to_prefix(infix_expr)
    # Reverse the postfix expression to get prefix
    prefix_expr = postfix_expr[::-1]
    return prefix_expr


# Example usage:
if __name__ == "__main__":
    import doctest

    doctest.testmod()
