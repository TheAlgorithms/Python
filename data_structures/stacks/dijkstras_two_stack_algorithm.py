"""
Author: Alexander Joslin
GitHub: github.com/echoaj

We can use Dijkstra's two stack algorithm to solve an equation
such as: (5 + ((4 * 2) * (2 + 3)))

These are the algorithm's rules:
RULE 1: Scan the expression from left to right. When an operand is encountered, push it onto the the operand stack.
RULE 2: When an operator is encountered in the expression, push it onto the operator stack.
RULE 3: When a left parenthesis is encountered in teh expression, ignore it.
RULE 4: When a right parenthesis is encountered in the expression, pop an operator off the operator stack.
        The two operands it must operate on must be the last two operands pushed onto the operand stack.
        We therefore pop the operand stack twice, perform the operation, and push the result back onto the
        operand stack so it will be available for use as an operand of the next operator popped off the
        operator stack.
RULE 5: When the entire infix expression has been scanned, the value left on the operand stack represents
        the value of the expression.
"""


class Stack:
    def __init__(self):
        self.__array = []
        self.__len = 0
        self.underflow_error = False

    def is_empty(self):
        if self.__len == 0:
            return True
        else:
            return False

    def push(self, x):
        self.__array.append(x)
        self.__len += 1

    def pop(self):
        if not self.is_empty():  # if empty
            self.__array.pop()
            self.__len -= 1
            self.underflow_error = False
        else:  # if not empty
            self.underflow_error = True

    def peek(self):
        return self.__array[-1] if not self.is_empty() else None

    def length(self):
        return self.__len

    def print_stack(self):
        print(self.__array)


def main():
    equation = "(5 + ((4 * 2) * (2 + 3)))"
    operand_stack = Stack()
    operator_stack = Stack()

    for i in equation:
        if i.isdigit():
            # Rule 1
            operand_stack.push(int(i))
        elif i in ['+', '*', '-', '/', '%']:
            # Rule 2
            operator_stack.push(i)
        elif i == ')':
            # Rule 4
            opr1 = operator_stack.peek()
            operator_stack.pop()
            num1 = operand_stack.peek()
            operand_stack.pop()
            num2 = operand_stack.peek()
            operand_stack.pop()

            total = 0
            if opr1 == '+':
                total = num2 + num1
            elif opr1 == '-':
                total = num2 - num1
            elif opr1 == '*':
                total = num2 * num1
            elif opr1 == '/':
                total = num2 / num1
            elif opr1 == '%':
                total = num2 % num1

            operand_stack.push(total)
        else:
            # Rule 3
            pass

    # Rule 5
    print(operand_stack.peek()) # Result -> 45



if __name__ == "__main__":
    main()