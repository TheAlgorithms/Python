import sys


def main():
    """
    Handles I/O
    :return: void
    """
    print("Enter message to encode or decode:", end=" ")
    message = sys.stdin.readline().strip()
    print("Enter keyword:", end=" ")
    key = sys.stdin.readline().strip()
    print("Encipher or decipher? E/D:", end=" ")
    option = sys.stdin.readline().strip()
    key = key.upper()
    message = message.upper().strip()
    cipher_map = create_cipher_map(key)
    if option.lower().startswith("e"):
        enciphered_message = encipher(message, cipher_map)
        print(enciphered_message)
    elif option.lower().startswith("d"):
        deciphered_message = decipher(message, cipher_map)
        print(deciphered_message)
    else:
        print("Invalid input option")


def create_cipher_map(key: str) -> dict:
    """
    Returns a cipher map given a keyword.
    :param key: keyword to use
    :return: dictionary cipher map
    """
    alphabet = []
    cipher_alphabet = {}
    # Create alphabet list
    for i in range(26):
        alphabet.append(chr(i + 65))
    # Remove duplicate characters from key
    key = remove_duplicates(key)
    offset = len(key)
    # First fill cipher with key characters
    for i in range(len(key)):
        cipher_alphabet[alphabet[i]] = key[i]
    # Then map remaining characters in alphabet to
    # the alphabet from the beginning
    for i in range(len(cipher_alphabet.keys()), 26):
        char = alphabet[i - offset]
        # Ensure we are not mapping letters to letters previously mapped
        while key.find(char) != -1:
            offset -= 1
            char = alphabet[i - offset]
        cipher_alphabet[alphabet[i]] = char
    return cipher_alphabet


def remove_duplicates(key: str) -> str:
    """
    Removes duplicate characters in a keyword (removed after first appearance).
    :param key: Keyword to use
    :return: String with duplicates removed
    """
    """
    >>> remove_duplicates('hellol')
    'helo'
    """

    key_no_dups = ""
    for ch in key:
        if key_no_dups.find(ch) == -1:
            key_no_dups += ch
    return key_no_dups


def encipher(message: str, cipher_map: dict) -> str:
    """
    Enciphers a message given a cipher map.
    :param message: Message to encipher
    :param cipher_map: Cipher map
    :return:
    """
    enciphered_message = ""
    for ch in message:
        if ch.isalpha():
            enciphered_message += cipher_map[ch.upper()]
        else:
            enciphered_message += ch
    return enciphered_message


def decipher(message: str, cipher_map: dict) -> str:
    """
    Deciphers a message given a cipher map
    :param message: Message to decipher
    :param cipher_map: Dictionary mapping to use
    :return: Deciphered string
    """
    # Reverse our cipher mappings
    rev_cipher_map = dict((v, k) for k, v in cipher_map.items())
    deciphered_message = ""
    for ch in message:
        if ch.isalpha():
            deciphered_message += rev_cipher_map[ch.upper()]
        else:
            deciphered_message += ch
    return deciphered_message


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
