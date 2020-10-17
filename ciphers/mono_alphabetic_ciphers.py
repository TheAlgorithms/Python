LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def translate_message(key, message, mode):
    """
    >>> translate_message(
            "QWERTYUIOPASDFGHJKLZXCVBNM", 
            "When you do the common things in life in an uncommon way, "
            "you will command the attention of the world", "encrypt")
    'Vitf ngx rg zit egddgf zioful of soyt of qf xfegddgf vqn, ngx voss egddqfr zit qzztfzogf gy zit vgksr'
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
    >>> encrypt_message("QWERTYUIOPASDFGHJKLZXCVBNM", "When you do the common things in life in an uncommon way, you will command the attention of the world")
    'Vitf ngx rg zit egddgf zioful of soyt of qf xfegddgf vqn, ngx voss egddqfr zit qzztfzogf gy zit vgksr'
    """
    return translate_message(key, message, "encrypt")


def decrypt_message(key, message):
    """
    >>> decrypt_message("QWERTYUIOPASDFGHJKLZXCVBNM", "When you do the common things in life in an uncommon way, you will command the attention of the world")
    'Bpcy fig mi epc vizziy ephyol hy shnc hy ky gyvizziy bkf, fig bhss vizzkym epc keecyehiy in epc bidsm'
    """
    return translate_message(key, message, "decrypt")


def main():
    myMessage = (
        "When you do the common things in life in an uncommon way, "
        "you will command the attention of the world"
    )
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
