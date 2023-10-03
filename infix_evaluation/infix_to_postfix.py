def infix_to_postfix(expression):
    # Define operator precedence
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    # Initialize an empty list to store the output
    output = []
    # Initialize an empty stack
    stack = []

    # Iterate through each character in the expression
    for char in expression:
        if char.isalnum():
            # If the character is an operand, add it to the output
            output.append(char)
        elif char in "+-*/^":
            # If the character is an operator
            while stack and precedence[char] <= precedence.get(stack[-1], 0):
                # Pop operators from the stack and add to the output
                output.append(stack.pop())
            # Push the current operator onto the stack
            stack.append(char)
        elif char == "(":
            # If an open parenthesis is encountered, push it onto the stack
            stack.append(char)
        elif char == ")":
            # If a close parenthesis is encountered
            while stack and stack[-1] != "(":
                # Pop operators from the stack and add to the output until an open parenthesis is found
                output.append(stack.pop())
            # Pop the open parenthesis from the stack
            stack.pop()

    # Pop any remaining operators from the stack and add to the output
    while stack:
        output.append(stack.pop())

    # Convert the output list to a string and return
    return "".join(output)


infix_expression = "3 + 4 * (2 - 1)"
postfix_expression = infix_to_postfix(infix_expression)
print(postfix_expression)
