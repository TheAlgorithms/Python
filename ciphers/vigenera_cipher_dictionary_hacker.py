import detectEnglish, vigenereCipher, pyperclip


def main():
    ciphertext = """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
    hackedMessage = hackVigenere(ciphertext)

    if hackedMessage != None:
        print("Copying hacked message to clipboard:")
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print("Failed to hack encryption.")


def hackVigenere(ciphertext: str) -> str:
    """
    Return the decrypted text
    """
    with open("dictionary.txt") as in_file:
        words = in_file.readlines()
    for word in words:
        word = word.strip()
        decryptedText = vigenereCipher.decryptMessage(word, ciphertext)
        if detectEnglish.isEnglish(decryptedText, wordPercentage=40):
            # Check with user to see if the decrypted key has been found.
            print()
            print("Possible encryption break:")
            print("Key " + str(word) + ": " + decryptedText[:100])
            print()
            print("Enter D for done, or just press Enter to continue breaking:")
            response = input("> ")

            if response.upper().startswith("D"):
                return decryptedText


if __name__ == "__main__":
    main()
