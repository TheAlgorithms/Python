from __future__ import print_function
from __future__ import absolute_import
import string

from .stack import Stack

__author__ = 'Omkar Pathak'


def is_operand(char):
    return char in string.ascii_letters or char in string.digits


def precedence(char):
    """ Return integer value representing an operator's precedence, or
    order of operation.

    https://en.wikipedia.org/wiki/Order_of_operations
    """
    dictionary = {'+': 1, '-': 1,
                  '*': 2, '/': 2,
                  '^': 3}
    return dictionary.get(char, -1)


def infix_to_postfix(expression):
    """ Convert infix notation to postfix notation using the Shunting-yard
    algorithm.

    https://en.wikipedia.org/wiki/Shunting-yard_algorithm
    https://en.wikipedia.org/wiki/Infix_notation
    https://en.wikipedia.org/wiki/Reverse_Polish_notation
    """
    stack = Stack(len(expression))
    postfix = []
    for char in expression:
        if is_operand(char):
            postfix.append(char)
        elif char not in {'(', ')'}:
            while (not stack.is_empty()
                    and precedence(char) <= precedence(stack.peek())):
                postfix.append(stack.pop())
            stack.push(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            # Pop '(' from stack. If there is no '(', there is a mismatched
            # parentheses.
            if stack.peek() != '(':
                raise ValueError('Mismatched parentheses')
            stack.pop()
    while not stack.is_empty():
        postfix.append(stack.pop())
    return ' '.join(postfix)


if __name__ == '__main__':
    expression = 'a+b*(c^d-e)^(f+g*h)-i'

    print('Infix to Postfix Notation demonstration:\n')
    print('Infix notation: ' + expression)
    print('Postfix notation: ' + infix_to_postfix(expression))
