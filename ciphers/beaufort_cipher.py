"""
Author: Mohit Radadiya

Organiser: K. Umut Araz
"""

from string import ascii_uppercase

şifreleme_sözlüğü = {char: i for i, char in enumerate(ascii_uppercase)}
çözme_sözlüğü = dict(enumerate(ascii_uppercase))


# Bu fonksiyon, anahtarın uzunluğu
# orijinal metnin uzunluğuna eşit olana kadar
# döngüsel olarak anahtar üretir
def anahtar_üret(message: str, key: str) -> str:
    """
    >>> anahtar_üret("THE GERMAN ATTACK","SECRET")
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


# Bu fonksiyon, anahtar yardımıyla
# üretilen şifreli metni döndürür
def şifreli_metin(message: str, key_new: str) -> str:
    """
    >>> şifreli_metin("THE GERMAN ATTACK","SECRETSECRETSECRE")
    'BDC PAYUWL JPAIYI'
    """
    şifreli_metin = ""
    i = 0
    for letter in message:
        if letter == " ":
            şifreli_metin += " "
        else:
            x = (şifreleme_sözlüğü[letter] - şifreleme_sözlüğü[key_new[i]]) % 26
            i += 1
            şifreli_metin += çözme_sözlüğü[x]
    return şifreli_metin


# Bu fonksiyon, şifreli metni çözer
# ve orijinal metni döndürür
def orijinal_metin(cipher_text: str, key_new: str) -> str:
    """
    >>> orijinal_metin("BDC PAYUWL JPAIYI","SECRETSECRETSECRE")
    'THE GERMAN ATTACK'
    """
    orijinal_txt = ""
    i = 0
    for letter in cipher_text:
        if letter == " ":
            orijinal_txt += " "
        else:
            x = (şifreleme_sözlüğü[letter] + şifreleme_sözlüğü[key_new[i]] + 26) % 26
            i += 1
            orijinal_txt += çözme_sözlüğü[x]
    return orijinal_txt


def main() -> None:
    message = "THE GERMAN ATTACK"
    key = "SECRET"
    key_new = anahtar_üret(message, key)
    s = şifreli_metin(message, key_new)
    print(f"Şifreli Metin = {s}")
    print(f"Orijinal Metin = {orijinal_metin(s, key_new)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
