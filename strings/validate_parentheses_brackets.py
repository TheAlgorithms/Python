def valid_parentheses_brackets(input_string: str) -> bool:
    """
    Determine whether the brackets, braces, and parentheses in a string are valid.
    Works only on strings containing only brackets, braces, and parentheses.

    :param input_string:
    :return: Boolean

    >>> valid_parentheses_brackets('()')
    True
    >>> valid_parentheses_brackets('()[]{}')
    True
    >>> valid_parentheses_brackets('{[()]}')
    True
    >>> valid_parentheses_brackets('(})')
    False

    Time complexity: O(n) where n is the length of the input string.
    Space complexity: O(n) where n is the length of the input string.
    """
    open_stack: list = []
    map_close_to_open: dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for character in input_string:
        if character in map_close_to_open:
            if open_stack and open_stack.pop() == map_close_to_open[character]:
                pass
            else:
                return False
        else:
            open_stack.append(character)
    
    return False if open_stack else True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
