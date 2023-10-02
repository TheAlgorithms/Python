from stack import Stack  # Assuming you have a Stack class defined in 'stack.py'


def reverse_stack(stack):
    """
    Reverse the elements of a stack using another stack.

    Args:
    stack (Stack): The input stack to be reversed.

    Example:

    >>> s = Stack()
    >>> s.push(1)
    >>> s.push(2)
    >>> s.push(3)
    >>> reverse_stack(s)
    >>> reversed_stack = []
    >>> while not s.is_empty():
    ...     reversed_stack.append(s.pop())
    >>> reversed_stack
    [3, 2, 1]
    """
    if stack.is_empty():
        return

    reversed_stack = Stack()

    while not stack.is_empty():
        item = stack.pop()
        reversed_stack.push(item)

    while not reversed_stack.is_empty():
        item = reversed_stack.pop()
        stack.push(item)


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    reverse_stack(s)

    reversed_stack = []
    while not s.is_empty():
        reversed_stack.append(s.pop())

    print("Reversed Stack:", reversed_stack)
