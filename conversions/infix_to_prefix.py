def is_operator(c):
    return c in ['+', '-', '*', '/']

def precedence(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    return 0

def infix_to_prefix(infix):
    # Reverse the infix expression
    reversed_infix = infix[::-1]
    stack = []
    prefix = []

    for char in reversed_infix:
        if char == ')':
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != ')':
                prefix.append(stack.pop())
            if stack and stack[-1] == ')':
                stack.pop()
        elif is_operator(char):
            while stack and precedence(stack[-1]) >= precedence(char):
                prefix.append(stack.pop())
            stack.append(char)
        else:
            prefix.append(char)

    while stack:
        prefix.append(stack.pop())

    # Reverse the resulting prefix expression
    prefix.reverse()

    return ''.join(prefix)

# Example usage
infix_expression = input("Enter infix expression: ")
prefix_expression = infix_to_prefix(infix_expression)
print("Infix Expression:", infix_expression)
print("Prefix Expression:", prefix_expression)
