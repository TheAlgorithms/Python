def evaluate_postfix(expression):
    # Initialize an empty stack to hold operands
    stack = []

    # Split the postfix expression into tokens (operands and operators)
    for char in expression.split():
        if char.isnumeric():
            # If the token is a numeric operand, push it onto the stack
            stack.append(int(char))
        elif char in '+-*/^':
            # If the token is an operator
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2
            elif char == '^':
                result = operand1 ** operand2
            # Push the result back onto the stack
            stack.append(result)

    # The final result should be the only element left in the stack
    return stack[0]

postfix_expression = "3 4 2 1 - * +"
result = evaluate_postfix(postfix_expression)
print(result)
