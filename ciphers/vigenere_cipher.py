import secrets

# TODO: Check linting
# TODO: Perform final cheks on printing and readability
# TODO: Remove  todo's

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main() -> None:
    message = input("Enter message: ")

    print(
        "\nEnter key [alphanumeric], "
        "leave blank for a random key as long as the message."
    )
    key = str(input("Enter the Key: ").strip())

    randomKey = False
    if not len(key):
        randomKey = True
        key = generateRandomKey(message)

    mode = input("Encrypt/Decrypt [e/d]: ")

    if mode.lower().startswith("e"):
        mode = "encrypt"
        translated = encryptMessage(key, message)
    elif mode.lower().startswith("d"):
        mode = "decrypt"
        translated = decryptMessage(key, message)

    print("\n%sed message:" % mode.title())
    print(translated)

    # Print the random key, if selected, after encryption.
    if randomKey and mode.lower().startswith("e"):
        print("Message key:\n%s" % key.lower())


def generateRandomKey(message: str) -> str:
    """Generates a randomized key with a length equal to that of the
    message length, including white space within the message and excluding
    leading and trailing whitespace. Whether used for encrypting or decrypting
    the key is not case sensitive.

    Include module
        secrets

    parameters
        message [str]: The user entered message.

    returns
        [str]: Randomized string of letters with length equal to message length.
    """
    message = message.strip()
    randomKey = []

    [randomKey.append(secrets.choice(LETTERS)) for i, letter in enumerate(message)]
    return "".join(randomKey)


def encryptMessage(key: str, message: str) -> str:
    """
    >>> encryptMessage('HDarji', 'This is Harshil Darji from Dharmaj.')
    'Akij ra Odrjqqs Gaisq muod Mphumrs.'
    """
    return translateMessage(key, message, "encrypt")


def decryptMessage(key: str, message: str) -> str:
    """
    >>> decryptMessage('HDarji', 'Akij ra Odrjqqs Gaisq muod Mphumrs.')
    'This is Harshil Darji from Dharmaj.'
    """
    return translateMessage(key, message, "decrypt")


def translateMessage(key: str, message: str, mode: str) -> str:
    translated = []
    keyIndex = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == "encrypt":
                num += LETTERS.find(key[keyIndex])
            elif mode == "decrypt":
                num -= LETTERS.find(key[keyIndex])

            num %= len(LETTERS)

            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)
    return "".join(translated)


if __name__ == "__main__":
    main()
