from Stack import Stack

__author__ = 'Omkar Pathak'


def balanced_parentheses(parentheses):
    """ Use a stack to check if a string of parentheses are balanced."""
    stack = Stack(len(parentheses))
    for parenthesis in parentheses:
        if parenthesis == '(':
            stack.push(parenthesis)
        elif parenthesis == ')':
            stack.pop()
    return not stack.is_empty()


if __name__ == '__main__':
    examples = ['((()))', '((())']
    print('Balanced parentheses demonstration:\n')
    for example in examples:
        print(example + ': ' + str(balanced_parentheses(example)))
