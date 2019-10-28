import math

def decryptMessage(key, message):

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

def brute_force_transposition_cipher(c):
    for i in range(1,len(c)):
        print("trying key",i," Decrypted text:",decryptMessage(i,c))
        
