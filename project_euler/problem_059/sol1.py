"""
Each character on a computer is assigned a unique code
and the preferred standard is ASCII(American Standard
Code for Information Interchange). For example,
uppercase A = 65, asterisk (*) = 42, and lowercase
k = 107.
A modern encryption method is to take a text file,
convert the bytes to ASCII, then XOR each byte with
a given value, taken from a secret key. The advantage
with the XOR function is that using the same encryption
key on the cipher text, restores the plain text; for
example, 65 XOR 42 = 107, then 107 XOR 42 = 65. For
unbreakable encryption, the key is the same length as
the plain text message, and the key is made up of
random bytes. The user would keep the encrypted
message and the encryption key in different locations,
and without both "halves", it is impossible to decrypt
the message.

Unfortunately, this method is impractical for most
users, so the modified method is to use a password as a
key. If the password is shorter than the message,
which is likely, the key is repeated cyclically
throughout the message. The balance for this method is
using a sufficiently long password key for security,
but short enough to be memorable.

Your task has been made easy, as the encryption key
consists of three lower case characters.
Using p059_cipher.txt
(right click and 'Save Link/Target As...'), a file
containing the encrypted ASCII codes, and the knowledge
that the plain text must contain common English words,
decrypt the message and find the sum of the ASCII
values in the original text.
"""

# Import necessary libraries
import os


def solution():
    """
    Finds the sum of the ascii values.
    >>> solution()
    129448
    """

    # Import the cipher file
    script_dir = os.path.abspath(os.path.dirname(__file__))
    cypherFile = os.path.join(script_dir, "p059_cipher.txt")
    with open(cypherFile, "r") as file_hand:
        data = file_hand.read()
        stringArray = data.split(",")
        numArrays = [[], [], []]

        arrayIndex = 0
        for num in stringArray:
            if arrayIndex == 3:
                arrayIndex = 0
            numArrays[arrayIndex].append(int(num))
            arrayIndex += 1

        # Find the three possible password characters
        passwordChars = [0, 0, 0]
        for lowerAscii in range(97, 123):
            for index in range(0, 3):
                possible = True
                for xchar in numArrays[index]:
                    possibleTemp = False
                    if int(xchar) ^ lowerAscii >= 32:
                        if int(xchar) ^ lowerAscii <= 93:
                            possibleTemp = True
                    if int(xchar) ^ lowerAscii >= 97:
                        if int(xchar) ^ lowerAscii <= 122:
                            possibleTemp = True
                    if not possibleTemp:
                        possible = False
                if possible:
                    passwordChars[index] = lowerAscii
        print(passwordChars)
        """
        Decrypt the data into a string, and find the sum
        of the ascii codes of each character in this string
        """
        unencryptedData = ""
        index = 0
        arrayIndex = 0
        valueIndex = 0
        totalValue = 0
        while index < len(stringArray):
            if arrayIndex == 3:
                arrayIndex = 0
                valueIndex += 1
            a = passwordChars[arrayIndex]
            b = numArrays[arrayIndex][valueIndex]
            unencrypted = a ^ b
            totalValue += unencrypted
            unencryptedData += chr(unencrypted)
            arrayIndex += 1
            index += 1
        # Return the total value
        return totalValue

if __name__ == "__main__":
    print(f"{solution() = }")
