def valid_parentheses(word: str) -> bool:
    """
    Will determine if the input string contains valid parentheses pair.

    >>> valid_parentheses("()")
    true
    >>> valid_parentheses("()[]{}")
    true
    >>> valid_parentheses("(]")
    false
    >>> valid_parentheses("([)]")
    false
    >>> valid_parentheses("{[]}")
    true
    """

    # Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    # determine if the input string is valid.
    # An input string is valid if:
    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.

    stack = []
    for i in word:
        if i in ("[", "{", "("):
            stack.insert(0, i)
        elif len(stack) == 0:
            return False
        elif stack[0] == "[" and i == "]" or stack[0] == "(" and i == ")" or stack[0] == "{" and i == "}":
            stack.pop(0)
        else:
            return False
    return len(stack) == 0

if __name__ == "__main__":
    from doctest import testmod

    testmod()
