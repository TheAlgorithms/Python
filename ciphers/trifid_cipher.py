"""
The trifid cipher uses a table to fractionate each plaintext letter into a
trigram,mixes the constituents of the trigrams, and then applies the table
in reverse to turn these mixed trigrams into ciphertext letters.
https://en.wikipedia.org/wiki/Trifid_cipher
"""

from __future__ import annotations


def __encrypt_part(message_part: str, character_to_number: dict[str, str]) -> str:
    """
    Arranges the triagram value of each letter of 'message_part' vertically
    and joins them horizontally

    >>> __encrypt_part('ASK',
    ... {'A': '111', 'B': '112', 'C':'113', 'D': '121', 'E': '122', 'F': '123',
    ... 'G': '131', 'H': '132', 'I': '133',
    ... 'J': '211', 'K': '212', 'L': '213', 'M': '221', 'N': '222',
    ... 'O': '223', 'P': '231', 'Q': '232', 'R': '233', 'S': '311', 'T': '312',
    ... 'U': '313', 'V': '321', 'W': '322', 'X': '323', 'Y': '331', 'Z': '332',
    ... '+': '333'})
    '132111112'

    """
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
    """
    Converts each letter of the input string into there respective trigram
    values, joins them and splits them into three equal groups of strings.
    Then returns the group of strings .

    >>> __decrypt_part('ABCDE',
    ... {'A': '111', 'B': '112', 'C':'113', 'D': '121', 'E': '122', 'F': '123',
    ... 'G': '131', 'H': '132', 'I': '133',
    ... 'J': '211', 'K': '212', 'L': '213', 'M': '221', 'N': '222',
    ... 'O': '223', 'P': '231', 'Q': '232', 'R': '233', 'S': '311', 'T': '312',
    ... 'U': '313', 'V': '321', 'W': '322', 'X': '323', 'Y': '331', 'Z': '332',
    ... '+': '333'})
    ('11111', '21131', '21122')
    """
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
    """
    A helper function that generates the triagrams and assigns each letter
    of the alphabet to its corresponding triagram and stores this in a
    dictionary ("character_to_number" and "number_to_character") after
    confirming if the alphabet's length is 27.

    >>> test = __prepare('I aM a BOy','abCdeFghijkLmnopqrStuVwxYZ+')
    >>> expected = ('IAMABOY','ABCDEFGHIJKLMNOPQRSTUVWXYZ+',
    ... {'A': '111', 'B': '112', 'C':'113', 'D': '121', 'E': '122', 'F': '123',
    ... 'G': '131', 'H': '132', 'I': '133',
    ... 'J': '211', 'K': '212', 'L': '213', 'M': '221', 'N': '222',
    ... 'O': '223', 'P': '231', 'Q': '232', 'R': '233', 'S': '311', 'T': '312',
    ... 'U': '313', 'V': '321', 'W': '322', 'X': '323', 'Y': '331', 'Z': '332',
    ... '+': '333'},
    ... {'111': 'A', '112': 'B', '113': 'C', '121': 'D', '122': 'E',
    ... '123': 'F', '131': 'G', '132': 'H', '133': 'I', '211': 'J', '212': 'K',
    ... '213': 'L', '221': 'M', '222': 'N', '223': 'O', '231': 'P', '232': 'Q',
    ... '233': 'R', '311': 'S', '312': 'T', '313': 'U', '321': 'V', '322': 'W',
    ... '323': 'X', '331': 'Y', '332': 'Z', '333': '+'})
    >>> test == expected
    True

    Testing with incomplete alphabet
    >>> __prepare('I aM a BOy','abCdeFghijkLmnopqrStuVw')
    Traceback (most recent call last):
        ...
    KeyError: 'Length of alphabet has to be 27.'

    Testing with extra long alphabets
    >>> __prepare('I aM a BOy','abCdeFghijkLmnopqrStuVwxyzzwwtyyujjgfd')
    Traceback (most recent call last):
        ...
    KeyError: 'Length of alphabet has to be 27.'

    Testing with punctuations that are not in the given alphabet
    >>> __prepare('am i a boy?','abCdeFghijkLmnopqrStuVwxYZ+')
    Traceback (most recent call last):
        ...
    ValueError: Each message character has to be included in alphabet!

    Testing with numbers
    >>> __prepare(500,'abCdeFghijkLmnopqrStuVwxYZ+')
    Traceback (most recent call last):
        ...
    AttributeError: 'int' object has no attribute 'replace'
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
    encrypt_message
    ===============

    Encrypts a message using the trifid_cipher. Any punctuatuions that
    would be used should be added to the alphabet.

    PARAMETERS
    ----------

    *   message: The message you want to encrypt.
    *   alphabet (optional): The characters to be used for the cipher .
    *   period (optional): The number of characters you want in a group whilst
        encrypting.


    >>> encrypt_message('I am a boy')
    'BCDGBQY'

    >>> encrypt_message(' ')
    ''

    >>> encrypt_message('   aide toi le c  iel      ta id  era    ',
    ... 'FELIXMARDSTBCGHJKNOPQUVWYZ+',5)
    'FMJFVOISSUFTFPUFEQQC'

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
    decrypt_message
    ===============

    Decrypts a trifid_cipher encrypted message .

    PARAMETERS
    ----------

    *   message: The message you want to decrypt .
    *   alphabet (optional): The characters used for the cipher.
    *   period (optional): The number of characters used in grouping when it
        was encrypted.

    >>> decrypt_message('BCDGBQY')
    'IAMABOY'

    Decrypting with your own alphabet and period
    >>> decrypt_message('FMJFVOISSUFTFPUFEQQC','FELIXMARDSTBCGHJKNOPQUVWYZ+',5)
    'AIDETOILECIELTAIDERA'
    """
    message, alphabet, character_to_number, number_to_character = __prepare(
        message, alphabet
    )

    decrypted_numeric = []
    decrypted = ""

    for i in range(0, len(message), period):
        a, b, c = __decrypt_part(message[i : i + period], character_to_number)

        for j in range(len(a)):
            decrypted_numeric.append(a[j] + b[j] + c[j])

    for each in decrypted_numeric:
        decrypted += number_to_character[each]

    return decrypted


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    msg = "DEFEND THE EAST WALL OF THE CASTLE."
    encrypted = encrypt_message(msg, "EPSDUCVWYM.ZLKXNBTFGORIJHAQ")
    decrypted = decrypt_message(encrypted, "EPSDUCVWYM.ZLKXNBTFGORIJHAQ")
    print(f"Encrypted: {encrypted}\nDecrypted: {decrypted}")
