""" Infix and postfix are notations used to represent mathematical expressions.
Infix notation is the standard way we write mathematical expressions,
where operators are placed between operands.
For example, "3 + 4" is in infix notation.
Postfix notation, also known as Reverse Polish Notation (RPN),
represents the same expression with operators placed after operands,
like "3 4 +".

Converting an infix expression to postfix notation is useful because it
makes it easier to evaluate expressions using a stack-based algorithm. """


def infix_to_postfix(expression):
    # Initialize an empty stack to store operators temporarily
    stack = []

    # Define the precedence of operators
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

    # Initialize an empty list to store the postfix expression
    postfix = []

    # Tokenize the input expression by splitting it on spaces
    tokens = expression.split()

    for token in tokens:
        if token.isnumeric():
            # If the token is a number, append it to the postfix list
            postfix.append(token)
        elif token in "+-*/^":
            # If the token is an operator, pop operators from the stack
            # and append them to the postfix list until a lower-precedence
            # operator is encountered or the stack is empty
            while (
                stack
                and stack[-1] in "+-*/^"
                and precedence[token] <= precedence[stack[-1]]
            ):
                postfix.append(stack.pop())
            # Push the current operator onto the stack
            stack.append(token)
        elif token == "(":
            # If the token is an opening parenthesis, push it onto the stack
            stack.append(token)
        elif token == ")":
            # If the token is a closing parenthesis, pop operators from the stack
            # and append them to the postfix list until an opening parenthesis is found
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())
            # Pop the opening parenthesis from the stack
            stack.pop()

    # Pop any remaining operators from the stack and append them to the postfix list
    while stack:
        postfix.append(stack.pop())

    # Join the elements of the postfix list to form the final postfix expression
    postfix_expression = " ".join(postfix)
    return postfix_expression


if __name__ == "__main__":
    import doctest

    result = infix_to_postfix("3 + 4 * ( 2 - 1 )")
    print(result)
    doctest.testmod()
