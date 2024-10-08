from string import ascii_uppercase


def miznitskiy(text: str, key: str) -> str:
    """
    Encrypt plaintext with the Miznitskiy cipher
    >>> miznitskiy('hello', 'KEY')
    'XQKKZ'
    >>> miznitskiy('hello', 'ABCD')
    'HFMMP'
    >>> miznitskiy('', 'KEY')
    ''
    >>> miznitskiy('yes, ¥€$ - _!@#%?', 'KEY')
    'YFV, ¥€$ - _!@#%?'
    >>> miznitskiy('yes, ¥€$ - _!@#%?', 'K')
    'YDV, ¥€$ - _!@#%?'
    >>> miznitskiy('yes, ¥€$ - _!@#%?', 'KEYWORD')
    'YHV, ¥€$ - _!@#%?'
    >>> miznitskiy('yes, ¥€$ - _!@#%?', '')
    Traceback (most recent call last):
      ...
    ZeroDivisionError: integer modulo by zero
    """
    ascii_len = len(ascii_uppercase)
    key_len = len(key)
    encrypted_text = ""
    keys = [ord(char) - ord("A") for char in key.upper()]

    if key_len == 0:
        raise ZeroDivisionError("integer modulo by zero")

    upper_case_text = text.upper()

    for i, char in enumerate(upper_case_text):
        if char in ascii_uppercase:
            shift_amount = keys[i % key_len]
            new_position = (ascii_uppercase.index(char) + shift_amount) % ascii_len
            shifted_letter = ascii_uppercase[new_position]
            encrypted_text += shifted_letter
        else:
            encrypted_text += char

    return encrypted_text


if __name__ == "__main__":
    from doctest import testmod

    testmod()
