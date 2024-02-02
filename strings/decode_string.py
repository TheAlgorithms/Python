"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string
inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces,
square brackets are well-formed, etc. Furthermore, you may assume that the original
data does not contain any digits and that digits are only for those repeat numbers, k.
For example, there will not be input like 3a or 2[4].

Reference: https://leetcode.com/problems/decode-string

Implementation notes:
The string in the inner brackets has to be processed first and
used as input for processing the outer brackets.
This suggests the use of a stack data structure.
An alternative approach would be to use the call stack by
implementing a recursive approach.
When we encounter an '[', we recursively process its inner contents.
"""


def decode_string_helper(input_string: str, index: int) -> tuple[str, int]:
    """
    This function returns a tuple of the decoded string and
    the last index of character processed.

    Args:
        input_string: The string to be decoded
        index: The starting index of the characters to process

    Returns:
        A tuple of result processed and the last index of character processed

    >>> decode_string_helper("3[a]2[bc]", 0)
    ('aaabcbc', 9)

    >>> decode_string_helper("2[abc]3[cd]ef", 6)
    ('cdcdcdef', 13)
    """
    result = ""
    num = 0

    while index < len(input_string):
        if input_string[index] == "[":
            decoded_string, new_index = decode_string_helper(input_string, index + 1)
            result = result + num * decoded_string
            num = 0
            index = new_index
        elif input_string[index] == "]":
            return (result, index)
        elif input_string[index].isdigit():
            num = num * 10 + int(input_string[index])
        else:  # s[i] is a letter
            result += input_string[index]
        index += 1

    return result, index


def decode_string(input_string: str) -> str:
    """
    This function returns the decoded string

    Args:
        input_string: The string to be decoded

    Returns:
        returns The decoded string
    >>> decode_string("3[a]2[bc]")
    'aaabcbc'

    >>> decode_string("3[a2[c]]")
    'accaccacc'

    >>> decode_string("2[abc]3[cd]ef")
    'abcabccdcdcdef'
    """
    decoded_string, _ = decode_string_helper(input_string, 0)
    return decoded_string


if __name__ == "__main__":
    import doctest

    doctest.testmod()
