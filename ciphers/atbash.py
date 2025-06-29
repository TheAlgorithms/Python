"""https://en.wikipedia.org/wiki/Atbash"""

import string


def atbash(text: str) -> str:
    """
    Encodes or decodes text using the Atbash cipher.

    The Atbash cipher substitutes each letter with its mirror in the alphabet:
    A -> Z, B -> Y, C -> X, ... Z -> A (case is preserved)
    Non-alphabetic characters are left unchanged.

    Args:
        text: The input string to encode/decode

    Returns:
        The transformed string
    """
    # Create translation tables for uppercase and lowercase
    lowercase_map = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1])
    uppercase_map = str.maketrans(string.ascii_uppercase, string.ascii_uppercase[::-1])

    # Apply both translation mappings
    return text.translate(lowercase_map).translate(uppercase_map)


# Example usage
if __name__ == "__main__":
    test_string = "Hello, World! 123"
    encoded = atbash(test_string)
    decoded = atbash(encoded)

    print(f"Original:  {test_string}")
    print(f"Encoded:   {encoded}")
    print(f"Decoded:   {decoded}")
