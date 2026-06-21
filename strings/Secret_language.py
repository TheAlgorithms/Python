# Encoding & Decoding

import random
import string


def random_chars() -> str:
    """
    Adds random 3 charaters to the string.

    """
    return "".join(random.choices(string.ascii_letters, k=3))


def random_digits() -> str:
    """
    Adds 3 random digits to the string.
    """

    return "".join(random.choices(string.digits, k=3))


<<<<<<< HEAD
def encode(code: str) -> str:
    '''
=======
def encode(code) -> str:
    """
>>>>>>> cb237ed2095a60e62d73afd8b17c1207cc1fb4f9
    Encodes the code by shifting the first character to the end of the original string,
    and adding the 3 random_characters + 3 random-digits + original string(code) +  3 random-digits + 3 random_characters.
    unless the length of the code exceeds 3 or equals to it."""

    if len(code) >= 3:
        code = code[1:] + code[0]
        code = (
            random_chars() + random_digits() + code + random_digits() + random_chars()
        )
    else:
        code = code[::-1]
        code = (
            random_chars() + random_digits() + code + random_digits() + random_chars()
        )
    return code

<<<<<<< HEAD
def decode(code: str) -> str:
    '''
=======

def decode(code) -> str:
    """
>>>>>>> cb237ed2095a60e62d73afd8b17c1207cc1fb4f9
    decodes the encoded string by removing the randomly added characters and reversing the shift

    """

    code = code[6:-6]
    if len(code) >= 3:
        code = code[-1] + code[:-1]
    else:
        code = code[::-1]
    return code


if __name__ == "__main__":
    code = input("Enter the code: ")
    encoded = encode(code)
    decoded = decode(encoded)
    print(f"Original → {code}")
    print(f"Encoded  → {encoded}")
    print(f"Decoded  → {decoded}")
