def generate_parentheses_iterative(length: int) -> list:
    """
    Generate all valid combinations of parentheses (Iterative Approach).

    The algorithm works as follows:
    1. Initialize an empty list to store the combinations.
    2. Initialize a stack to keep track of partial combinations.
    3. Start with empty string and push it onstack along with the counts of '(' and ')'.
    4. While the stack is not empty:
        a. Pop a partial combination and its open and close counts from the stack.
        b. If the combination length is equal to 2*length, add it to the result.
        c. If open count < length, push new combination with added '(' on stack.
        d. If close count < open count, push new combination with added ')' on stack.
    5. Return the result containing all valid combinations.

    Args:
        length: The desired length of the parentheses combinations

    Returns:
        A list of strings representing valid combinations of parentheses

    Time Complexity:
        O(2^(2*length))

    Space Complexity:
        O(2^(2*length))

    >>> generate_parentheses_iterative(3)
    ['()()()', '()(())', '(())()', '(()())', '((()))']
    >>> generate_parentheses_iterative(2)
    ['()()', '(())']
    >>> generate_parentheses_iterative(1)
    ['()']
    >>> generate_parentheses_iterative(0)
    ['']
    """
    result = []
    stack = []

    # Each element in stack is a tuple (current_combination, open_count, close_count)
    stack.append(("", 0, 0))

    while stack:
        current_combination, open_count, close_count = stack.pop()

        if len(current_combination) == 2 * length:
            result.append(current_combination)

        if open_count < length:
            stack.append((current_combination + "(", open_count + 1, close_count))

        if close_count < open_count:
            stack.append((current_combination + ")", open_count, close_count + 1))

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(generate_parentheses_iterative(3))
