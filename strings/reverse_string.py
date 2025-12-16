"""
Algorithm: Reverse String
Author: muannn
Description:
    This module implements a simple function to reverse an input string.
    It is part of the TheAlgorithms/Python open-source collection.

    The algorithm takes a string `s` as input and returns the reversed version.
    It also handles edge cases such as empty strings and single-character inputs.

Example:
    >>> reverse_string("Hello")
    'olleH'

    >>> reverse_string("OpenAI")
    'IAnepO'
"""


def reverse_string(s: str) -> str:
    """
    Reverse the given string.

    Args:
        s (str): The string to be reversed.

    Returns:
        str: A new string that is the reverse of `s`.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")

    # Core logic: Python slicing technique to reverse string
    return s[::-1]


if __name__ == "__main__":
    # Simple test cases for demonstration
    print(reverse_string("Python"))  # Expected: 'nohtyP'
    print(reverse_string("OpenAI"))  # Expected: 'IAnepO'
    print(reverse_string(""))  # Expected: ''
    print(reverse_string("A"))  # Expected: 'A'
