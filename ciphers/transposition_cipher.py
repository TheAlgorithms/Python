import math

"""
In cryptography, the TRANSPOSITION cipher is a method of encryption where the
positions of plaintext are shifted a certain number(determined by the key) that
follows a regular system that results in the permuted text, known as the encrypted
text. The type of transposition cipher demonstrated under is the ROUTE cipher.
"""


def main():
    message = input("Enter message: ")
    key = int(input("Enter key [2-%s]: " % (len(message) - 1)))
    mode = input("Encryption/Decryption [e/d]: ")

    if mode.lower().startswith("e"):
        text = encryptMessage(key, message)
    elif mode.lower().startswith("d"):
        text = decryptMessage(key, message)

    # Append pipe symbol (vertical bar) to identify spaces at the end.
    print("Output:\n%s" % (text + "|"))


def encryptMessage(key: int, message: str) -> str:
    """
    >>> encryptMessage(6, 'Harshil Darji')
    'Hlia rDsahrij'
    """
    cipherText = [""] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipherText[col] += message[pointer]
            pointer += key
    return "".join(cipherText)


def decryptMessage(key: int, message: str) -> str:
    """
    >>> decryptMessage(6, 'Hlia rDsahrij')
    'Harshil Darji'
    """
    numCols = math.ceil(len(message) / key)
    numRows = key
    numShadedBoxes = (numCols * numRows) - len(message)
    plainText = [""] * numCols
    col = 0
    row = 0

    for symbol in message:
        plainText[col] += symbol
        col += 1

        if (
            (col == numCols)
            or (col == numCols - 1)
            and (row >= numRows - numShadedBoxes)
        ):
            col = 0
            row += 1

    return "".join(plainText)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
