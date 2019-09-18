import sys

alphabet = ".ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
dictionary = {v: k for k, v in enumerate(alphabet)}


def translateCharacter(char, key):
    """Translates a character using the key and tabula recta"""
    for x in range(0, len(alphabet)):
        if dictionary[char] + x > len(alphabet) - 1:
            if dictionary[char] + x - len(alphabet) == dictionary[key]:
                return alphabet[x]
        else:
            if dictionary[char] + x == dictionary[key]:
                return alphabet[x]


def filterInput(string):
    """Filters input from characters that aren't in the alphabet"""
    for n in range(len(string)):
        if not string[n] in alphabet:
            string = string.replace(string[n], alphabet[0])
    return string


def assignKeyMask(input, key):
    """Assigns a key mask with the same length of a given input"""
    keymask = str()
    for i in range(0, len(input) // len(key)):
        keymask += key
    for i in range(0, len(input) % len(key)):
        keymask += key[i]
    return keymask


def useCipher(text, key):
    """Encodes or decodes your input"""
    result = str()
    text = filterInput(text)
    key = filterInput(key)
    keymask = assignKeyMask(text, key)
    for i in range(0, len(text)):
        result += translateCharacter(text[i], keymask[i])
    return result


if __name__ == "__main__":
    if len(sys.argv) > 2:
        text = sys.argv[1]
        key = sys.argv[2]
    else:
        print("Input your message: ")
        text = input()
        print(f"Your input is: '{text}', enter your key: ")
        key = input()

    print(useCipher(text, key))
