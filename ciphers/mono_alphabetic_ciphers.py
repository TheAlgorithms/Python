LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    myMessage = "When you do the common things in life in an uncommon way, you will command the attention of the world"
    myKey = "QWERTYUIOPASDFGHJKLZXCVBNM"
    myMode = "decrypt"  # set to 'encrypt' or 'decrypt'

    checkValidKey(myKey)

    if myMode == "encrypt":
        translated = encryptMessage(myKey, myMessage)
    elif myMode == "decrypt":
        translated = decryptMessage(myKey, myMessage)
    print("Using key %s" % (myKey))
    print("The %sed message is:" % (myMode))
    print(translated)


def checkValidKey(key: str):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit("There is an error in the key or symbol set.")


def encryptMessage(key: str, message: str) -> str:
    """
    >>> encryptMessage("QWERTYUIOPASDFGHJKLZXCVBNM", "When you do the common things in life in an uncommon way, you will command the attention of the world")
    'Vitf ngx rg zit egddgf zioful of soyt of qf xfegddgf vqn, ngx voss egddqfr zit qzztfzogf gy zit vgksr'
    """
    return translateMessage(key, message, "encrypt")


def decryptMessage(key, message):
    """
    >>> decryptMessage("QWERTYUIOPASDFGHJKLZXCVBNM", "When you do the common things in life in an uncommon way, you will command the attention of the world")
    'Bpcy fig mi epc vizziy ephyol hy shnc hy ky gyvizziy bkf, fig bhss vizzkym epc keecyehiy in epc bidsm'
    """
    return translateMessage(key, message, "decrypt")


def translateMessage(key, message, mode):
    """
    >>> translateMessage("QWERTYUIOPASDFGHJKLZXCVBNM", "When you do the common things in life in an uncommon way, you will command the attention of the world", "encrypt")
    'Vitf ngx rg zit egddgf zioful of soyt of qf xfegddgf vqn, ngx voss egddqfr zit qzztfzogf gy zit vgksr'
    """
    translated = ""
    charsA = LETTERS
    charsB = key
    if mode == "decrypt":
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA
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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
