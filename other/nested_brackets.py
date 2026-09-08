"""
The nested brackets problem is a problem that determines if a sequence of
brackets are properly nested.  A sequence of brackets s is considered properly nested
if any of the following conditions are true:

    - s is empty
    - s has the form (U) or [U] or {U} where U is a properly nested string
    - s has the form VW where V and W are properly nested strings

For example, the string "()()[()]" is properly nested but "[(()]" is not.

The function called is_balanced takes as input a string S which is a sequence of
brackets and returns true if S is nested and false otherwise.
"""


def is_balanced(s: str) -> bool:
    """
    >>> is_balanced("")
    True
    >>> is_balanced("()")
    True
    >>> is_balanced("[]")
    True
    >>> is_balanced("{}")
    True
    >>> is_balanced("()[]{}")
    True
    >>> is_balanced("(())")
    True
    >>> is_balanced("[[")
    False
    >>> is_balanced("([{}])")
    True
    >>> is_balanced("(()[)]")
    False
    >>> is_balanced("([)]")
    False
    >>> is_balanced("[[()]]")
    True
    >>> is_balanced("(()(()))")
    True
    >>> is_balanced("]")
    False
    >>> is_balanced("Life is a bowl of cherries.")
    True
    >>> is_balanced("Life is a bowl of che{}ies.")
    True
    >>> is_balanced("Life is a bowl of che}{ies.")
    False
    """
    open_to_closed = {"{": "}", "[": "]", "(": ")"}
    stack = []
    for symbol in s:
        if symbol in open_to_closed:
            stack.append(symbol)
        elif symbol in open_to_closed.values() and (
            not stack or open_to_closed[stack.pop()] != symbol
        ):
            return False
    return not stack  # stack should be empty


def main():
    s = input("Enter sequence of brackets: ")
    print(f"'{s}' is {'' if is_balanced(s) else 'not '}balanced.")


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    main()
