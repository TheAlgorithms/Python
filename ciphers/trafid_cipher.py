# https://en.wikipedia.org/wiki/Trifid_cipher
from __future__ import annotations


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
    msg = "DEFEND THE EAST WALL OF THE CASTLE."
    encrypted = encrypt_message(msg, "EPSDUCVWYM.ZLKXNBTFGORIJHAQ")
    decrypted = decrypt_message(encrypted, "EPSDUCVWYM.ZLKXNBTFGORIJHAQ")
    print(f"Encrypted: {encrypted}\nDecrypted: {decrypted}")
