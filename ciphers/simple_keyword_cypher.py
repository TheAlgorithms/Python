def main():
    message = input("Enter message to encode or decode: ")
    key = input("Enter keyword: ")
    option = input("Encipher or decipher? E/D: ")
    key = key.upper()
    message = message.upper()
    cipher = encode(key)
    if option.lower() == 'e':
        enciphered = encipher(message, cipher)
        print(enciphered)
    elif option.lower() == 'd':
        deciphered = decipher(message, cipher)
        print(deciphered)
    else:
        print("Invalid input option")


def encode(key):
    alphabet = []
    cipherAlphabet = {}
    # Create alphabet list
    for i in range(26):
        alphabet.append(chr(i + 65))
    # Remove duplicate characters from key
    key = removeDuplicates(key)
    offset = len(key)
    # First fill cipher with key characters
    for i in range(len(key)):
        cipherAlphabet[alphabet[i]] = key[i]
    # Then map remaining characters in alphabet to
    # the alphabet from the beginning
    for i in range(len(cipherAlphabet.keys()), 26):
        char = alphabet[i - offset]
        # Ensure we are not mapping letters to letters previously mapped
        while key.find(char) != -1:
            offset -= 1
            char = alphabet[i - offset]
        cipherAlphabet[alphabet[i]] = char
    return cipherAlphabet


def removeDuplicates(key):
    keyNoDups = ""
    for ch in key:
        if keyNoDups.find(ch) == -1:
            keyNoDups += ch
    return keyNoDups


def encipher(message, cipher):
    enciphered = ""
    for ch in message:
        if ch.isalpha():
            enciphered += cipher[ch.upper()]
        else:
            enciphered += ' '
    return enciphered


def decipher(message, cipher):
    # Reverse our cipher mappings
    revCipher = dict((v, k) for k, v in cipher.items())
    deciphered = ""
    print(cipher)
    for ch in message:
        if ch.isalpha():
            deciphered += revCipher[ch.upper()]
        else:
            deciphered += ch
    return deciphered


if __name__ == "__main__":
    main()
