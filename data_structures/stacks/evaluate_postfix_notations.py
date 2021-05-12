from typing import Any, List

"""
The Reverse Polish Nation also known as Polish postfix notation
or simply postfix notation.
https://en.wikipedia.org/wiki/Reverse_Polish_notation
Classic examples of simple stack implementations
Valid operators are +, -, *, /.
Each operand may be an integer or another expression.
"""


def evaluate_postfix(postfix_notation: list) -> int:
    """
    >>> evaluate_postfix(["2", "1", "+", "3", "*"])
    9
    >>> evaluate_postfix(["4", "13", "5", "/", "+"])
    6
    >>> evaluate_postfix([])
    0
    """
    if not postfix_notation:
        return 0

    operations = {"+", "-", "*", "/"}
    stack: List[Any] = []

    for token in postfix_notation:
        if token in operations:
            b, a = stack.pop(), stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                if a * b < 0 and a % b != 0:
                    stack.append(a // b + 1)
                else:
                    stack.append(a // b)
        else:
            stack.append(int(token))

    return stack.pop()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
