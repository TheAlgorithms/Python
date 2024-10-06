"""
Python implementation of the Gronsfeld cipher encryption

The Gronsfeld cipher is similar to the Vigenere cipher,
with the exception that the key is numeric.

https://www.dcode.fr/gronsfeld-cipher
"""


def gronsfeld(text: str, key: str) -> str:
    """
    Encrypt plaintext with the Gronsfeld cipher

    >>> gronsfeld('hello', '412')
    'LFNPP'
    >>> gronsfeld('', '123')
    ''
    """
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keys = [int(i) for i in key]
    encrypted_text = ""
    upper_case_text = text.upper()

    for i, char in enumerate(upper_case_text):
        if char in alphabets:
            new_position = (alphabets.index(char) + keys[i % len(keys)]) % len(
                alphabets
            )
            shifted_letter = alphabets[new_position]
            encrypted_text += shifted_letter
        else:
            encrypted_text += char

    return encrypted_text


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    encrypted = gronsfeld("hello world", "123")
    print(f"Encrypted text is {encrypted}")
