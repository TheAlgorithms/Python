def evaluate_postfix(expression):
    # Initialize an empty stack to store operands
    stack = []

    # Tokenize the input expression by splitting it on spaces
    tokens = expression.split()

    for token in tokens:
        if token.isnumeric():
            # If the token is a number, push it onto the stack
            stack.append(int(token))
        elif token in "+-*/^":
            # If the token is an operator, pop the top two operands from the stack
            operand2 = stack.pop()
            operand1 = stack.pop()

            # Perform the operation and push the result back onto the stack
            if token == "+":
                result = operand1 + operand2
            elif token == "-":
                result = operand1 - operand2
            elif token == "*":
                result = operand1 * operand2
            elif token == "/":
                result = operand1 / operand2
            elif token == "^":
                result = operand1**operand2

            stack.append(result)

    # The final result should be on top of the stack
    return stack[0]


if __name__ == "__main__":
    import doctest

    result = evaluate_postfix("3 4 2 1 - * +")
    print(result)
    doctest.testmod()
