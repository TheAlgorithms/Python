"""
https://tr.wikipedia.org/wiki/Autokey_şifresi
Autokey şifresi (aynı zamanda otoklav şifresi olarak da bilinir), mesajı (açık metni) anahtara dahil eden bir şifreleme yöntemidir.
Anahtar, mesajdan otomatik bir şekilde üretilir; bazen metinden belirli harfler seçilerek veya daha yaygın olarak, kısa bir primer anahtarın mesajın önüne eklenmesiyle oluşturulur.

Organiser: K. Umut Araz
"""


def encrypt(plaintext: str, key: str) -> str:
    """
    Verilen bir açık metni (string) ve anahtarı (string) şifreleyerek,
    şifrelenmiş metni döndürür.
    >>> encrypt("merhaba dünya", "kahve")
    'jsqqs avvwo'
    >>> encrypt("kahve iyi bir şeydir", "Algoritmalar")
    'vvjfpk wj ohvp su ddylsv'
    >>> encrypt("kahve iyi bir şeydir", 2)
    Traceback (most recent call last):
        ...
    TypeError: anahtar bir string olmalıdır
    >>> encrypt("", "Algoritmalar")
    Traceback (most recent call last):
        ...
    ValueError: açık metin boş
    """
    if not isinstance(plaintext, str):
        raise TypeError("açık metin bir string olmalıdır")
    if not isinstance(key, str):
        raise TypeError("anahtar bir string olmalıdır")

    if not plaintext:
        raise ValueError("açık metin boş")
    if not key:
        raise ValueError("anahtar boş")

    key += plaintext
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
    Verilen bir şifreli metni (string) ve anahtarı (string) çözerek,
    çözümlenmiş metni döndürür.
    >>> decrypt("jsqqs avvwo", "kahve")
    'merhaba dünya'
    >>> decrypt("vvjfpk wj ohvp su ddylsv", "Algoritmalar")
    'kahve iyi bir şeydir'
    >>> decrypt("vvjfpk wj ohvp su ddylsv", "")
    Traceback (most recent call last):
        ...
    ValueError: anahtar boş
    >>> decrypt(527.26, "Algoritmalar")
    Traceback (most recent call last):
        ...
    TypeError: şifreli metin bir string olmalıdır
    """
    if not isinstance(ciphertext, str):
        raise TypeError("şifreli metin bir string olmalıdır")
    if not isinstance(key, str):
        raise TypeError("anahtar bir string olmalıdır")

    if not ciphertext:
        raise ValueError("şifreli metin boş")
    if not key:
        raise ValueError("anahtar boş")

    key = key.lower()
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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    operation = int(input("Şifrelemek için 1, çözmek için 2 yazın:"))
    if operation == 1:
        plaintext = input("Şifrelenecek açık metni yazın:\n")
        key = input("Anahtarı yazın:\n")
        print(encrypt(plaintext, key))
    elif operation == 2:
        ciphertext = input("Çözülecek şifreli metni yazın:\n")
        key = input("Anahtarı yazın:\n")
        print(decrypt(ciphertext, key))
    decrypt("jsqqs avvwo", "kahve")
