"""
Given an set of numbers in a stack,
find the minimum value from the stack at O(1)

Problem: https://leetcode.com/problems/min-stack/description/
"""

stack: list[int] = []
min_stack: list[int] = []


def push(value: int) -> None:
    """
    Push into the main stack and track the minimum.
    If the value to insert < minimum, then push to min stack
    Returns None

    >>>
    """
    if len(stack) == 0:
        min_stack.append(value)
        stack.append(value)
        return

    if value < min_stack[-1]:
        min_stack.append(value)
    stack.append(value)


def pop() -> None:
    """
    Pop from the stack.
    If the popped value is the same as the min stack top,
    pop from the min stack as well

    Returns None

    >>>
    """
    if len(stack) == 0:
        print("Nothing on stack")
        return

    top = stack.pop()
    if len(min_stack) > 0 and top == min_stack[-1]:
        min_stack.pop()


def get_min() -> int:
    """
    Return the minimum element of the main stack by
    returning the top of the minimum stack

    Returns the minimum element (int)

    >>> push(10)
    >>> push(20)
    >>> push(5)
    >>> push(30)
    >>> push(1)
    >>> get_min()
    1
    >>> pop()
    >>> get_min()
    5
    >>> pop()
    >>> get_min()
    10
    """
    return min_stack.pop()


if __name__ == "__main__":
    from doctest import testmod

    testmod()
