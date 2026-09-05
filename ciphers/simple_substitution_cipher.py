import random
import sys

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main() -> None:
    message = input("Enter message: ")
    key = "LFWOAYUISVKMNXPBDCRJTQEGHZ"
    resp = input("Encrypt/Decrypt [e/d]: ")

    check_valid_key(key)

    if resp.lower().startswith("e"):
        mode = "encrypt"
        translated = encrypt_message(key, message)
    elif resp.lower().startswith("d"):
        mode = "decrypt"
        translated = decrypt_message(key, message)

    print(f"\n{mode.title()}ion: \n{translated}")


def check_valid_key(key: str) -> None:
    """
    Check if the key is valid (contains all 26 letters of the alphabet exactly once).
    Exits the program if the key is invalid.

    >>> check_valid_key('LFWOAYUISVKMNXPBDCRJTQEGHZ')
    >>> check_valid_key('INVALIDKEY')
    Traceback (most recent call last):
        ...
    SystemExit: Error in the key or symbol set.
    """
    key_list = list(key)
    letters_list = list(LETTERS)
    key_list.sort()
    letters_list.sort()

    if key_list != letters_list:
        sys.exit("Error in the key or symbol set.")


def encrypt_message(key: str, message: str) -> str:
    """
    >>> encrypt_message('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Harshil Darji')
    'Ilcrism Olcvs'
    """
    return translate_message(key, message, "encrypt")


def decrypt_message(key: str, message: str) -> str:
    """
    >>> decrypt_message('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Ilcrism Olcvs')
    'Harshil Darji'
    """
    return translate_message(key, message, "decrypt")


def translate_message(key: str, message: str, mode: str) -> str:
    translated = ""
    chars_a = LETTERS
    chars_b = key

    if mode == "decrypt":
        chars_a, chars_b = chars_b, chars_a

    for symbol in message:
        if symbol.upper() in chars_a:
            sym_index = chars_a.find(symbol.upper())
            if symbol.isupper():
                translated += chars_b[sym_index].upper()
            else:
                translated += chars_b[sym_index].lower()
        else:
            translated += symbol

    return translated


def get_random_key() -> str:
    """
    Generate a random substitution cipher key.

    >>> random.seed(0)
    >>> get_random_key()
    'OAXSGFHKWUECVDRLTJZPQIBNYM'
    """
    key = list(LETTERS)
    random.shuffle(key)
    return "".join(key)


if __name__ == "__main__":
    main()
