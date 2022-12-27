LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main() -> None:
    message = input("Enter message: ")
    key = input("Enter key [alphanumeric]: ")
    mode = input("Encrypt/Decrypt [e/d]: ")

    if mode.lower().startswith("e"):
        mode = "encrypt"
        translated = encrypt_message(key, message)
    elif mode.lower().startswith("d"):
        mode = "decrypt"
        translated = decrypt_message(key, message)

    print(f"\n{mode.title()}ed message:")
    print(translated)


def encrypt_message(key: str, message: str) -> str:
    """
    >>> encrypt_message('HDarji', 'This is Harshil Darji from Dharmaj.')
    'Akij ra Odrjqqs Gaisq muod Mphumrs.'
    """
    return translate_message(key, message, "encrypt")


def decrypt_message(key: str, message: str) -> str:
    """
    >>> decrypt_message('HDarji', 'Akij ra Odrjqqs Gaisq muod Mphumrs.')
    'This is Harshil Darji from Dharmaj.'
    """
    return translate_message(key, message, "decrypt")


def translate_message(key: str, message: str, mode: str) -> str:
    translated = []
    key_index = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == "encrypt":
                num += LETTERS.find(key[key_index])
            elif mode == "decrypt":
                num -= LETTERS.find(key[key_index])

            num %= len(LETTERS)

            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            key_index += 1
            if key_index == len(key):
                key_index = 0
        else:
            translated.append(symbol)
    return "".join(translated)


if __name__ == "__main__":
    main()
