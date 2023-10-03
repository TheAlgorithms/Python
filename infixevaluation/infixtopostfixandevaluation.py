def infix_to_postfix(expression):
    def precedence(operator):
        precedence_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedence_dict.get(operator, 0)

    def is_operator(char):
        return char in "+-*/^"

    postfix = []
    stack = []

    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Pop the '('
        elif is_operator(char):
            while stack and stack[-1] != '(' and precedence(char) <= precedence(stack[-1]):
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)

def evaluate_postfix(expression):
    stack = []

    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        elif char in "+-*/^":
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
            stack.append(result)

    return stack.pop()

# Example usage:
infix_expression = "3 + 4 * (2 - 1)"
postfix_expression = infix_to_postfix(infix_expression)
print("Infix Expression:", infix_expression)
print("Postfix Expression:", postfix_expression)
result = evaluate_postfix(postfix_expression)
print("Result of Postfix Evaluation:", result)
