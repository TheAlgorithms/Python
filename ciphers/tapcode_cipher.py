# Python program to implement Tap Code Translator

# Dictionary representing the tap code chart
TAP_CODE_DICT = {
    "A": ". .",
    "B": ". ..",
    "C": ". ...",
    "D": ". ....",
    "E": ". .....",
    "F": ".. .",
    "G": ".. ..",
    "H": ".. ...",
    "I": ".. ....",
    "J": ".. .....",
    "K": ". ...",
    "L": "... .",
    "M": "... ..",
    "N": "... ...",
    "O": "... ....",
    "P": "... .....",
    "Q": ".... .",
    "R": ".... ..",
    "S": ".... ...",
    "T": ".... ....",
    "U": ".... .....",
    "V": "..... .",
    "W": "..... ..",
    "X": "..... ...",
    "Y": "..... ....",
    "Z": "..... .....",
}


def encrypt(message):
    cipher = ""
    for letter in message:
        if letter != " ":
            cipher += TAP_CODE_DICT[letter] + " "
        else:
            cipher += "/ "

    # Remove trailing space added on line 64
    return cipher[:-1]


def decrypt(message):
    decipher = ""
    letters = message.split(" ")
    for letter in letters:
        if letter != "/":
            decipher += list(TAP_CODE_DICT.keys())[
                list(TAP_CODE_DICT.values()).index(letter)
            ]
        else:
            decipher += " "

    return decipher


def main():
    message = "Tap code here"
    result = encrypt(message.upper())
    print(result)

    message = result
    result = decrypt(message)
    print(result)


if __name__ == "__main__":
    main()
