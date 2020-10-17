"""
Author: Mohit Radadiya
"""

dict1 = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25,
}

dict2 = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
    10: "K",
    11: "L",
    12: "M",
    13: "N",
    14: "O",
    15: "P",
    16: "Q",
    17: "R",
    18: "S",
    19: "T",
    20: "U",
    21: "V",
    22: "W",
    23: "X",
    24: "Y",
    25: "Z",
}


# This function generates the key in
# a cyclic manner until it's length isn't
# equal to the length of original text
def generate_key(message: str, key: str) -> str:
    """
    >>> generate_key("THE GERMAN ATTACK","SECRET")
    SECRETSECRETSECRE
    """
    x = len(message)
    i = 0
    while True:
        if x == i:
            i = 0
        if len(key) == len(message):
            break
        key += key[i]
        i += 1
    return key


# This function returns the encrypted text
# generated with the help of the key
def cipherText(message: str, key_new: str) -> str:
    """
    >>> cipherText("THE GERMAN ATTACK","SECRETSECRETSECRE")
    BDC PAYUWL JPAIYI
    """
    cipher_text = ""
    i = 0
    for letter in message:
        if letter == " ":
            cipher_text += " "
        else:
            x = (dict1[letter] - dict1[key_new[i]]) % 26
            i += 1
            cipher_text += dict2[x]
    return cipher_text


# This function decrypts the encrypted text
# and returns the original text
def originalText(cipher_text: str, key_new: str) -> str:
    """
    >>> originalText("BDC PAYUWL JPAIYI","SECRETSECRETSECRE")
    THE GERMAN ATTACK
    """
    or_txt = ""
    i = 0
    for letter in cipher_text:
        if letter == " ":
            or_txt += " "
        else:
            x = (dict1[letter] + dict1[key_new[i]] + 26) % 26
            i += 1
            or_txt += dict2[x]
    return or_txt


def main():
    message = "THE GERMAN ATTACK"
    key = "SECRET"
    key_new = generate_key(message, key)
    cipher_text = cipherText(message, key_new)
    original_text = originalText(cipher_text, key_new)
    print("Encrypted Text =", cipher_text)
    print("Original Text =", original_text)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
