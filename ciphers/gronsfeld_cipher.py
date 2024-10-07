from string import ascii_uppercase


def gronsfeld(text: str, key: str) -> str:
    """
    Encrypt plaintext with the Gronsfeld cipher

    >>> gronsfeld('hello', '412')
    'LFNPP'
    >>> gronsfeld('hello', '123')
    'IGOMQ'
    >>> gronsfeld('', '123')
    ''
    >>> gronsfeld('yes, ¥€$ - _!@#%?', '0')
    'YES, ¥€$ - _!@#%?'
    >>> gronsfeld('yes, ¥€$ - _!@#%?', '01')
    'YFS, ¥€$ - _!@#%?'
    >>> gronsfeld('yes, ¥€$ - _!@#%?', '012')
    'YFU, ¥€$ - _!@#%?'
    >>> gronsfeld('yes, ¥€$ - _!@#%?', '')
    Traceback (most recent call last):
      ...
    ZeroDivisionError: integer modulo by zero
    """
    ascii_len = len(ascii_uppercase)
    key_len = len(key)
    encrypted_text = ""
    keys = [int(char) for char in key]
    upper_case_text = text.upper()

    for i, char in enumerate(upper_case_text):
        if char in ascii_uppercase:
            new_position = (ascii_uppercase.index(char) + keys[i % key_len]) % ascii_len
            shifted_letter = ascii_uppercase[new_position]
            encrypted_text += shifted_letter
        else:
            encrypted_text += char

    return encrypted_text


if __name__ == "__main__":
    from doctest import testmod

    testmod()
