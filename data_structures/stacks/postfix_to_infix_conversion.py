"""
https://math.oxford.emory.edu/site/cs171/postfixExpressions/
https://en.wikipedia.org/wiki/Shunting_yard_algorithm
"""


def postfix_to_infix(postfix_expression: str) -> str:
    """
    Returns the infix expression for the given postfix expression as an argument
    >>> postfix_to_infix("")
    Traceback (most recent call last):
        ...
    ValueError: Invalid postfix expression.
    >>> postfix_to_infix("123+*4+")
    '((1*(2+3))+4)'
    >>> postfix_to_infix("abc*+de*f+g*+")
    '((a+(b*c))+(((d*e)+f)*g))'
    >>> postfix_to_infix("xy^5z*/2+")
    '(((x^y)/(5*z))+2)'
    >>> postfix_to_infix("232^^")
    '(2^(3^2))'
    >>> postfix_to_infix("32+")
    '(3+2)'
    """

    # Check for invalid input.
    if postfix_expression is None or postfix_expression == "":
        raise ValueError("Invalid postfix expression.")

    # Create a stack to store the operands and operators.
    stack = []

    # Iterate over the postfix expression.
    for item in postfix_expression:
        # If the item is an operand, push it onto the stack.
        if item not in ["+", "-", "*", "/", "^"]:
            stack.append(item)
        else:
            # If the item is an operator, pop the top two operands from the stack
            # and concatenate the operator between them.
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            infix_expression = "(" + operand_1 + item + operand_2 + ")"

            # Push the resulting infix expression onto the stack.
            stack.append(infix_expression)

    # The top element of the stack is the final infix expression.
    return stack.pop()


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    # Enter the posfix expression with no whitespaces.
    postfix_expression = "512+4*+3-"

    try:
        infix_expression = postfix_to_infix(postfix_expression)
        print("Infix expression: " + infix_expression)
    except ValueError as e:
        print(e)
