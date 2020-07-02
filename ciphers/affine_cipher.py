import random
import sys

import cryptomath_module as cryptomath

SYMBOLS = (
    r""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`"""
    r"""abcdefghijklmnopqrstuvwxyz{|}~"""
)


def main():
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


def check_keys(keyA, keyB, mode):
    if mode == "encrypt":
        if keyA == 1:
            sys.exit(
                "The affine cipher becomes weak when key "
                "A is set to 1. Choose different key"
            )
        if keyB == 0:
            sys.exit(
                "The affine cipher becomes weak when key "
                "B is set to 0. Choose different key"
            )
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit(
            "Key A must be greater than 0 and key B must "
            f"be between 0 and {len(SYMBOLS) - 1}."
        )
    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit(
            f"Key A {keyA} and the symbol set size {len(SYMBOLS)} "
            "are not relatively prime. Choose a different key."
        )


def encrypt_message(key: int, message: str) -> str:
    """
    >>> encrypt_message(4545, 'The affine cipher is a type of monoalphabetic '
    ...                       'substitution cipher.')
    'VL}p MM{I}p~{HL}Gp{vp pFsH}pxMpyxIx JHL O}F{~pvuOvF{FuF{xIp~{HL}Gi'
    """
    keyA, keyB = divmod(key, len(SYMBOLS))
    check_keys(keyA, keyB, "encrypt")
    cipherText = ""
    for symbol in message:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
            cipherText += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            cipherText += symbol
    return cipherText


def decrypt_message(key: int, message: str) -> str:
    """
    >>> decrypt_message(4545, 'VL}p MM{I}p~{HL}Gp{vp pFsH}pxMpyxIx JHL O}F{~pvuOvF{FuF'
    ...                       '{xIp~{HL}Gi')
    'The affine cipher is a type of monoalphabetic substitution cipher.'
    """
    keyA, keyB = divmod(key, len(SYMBOLS))
    check_keys(keyA, keyB, "decrypt")
    plainText = ""
    modInverseOfkeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))
    for symbol in message:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
            plainText += SYMBOLS[(symIndex - keyB) * modInverseOfkeyA % len(SYMBOLS)]
        else:
            plainText += symbol
    return plainText


def get_random_key():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # main()
