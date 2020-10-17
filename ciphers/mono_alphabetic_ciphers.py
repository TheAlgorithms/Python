LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def translate_message(key, message, mode):
    """
    >>> translate_message("QWERTYUIOPASDFGHJKLZXCVBNM","Hello World","encrypt")
    'Pcssi Bidsm'
    """
    charsA = LETTERS if mode == "decrypt" else key
    charsB = key if mode == "decrypt" else LETTERS
    translated = ""
    # loop through each symbol in the message
    for symbol in message:
        if symbol.upper() in charsA:
            # encrypt/decrypt the symbol
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol
    return translated


def encrypt_message(key: str, message: str) -> str:
    """
    >>> encrypt_message("QWERTYUIOPASDFGHJKLZXCVBNM", "Hello World")
    'Pcssi Bidsm'
    """
    return translate_message(key, message, "encrypt")


def decrypt_message(key: str, message: str) -> str:
    """
    >>> decrypt_message("QWERTYUIOPASDFGHJKLZXCVBNM", "Hello World")
    'Itssg Vgksr'
    """
    return translate_message(key, message, "decrypt")


def main():
    myMessage = "Hello World"
    myKey = "QWERTYUIOPASDFGHJKLZXCVBNM"
    myMode = "decrypt"  # set to 'encrypt' or 'decrypt'

    if myMode == "encrypt":
        translated = encrypt_message(myKey, myMessage)
    elif myMode == "decrypt":
        translated = decrypt_message(myKey, myMessage)
    print("Using key %s" % (myKey))
    print("The %sed message is:" % (myMode))
    print(translated)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
