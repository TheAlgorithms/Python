def main():
    """
    Handles I/O
    :return: void
    """
    message = input("Enter message to encode or decode: ").strip().upper()
    key = input("Enter keyword: ").strip().upper()
    option = input("Encipher or decipher? E/D:").strip()[0].lower()
    try:
        func = {"e": encipher, "d": decipher}[option]
    except KeyError:
        raise KeyError("invalid input option")
    cipher_map = create_cipher_map(key)
    print(func(message, cipher_map))


def create_cipher_map(key: str) -> dict:
    """
    Returns a cipher map given a keyword.
    :param key: keyword to use
    :return: dictionary cipher map
    """
    cipher_alphabet = {}
    # Create alphabet list
    alphabet = [chr(i + 65) for i in range(26)]
    # Remove duplicate characters from key
    key = remove_duplicates(key)
    offset = len(key)
    # First fill cipher with key characters
    for i, char in enumerate(key):
        cipher_alphabet[alphabet[i]] = char
    # Then map remaining characters in alphabet to
    # the alphabet from the beginning
    for i in range(len(cipher_alphabet.keys()), 26):
        char = alphabet[i - offset]
        # Ensure we are not mapping letters to letters previously mapped
        while char in key:
            offset -= 1
            char = alphabet[i - offset]
        cipher_alphabet[alphabet[i]] = char
    return cipher_alphabet


def remove_duplicates(key: str) -> str:
    """
    Removes duplicate alphabetic characters in a keyword (removed after first appearance).
    :param key: Keyword to use
    :return: String with duplicates removed
    >>> remove_duplicates('Hello World!!')
    'Helo Wrd'
    """

    key_no_dups = ""
    for ch in key:
        if (ch not in key_no_dups and ch.isalpha()) or ch == " ":
            key_no_dups += ch
    return key_no_dups


def encipher(message: str, cipher_map: dict) -> str:
    """
    Enciphers a message given a cipher map.
    :param message: Message to encipher
    :param cipher_map: Cipher map
    :return: enciphered string
    >>> encipher('HELLO WORLD!!', create_cipher_map('GOODBYE!!'))
    'CYJJM VMQJB!!'
    """
    enciphered_message = ""
    for ch in message:
        enciphered_message += cipher_map.get(ch, ch)
    return enciphered_message


def decipher(message: str, cipher_map: dict) -> str:
    """
    Deciphers a message given a cipher map
    :param message: Message to decipher
    :param cipher_map: Dictionary mapping to use
    :return: Deciphered string
    >>> decipher(encipher('HELLO WORLD!!', create_cipher_map('GOODBYE!!')), create_cipher_map('GOODBYE!!'))
    'HELLO WORLD!!'
    """
    # Reverse our cipher mappings
    rev_cipher_map = {v: k for k, v in cipher_map.items()}
    deciphered_message = ""
    for ch in message:
        deciphered_message += rev_cipher_map.get(ch, ch)
    return deciphered_message


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
