def is_valid(next_string: str) -> bool:
    """
    Helper function to check if a string has valid parentheses.

    Params:
        next_string (str): The input string to be checked.

    Returns:
        bool: True if the parentheses in the string are valid, False otherwise.

    Examples:
    >>> is_valid("(a)())")
    False

    >>> is_valid("(a())")
    True

    >>> is_valid(")(a)()")
    False

    """
    count: int = 0
    for char in next_string:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
            if count < 0:
                return False
    return count == 0


def depth_first_search(
    current_string: str, left_removed: int, right_removed: int
) -> list[str]:
    """
    Depth-first search function to generate valid combinations
    of the input string.

    Params:
        current_string (str): The current string being processed.
        left_removed (int): The number of left parentheses to be removed.
        right_removed (int): The number of right parentheses to be removed.

    Returns:
        list[str]: A list of valid strings after removing the
        minimum number of parentheses.
    Example:
    >>> depth_first_search("()())()", 0, 1)
    ['(())()', '()()()']

    >>> depth_first_search("()())(", 0, 0)
    []

    >>> depth_first_search(")(a)())", 0, 2)
    ['(a())', '(a)()']
    """
    valid_parentheses: set = set()
    stack = [(current_string, left_removed, right_removed, 0)]
    while stack:
        current_str, left, right, index = stack.pop()
        if left < 0 or right < 0:
            continue
        if left == 0 and right == 0 and is_valid(current_str):
            valid_parentheses.add(current_str)
            continue
        if index >= len(current_str):
            continue
        if current_str[index] == "(":
            stack.append(
                (current_str[:index] + current_str[index + 1 :], left - 1, right, index)
            )
            stack.append((current_str, left, right, index + 1))
        elif current_str[index] == ")":
            stack.append(
                (current_str[:index] + current_str[index + 1 :], left, right - 1, index)
            )
            stack.append((current_str, left, right, index + 1))
        else:
            stack.append((current_str, left, right, index + 1))
    parentheses: list = list(valid_parentheses)
    parentheses.sort()
    return parentheses


def remove_invalid_parentheses(input_string: str) -> list[str]:
    """
    Removes the minimum number of invalid parentheses
    to make the input string valid.

    Args:
        input_string (str): The input string containing parentheses.

    Returns:
        List[str]: A list of valid strings after removing
        the minimum number of parentheses.
    Examples:
    >>> remove_invalid_parentheses(")(a)())")
    ['(a())', '(a)()']

    >>> remove_invalid_parentheses("()())()")
    ['(())()', '()()()']

    >>> remove_invalid_parentheses(")(")
    ['']
    """
    left_removed_count: int = 0
    right_removed_count: int = 0
    for char in input_string:
        if char == "(":
            left_removed_count += 1
        elif char == ")":
            if left_removed_count > 0:
                left_removed_count -= 1
            else:
                right_removed_count += 1
    valid_combinations: list[str] = depth_first_search(
        input_string, left_removed_count, right_removed_count
    )
    return valid_combinations


if __name__ == "__main__":
    import doctest

    doctest.testmod()
