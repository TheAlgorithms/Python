from __future__ import annotations

"""
The trifid cipher is a classical cipher invented by Félix Delastelle in 1902

Wikipedia : https://en.wikipedia.org/wiki/Trifid_cipher

It takes in input the plaintext and the key and encrypts it
For decryption, the same key used in the encryption is required

Syntax : encrypt_message(plaintext, key)
         decrypt_message(encrypted, key)
"""


def __encrypt_part(message_part: str, character_to_number: dict[str, str]) -> str:
    one, two, three = "", "", ""
    tmp = []

    for character in message_part:
        tmp.append(character_to_number[character])

    for each in tmp:
        one += each[0]
        two += each[1]
        three += each[2]

    return one + two + three


def __decrypt_part(
    message_part: str, character_to_number: dict[str, str]
) -> tuple[str, str, str]:
    tmp, this_part = "", ""
    result = []

    for character in message_part:
        this_part += character_to_number[character]

    for digit in this_part:
        tmp += digit
        if len(tmp) == len(message_part):
            result.append(tmp)
            tmp = ""

    return result[0], result[1], result[2]


def __prepare(
    message: str, alphabet: str
) -> tuple[str, str, dict[str, str], dict[str, str]]:
    """__prepare validates the entered message and alphabet to check if
    it satisfies all the given requirements:

    1) message must not create numbers lik 1,2,3 etc
    2) Key must have all the alphabets the message has
    3) Length of the key has to be 27

    >>> __prepare("hello", "ABCDEHG")
    Traceback (most recent call last):
    ...
    KeyError: 'Length of alphabet has to be 27.'

    >>> __prepare("hello", "AABCDEFGGIJKLMNOPQRSTUVWXYZ")
    Traceback (most recent call last):
    ...
     raise ValueError("Each message character has to be included in alphabet!")
    ValueError: Each message character has to be included in alphabet!
    """
    # Validate message and alphabet, set to upper and remove spaces
    alphabet = alphabet.replace(" ", "").upper()
    message = message.replace(" ", "").upper()

    # Check length and characters
    if len(alphabet) != 27:
        raise KeyError("Length of alphabet has to be 27.")
    for each in message:
        if each not in alphabet:
            raise ValueError("Each message character has to be included in alphabet!")

    # Generate dictionares
    numbers = (
        "111",
        "112",
        "113",
        "121",
        "122",
        "123",
        "131",
        "132",
        "133",
        "211",
        "212",
        "213",
        "221",
        "222",
        "223",
        "231",
        "232",
        "233",
        "311",
        "312",
        "313",
        "321",
        "322",
        "323",
        "331",
        "332",
        "333",
    )
    character_to_number = {}
    number_to_character = {}
    for letter, number in zip(alphabet, numbers):
        character_to_number[letter] = number
        number_to_character[number] = letter

    return message, alphabet, character_to_number, number_to_character


def encrypt_message(
    message: str, alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.", period: int = 5
) -> str:
    """
    encrypt_message(message, alphabet, period) encrypts the message using the alphabet
    and period

    1) If not provided, default alphabet is taken as "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    2) If not provided, default period is taken as 5
    3) message is a compulsory argument

    >>> print(encrypt_message("hello world"))
    BOJN.WKPOY

    >>> print(encrypt_message("how are you", "BAECDHFGIJKLMNOPRQTSUVXWZY."))
    HDM.XGULQ

    >>> print(encrypt_message("all aboard the train", "BAECDHFGIJKLMNOPRQTSUVXWZY.", 4))
    DBAYCKFXFCKIVEFON
    """
    message, alphabet, character_to_number, number_to_character = __prepare(
        message, alphabet
    )
    encrypted, encrypted_numeric = "", ""

    for i in range(0, len(message) + 1, period):
        encrypted_numeric += __encrypt_part(
            message[i : i + period], character_to_number
        )

    for i in range(0, len(encrypted_numeric), 3):
        encrypted += number_to_character[encrypted_numeric[i : i + 3]]

    return encrypted


def decrypt_message(
    message: str, alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.", period: int = 5
) -> str:
    """
    decrypt_message(message, alphabet, period) decrypts the message using the alphabet
    and period

    1) If not provided, default alphabet is taken as "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    2) If not provided, default period is taken as 5
    3) message is a compulsory argument

    >>> print(decrypt_message("BOJN.IYSS"))
    HELLOGUYS

    >>> print(decrypt_message("KHQDYRSTJWPYTEAOC", "QWERTYUIOPASDFGHJKLZXCVBNM."))
    ALLABOARDTHETRAIN

    >>> print(decrypt_message("DBAYCKFXFCKIVEFON", "BAECDHFGIJKLMNOPRQTSUVXWZY.", 4))
    ALLABOARDTHETRAIN
    """
    message, alphabet, character_to_number, number_to_character = __prepare(
        message, alphabet
    )
    decrypted_numeric = []
    decrypted = ""

    for i in range(0, len(message) + 1, period):
        a, b, c = __decrypt_part(message[i : i + period], character_to_number)

        for j in range(len(a)):
            decrypted_numeric.append(a[j] + b[j] + c[j])

    for each in decrypted_numeric:
        decrypted += number_to_character[each]

    return decrypted


if __name__ == "__main__":
    import doctest

    doctest.testmod()
