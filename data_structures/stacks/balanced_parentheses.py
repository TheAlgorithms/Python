from .stack import Stack


def balanced_parentheses(parentheses: str) -> bool:
    """ Use a stack to check if a string of parentheses is balanced.
    >>> balanced_parentheses("([]{})")
    True
    >>> balanced_parentheses("[()]{}{[()()]()}")
    True
    >>> balanced_parentheses("[(])")
    False
    >>>
    """
    stack = Stack()
    for bracket in parentheses:
        if bracket in ("(", "[", "{"):
            stack.push(bracket)
        elif bracket in (")", "]", "}"):
            if stack.is_empty() or not is_paired(stack.pop(), bracket):
                return False
    return stack.is_empty()


def is_paired(left_bracket: str, right_bracket: str) -> bool:
    """
    >>> brackets = {"(" : ")", "[" : "]", "{" : "}"}
    >>> for left_bracket, right_bracket in brackets.items():
    ...     assert is_paired(left_bracket, right_bracket)
    >>> is_paired("(", "}")
    False
    >>> is_paired("(", "]")
    False
    """
    return (
            left_bracket == "(" and right_bracket == ")" or
            left_bracket == "[" and right_bracket == "]" or
            left_bracket == "{" and right_bracket == "}"
    )


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    
    examples = ["((()))", "((())", "(()))"]
    print("Balanced parentheses demonstration:\n")
    for example in examples:
        print(
            example, "is",
            "balanced" if balanced_parentheses(example)
            else "not balanced"
        )
