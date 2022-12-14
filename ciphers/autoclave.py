def encrypt(plaintext, key) -> str:
    """
    Function that encrypt a given plaintext (string)
    and key (string), returning the encrypted ciphertext

    @params
    plaintext - a normal text to be encrypted (string)
    key - a small text or word to start the replacing (sFtring)

    @return
    A string with the ciphertext

    >>> encrypt("hello world", "coffee")
    'jsqqs avvwo'
    """
    if type(plaintext) != str:
        raise TypeError("plaintext must be a string")
    if type(key) != str:
        raise TypeError("key must be a string")

    if plaintext == "":
        raise ValueError("plaintext is empty")
    if key == "":
        raise ValueError("key is empty")

    key = key + plaintext
    plaintext = plaintext.lower()
    key = key.lower()
    plaintext_iterator = 0
    key_iterator = 0
    ciphertext = ""
    while plaintext_iterator < len(plaintext):
        if (
            ord(plaintext[plaintext_iterator]) < 97
            or ord(plaintext[plaintext_iterator]) > 122
        ):
            ciphertext += plaintext[plaintext_iterator]
            plaintext_iterator += 1
        elif ord(key[key_iterator]) < 97 or ord(key[key_iterator]) > 122:
            key_iterator += 1
        else:
            ciphertext += chr(
                (
                    (ord(plaintext[plaintext_iterator]) - 97 + ord(key[key_iterator]))
                    - 97
                )
                % 26
                + 97
            )
            key_iterator += 1
            plaintext_iterator += 1
    return ciphertext


def decrypt(ciphertext: str, key: str) -> str:
    """
    Function that decrypt a given ciphertext (string)
    and key (string), returning the decrypted ciphertext

    @params
    ciphertext - a normal text to be decrypted (string)
    key - a small text or word used to encrypt (string)

    @return
    A string with the ciphertext

    >>> decrypt("jsqqs avvwo", "coffee")
    'hello world'
    """
    if type(ciphertext) != str:
        raise TypeError("ciphertext must be a string")
    if type(key) != str:
        raise TypeError("key must be a string")

    if ciphertext == "":
        raise ValueError("ciphertext is empty")
    if key == "":
        raise ValueError("key is empty")
    ciphertext_iterator = 0
    key_iterator = 0
    plaintext = ""
    while ciphertext_iterator < len(ciphertext):
        if (
            ord(ciphertext[ciphertext_iterator]) < 97
            or ord(ciphertext[ciphertext_iterator]) > 122
        ):
            plaintext += ciphertext[ciphertext_iterator]
        else:
            plaintext += chr(
                (ord(ciphertext[ciphertext_iterator]) - ord(key[key_iterator])) % 26
                + 97
            )
            key += chr(
                (ord(ciphertext[ciphertext_iterator]) - ord(key[key_iterator])) % 26
                + 97
            )
            key_iterator += 1
        ciphertext_iterator += 1
    return plaintext


operation = int(input("Type 1 to encrypt or 2 to decrypt:"))
if operation == 1:
    plaintext = str(input("Typeplaintext to be encrypted:\n"))
    key = str(input("Type the key:\n"))
    print(encrypt(plaintext, key))
elif operation == 2:
    ciphertext = str(input("Type the ciphertext to be decrypted:\n"))
    key = str(input("Type the key:\n"))
    print(decrypt(ciphertext, key))
decrypt("jsqqs avvwo", "coffee")
