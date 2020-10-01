'''
The Reverse Polish Nation also known as Polish postfix notation or simply postfix notation
https://en.wikipedia.org/wiki/Reverse_Polish_notation
Classic examples of simple stack implementations
Valid operators are +, -, *, /. Each operand may be an integer or another expression.
'''
def evaluate_postfix_notation(postfix_notation):
    operations = {'+', '-', '*', '/'}
    stack = []

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


assert evaluate_postfix_notation(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
# (10 * (6 / ((9 + 3) * -11))) + 17) + 5

assert evaluate_postfix_notation(["2", "1", "+", "3", "*"]) == 9
# ((2 + 1) * 3) = 9

assert evaluate_postfix_notation(["4", "13", "5", "/", "+"]) == 6
# (4 + (13 / 5)) = 6
