# Python program to implement Morse Code Translator

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    "&": ".-...",
    "@": ".--.-.",
    ":": "---...",
    ",": "--..--",
    ".": ".-.-.-",
    "'": ".----.",
    '"': ".-..-.",
    "?": "..--..",
    "/": "-..-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    # Exclamation mark is not in ITU-R recommendation
    "!": "-.-.--",
}


def encrypt(message: str) -> str:
    cipher = ""
    for letter in message:
        if letter != " ":
            cipher += MORSE_CODE_DICT[letter] + " "
        else:
            cipher += "/ "

    # Remove trailing space added on line 64
    return cipher[:-1]


def decrypt(message: str) -> str:
    decipher = ""
    letters = message.split(" ")
    for letter in letters:
        if letter != "/":
            decipher += list(MORSE_CODE_DICT.keys())[
                list(MORSE_CODE_DICT.values()).index(letter)
            ]
        else:
            decipher += " "

    return decipher


def main() -> None:
    message = "Morse code here"
    result = encrypt(message.upper())
    print(result)

    message = result
    result = decrypt(message)
    print(result)


if __name__ == "__main__":
    main()
