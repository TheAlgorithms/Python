# Encoding & Decoding

import random
import string


def random_chars() -> str:
    """
    Generate a random string of 3 ASCII letters.

    >>> import random
    >>> len(random_chars()) == 3
    True
    >>> all(c in string.ascii_letters for c in random_chars())
    True
    """
    return ''.join(random.choices(string.ascii_letters, k=3))


def random_digits() -> str:
    """
    Generate a random string of 3 digits.

    >>> len(random_digits()) == 3
    True
    >>> all(c in string.digits for c in random_digits())
    True
    """
    return ''.join(random.choices(string.digits, k=3))


def encode(code: str) -> str:
    """
    Encode a string by shifting the first character to the end and
    wrapping it with random padding of 3 letters and 3 digits on each side.

    Reference: https://en.wikipedia.org/wiki/Caesar_cipher

    >>> len(encode('hello')) == len('hello') + 12
    True
    >>> len(encode('hi')) == len('hi') + 12
    True
    """
    if len(code) >= 3:
        code = code[1:] + code[0]
        code = random_chars() + random_digits() + code + random_digits() + random_chars()
    else:
        code = code[::-1]
        code = random_chars() + random_digits() + code + random_digits() + random_chars()
    return code


def decode(code: str) -> str:
    """
    Decode an encoded string by stripping the random padding and
    reversing the character shift.

    >>> decode(encode('hello'))
    'hello'
    >>> decode(encode('hi'))
    'hi'
    >>> decode(encode('python'))
    'python'
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