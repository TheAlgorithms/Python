def valid_parentheses(input_str: str) -> bool:
    """
    Return True if string contains valid parentheses otherwise False.
    >>> valid_parentheses("()[]{}")
    True
    >>> valid_parentheses("{[()]}")
    True
    >>> valid_parentheses("([)]")
    False
    """
    while True:
        stack = []
        open_list = ["[", "{", "("]
        close_list = ["]", "}", ")"]
        valid_pairs = {"]": "[", "}": "{", ")": "("}
        for i in input_str:
            if i in open_list:
                stack.append(i)
            if i in close_list:
                if not stack:
                    return False
                elif stack.pop() != valid_pairs[i]:
                    return False
                else:
                    continue
        return not stack


if __name__ == "__main__":
    import doctest

    doctest.testmod()
