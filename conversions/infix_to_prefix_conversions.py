"""
Infix to Prefix Expression Converter
This script defines functions to convert infix expressions to prefix expressions
using the shunting-yard algorithm. It also includes definitions for SI and Binary
unit prefixes.
Author: "Arunkumar [halfhearted]"
Date: "02-10-2023"
"""


from __future__ import annotations
from enum import Enum, unique
from typing import TypeVar

# Create a generic variable that can be 'Enum', or any subclass.
T = TypeVar("T", bound=Enum)


@unique
class BinaryUnit(Enum):
    yotta = 80
    zetta = 70
    exa = 60
    peta = 50
    tera = 40
    giga = 30
    mega = 20
    kilo = 10


@unique
class SIUnit(Enum):
    yotta = 24
    zetta = 21
    exa = 18
    peta = 15
    tera = 12
    giga = 9
    mega = 6
    kilo = 3
    hecto = 2
    deca = 1
    deci = -1
    centi = -2
    milli = -3
    micro = -6
    nano = -9
    pico = -12
    femto = -15
    atto = -18
    zepto = -21
    yocto = -24

    @classmethod
    def get_positive(cls: type[T]) -> dict:
        """
        Returns a dictionary with only the elements of this enum
        that have a positive value.
        """
        return {unit.name: unit.value for unit in cls if unit.value > 0}

    @classmethod
    def get_negative(cls: type[T]) -> dict:
        """
        Returns a dictionary with only the elements of this enum
        that have a negative value.
        """
        return {unit.name: unit.value for unit in cls if unit.value < 0}


def infix_to_prefix(expression):
    """
    Convert an infix expression to a prefix expression.
    """

    def precedence(operator):
        precedence_dict = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
        return precedence_dict.get(operator, 0)

    def is_operator(char):
        return char in "+-*/^"

    def infix_to_postfix(infix_expr):
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
    postfix_expr = infix_to_postfix(infix_expr)
    # Reverse the postfix expression to get prefix
    prefix_expr = postfix_expr[::-1]
    return prefix_expr


# Example usage:
if __name__ == "__main__":
    import doctest

    doctest.testmod()
