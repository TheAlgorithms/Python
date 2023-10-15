def decode_string(encoded_string: str) -> str:
    """
    Decode an encoded string using the specified rules.

    This function takes an encoded string and decodes it based on the following rules:
    - The input string consists of digits, lowercase English letters, '[', and ']'.
    - The encoded string is repeated inside square brackets ('[]').

    Args:
        encoded_string (str): The encoded string to be decoded.

    Returns:
        str: The decoded string.

    Examples:
        >>> decode_string("3[a]2[bc]")
        'aaabcbc'

        >>> decode_string("3[a2[c]]")
        'accaccacc'

        >>> decode_string("2[abc]3[cd]ef")
        'abcabccdcdcdef'
    """
    stack = []

    for char in encoded_string:
        if char != "]":
            stack.append(char)
        else:
            substring = ""
            while stack[-1] != "[":
                substring = stack.pop() + substring
            stack.pop()

            count = ""
            while stack and stack[-1].isdigit():
                count = stack.pop() + count

            stack.append(int(count) * substring)

    return "".join(stack)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
