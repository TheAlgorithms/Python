"""
Author: Mohit Radadiya
"""

from string import ascii_uppercase

dict1 = {char: i for i, char in enumerate(ascii_uppercase)}
dict2 = dict(enumerate(ascii_uppercase))


# This function generates the key in
# a cyclic manner until it's length isn't
# equal to the length of original text
def generate_key(message: str, key: str) -> str:
    """
    >>> generate_key("THE GERMAN ATTACK","SECRET")
    'SECRETSECRETSECRE'
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
def cipher_text(message: str, key_new: str) -> str:
    """
    >>> cipher_text("THE GERMAN ATTACK","SECRETSECRETSECRE")
    'BDC PAYUWL JPAIYI'
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
def original_text(cipher_text: str, key_new: str) -> str:
    """
    >>> original_text("BDC PAYUWL JPAIYI","SECRETSECRETSECRE")
    'THE GERMAN ATTACK'
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


def main() -> None:
    message = "THE GERMAN ATTACK"
    key = "SECRET"
    key_new = generate_key(message, key)
    s = cipher_text(message, key_new)
    print(f"Encrypted Text = {s}")
    print(f"Original Text = {original_text(s, key_new)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
