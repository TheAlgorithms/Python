def valid_parentheses(word: str) -> str:
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

    # Converting to ascii value int value and checking to see if char is a lower letter
    # if it is a lowercase letter it is getting shift by 32 which makes it an uppercase
    # case letter
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
