import random
import sys

from maths.greatest_common_divisor import gcd_by_iterative

from . import cryptomath_module as cryptomath

SYMBOLS = (
    r""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`"""
    r"""abcdefghijklmnopqrstuvwxyz{|}~"""
)


def check_keys(key_a: int, key_b: int, mode: str) -> None:
    if mode == "encrypt":
        if key_a == 1:
            sys.exit(
                "The affine cipher becomes weak when key "
                "A is set to 1. Choose different key"
            )
        if key_b == 0:
            sys.exit(
                "The affine cipher becomes weak when key "
                "B is set to 0. Choose different key"
            )
    if key_a < 0 or key_b < 0 or key_b > len(SYMBOLS) - 1:
        sys.exit(
            "Key A must be greater than 0 and key B must "
            f"be between 0 and {len(SYMBOLS) - 1}."
        )
    if gcd_by_iterative(key_a, len(SYMBOLS)) != 1:
        sys.exit(
            f"Key A {key_a} and the symbol set size {len(SYMBOLS)} "
            "are not relatively prime. Choose a different key."
        )


def encrypt_message(key: int, message: str) -> str:
    """
    >>> encrypt_message(4545, 'The affine cipher is a type of monoalphabetic '
    ...                       'substitution cipher.')
    'VL}p MM{I}p~{HL}Gp{vp pFsH}pxMpyxIx JHL O}F{~pvuOvF{FuF{xIp~{HL}Gi'
    """
    key_a, key_b = divmod(key, len(SYMBOLS))
    check_keys(key_a, key_b, "encrypt")
    cipher_text = ""
    for symbol in message:
        if symbol in SYMBOLS:
            sym_index = SYMBOLS.find(symbol)
            cipher_text += SYMBOLS[(sym_index * key_a + key_b) % len(SYMBOLS)]
        else:
            cipher_text += symbol
    return cipher_text


def decrypt_message(key: int, message: str) -> str:
    """
    >>> decrypt_message(4545, 'VL}p MM{I}p~{HL}Gp{vp pFsH}pxMpyxIx JHL O}F{~pvuOvF{FuF'
    ...                       '{xIp~{HL}Gi')
    'The affine cipher is a type of monoalphabetic substitution cipher.'
    """
    key_a, key_b = divmod(key, len(SYMBOLS))
    check_keys(key_a, key_b, "decrypt")
    plain_text = ""
    mod_inverse_of_key_a = cryptomath.find_mod_inverse(key_a, len(SYMBOLS))
    for symbol in message:
        if symbol in SYMBOLS:
            sym_index = SYMBOLS.find(symbol)
            plain_text += SYMBOLS[
                (sym_index - key_b) * mod_inverse_of_key_a % len(SYMBOLS)
            ]
        else:
            plain_text += symbol
    return plain_text


def get_random_key() -> int:
    while True:
        key_b = random.randint(2, len(SYMBOLS))
        key_b = random.randint(2, len(SYMBOLS))
        if gcd_by_iterative(key_b, len(SYMBOLS)) == 1 and key_b % len(SYMBOLS) != 0:
            return key_b * len(SYMBOLS) + key_b


def main() -> None:
    """
    >>> key = get_random_key()
    >>> msg = "This is a test!"
    >>> decrypt_message(key, encrypt_message(key, msg)) == msg
    True
    """
    message = input("Enter message: ").strip()
    key = int(input("Enter key [2000 - 9000]: ").strip())
    mode = input("Encrypt/Decrypt [E/D]: ").strip().lower()

    if mode.startswith("e"):
        mode = "encrypt"
        translated = encrypt_message(key, message)
    elif mode.startswith("d"):
        mode = "decrypt"
        translated = decrypt_message(key, message)
    print(f"\n{mode.title()}ed text: \n{translated}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # main()
