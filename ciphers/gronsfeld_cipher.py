"""
Python implementation of the Gronsfeld cipher encryption

The Gronsfeld cipher is similar to the Vigenere cipher,
with the exception that the key is numeric.

https://www.dcode.fr/gronsfeld-cipher
"""

from string import ascii_uppercase


def gronsfeld(text: str, key: str) -> str:
    """
    Encrypt plaintext with the Gronsfeld cipher

    >>> gronsfeld('hello', '412')
    'LFNPP'
    >>> gronsfeld('', '123')
    ''
    """
    ascii_len = len(ascii_uppercase)
    key_len = len(key)
    encrypted_text = ""
    keys = [int(char) for char in key]
    upper_case_text = text.upper()

    for i, char in enumerate(upper_case_text):
        if char in alphabets:
            new_position = (ascii_uppercase.index(char) + keys[i % key_len]) % ascii_len
            shifted_letter = ascii_uppercase[new_position]
            encrypted_text += shifted_letter
        else:
            encrypted_text += char

    return encrypted_text


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    encrypted = gronsfeld("hello world", "123")
    print(f"Encrypted text is {encrypted}")
