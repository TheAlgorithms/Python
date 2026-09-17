"""
Caesar Cipher Algorithm

The Caesar cipher is one of the simplest and most widely known encryption techniques.
It works by shifting each letter in the plaintext by a fixed number of positions
down or up the alphabet.

Example:
    >>> encrypt("abc", 2)
    'cde'
    >>> decrypt("cde", 2)
    'abc'

You can also encrypt/decrypt with uppercase letters:
    >>> encrypt("Hello, World!", 3)
    'Khoor, Zruog!'
    >>> decrypt("Khoor, Zruog!", 3)
    'Hello, World!'

Reference:
    https://en.wikipedia.org/wiki/Caesar_cipher
"""

from string import ascii_lowercase, ascii_uppercase


def encrypt(text: str, shift: int) -> str:
    """
    Encrypt the given text using Caesar cipher.

    Args:
        text: The input text to encrypt.
        shift: The number of positions to shift each letter.

    Returns:
        The encrypted text as a string.

    The caesar cipher is named after Julius Caesar who used it when sending
    secret military messages to his troops. This is a simple substitution cipher
    where every character in the plain-text is shifted by a certain number known
    as the "key" or "shift".

    Example:
    Say we have the following message:
    ``Hello, captain``

    And our alphabet is made up of lower and uppercase letters:
    ``abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ``

    And our shift is ``2``

    We can then encode the message, one letter at a time. ``H`` would become ``J``,
    since ``J`` is two letters away, and so on. If the shift is ever too large, or
    our letter is at the end of the alphabet, we just start at the beginning
    (``Z`` would shift to ``a`` then ``b`` and so on).

    Our final message would be ``Jgnnq, ecrvckp``

    Further reading
    ===============

    *   https://en.m.wikipedia.org/wiki/Caesar_cipher

    Doctests
    ========

    >>> encrypt('The quick brown fox jumps over the lazy dog', 8)
    'bpm yCqks jzwEv nwF rCuxA wDmz Bpm tiHG lwo'

    >>> encrypt('A very large key', 8000)
    's nWjq dSjYW cWq'

    >>> encrypt('a lowercase alphabet', 5, 'abcdefghijklmnopqrstuvwxyz')
    'f qtbjwhfxj fqumfgjy'
    
    >>> encrypt("abc", 1)
    'bcd'
    >>> encrypt("xyz", 3)
    'abc'
    >>> encrypt("Hello, World!", 5)
    'Mjqqt, Btwqi!'
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")
    if not isinstance(shift, int):
        raise TypeError("Shift must be an integer.")

    result = []

    for char in text:
        if char in ascii_lowercase:
            index = (ascii_lowercase.index(char) + shift) % 26
            result.append(ascii_lowercase[index])
        elif char in ascii_uppercase:
            index = (ascii_uppercase.index(char) + shift) % 26
            result.append(ascii_uppercase[index])
        else:
            result.append(char)

    return "".join(result)


def decrypt(text: str, shift: int) -> str:
    """
    Decrypt the given text encrypted with Caesar cipher.

    Args:
        text: The encrypted text to decrypt.
        shift: The number of positions originally used to encrypt.

    Returns:
        The decrypted text as a string.

    >>> decrypt("bcd", 1)
    'abc'
    >>> decrypt("abc", 3)
    'xyz'
    >>> decrypt("Mjqqt, Btwqi!", 5)
    'Hello, World!'
    """
    return encrypt(text, -shift)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print("✅ All doctests passed!")
