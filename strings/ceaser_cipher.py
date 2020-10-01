
def ceaser_cipher(text: str, s: int) -> str:
    result = ""

    for i in range(len(text)):  # Traverse the text
        char = text[i]

         # Encrypt According to the case
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        elif (char.islower()):
            result += chr((ord(char) + s - 97) % 26 + 97)

        else: # Do not encrypt non alpha characters
            result += char

    return result

if __name__ == "__main__":
    txt = input("Enter text to Encrypt: ")
    key = int(input("Enter Your Key: "))
    print("Encrypted Text:", ceaser_cipher(txt, key))
