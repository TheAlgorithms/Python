binary = ['00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001', '01010',  # A to K
          '01011', '01100', '01101', '01110', '01111', '10000', '10001', '10010', '10011', '10100', '10101',  # L to V
          '10110', '10111', '11000', '11001']  # W to Z

alphabet = "abcdefghijklmnopqrstuvwxyz"


def encrypt(text):
    result = ''
    text = text.lower()
    for x in text:
        if x in alphabet:
            result += binary[alphabet.index(x)] + " "
        else:
            if x == " ":
                result += "* "
    return result


def decrypt(text):
    result = ''
    text = text.split(" ")
    text = text[0:len(text) - 1]  # this erase useless space at the end.
    for x in text:
        if x in binary:
            result += alphabet[binary.index(x)]
        else:
            if x == "*":
                result += " "
    return result


# should return the same phrase you introduce
string = "this is a test"
print(decrypt(encrypt(string)))
