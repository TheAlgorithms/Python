"""
https://tr.wikipedia.org/wiki/Raylı_anahtar_şifreleme

#Organiser: K. Umut Araz
"""


def rayli_anahtar_sifrele(anahtar: str, metin: str) -> str:
    """
    Metni Raylı Anahtar Şifreleme yöntemiyle şifreler.

    :param anahtar: Raylı anahtar (uzun bir metin parçası).
    :param metin: Şifrelenecek metin.
    :return: Şifreli metin.
    """
    metin = metin.replace(" ", "").upper()
    anahtar = anahtar.replace(" ", "").upper()
    anahtar_uzunlugu = len(anahtar)
    sifreli_metin = []
    ord_a = ord("A")

    for i, karakter in enumerate(metin):
        p = ord(karakter) - ord_a
        k = ord(anahtar[i % anahtar_uzunlugu]) - ord_a
        c = (p + k) % 26
        sifreli_metin.append(chr(c + ord_a))

    return "".join(sifreli_metin)


def rayli_anahtar_coz(anahtar: str, sifreli_metin: str) -> str:
    """
    Şifreli metni Raylı Anahtar Şifreleme yöntemiyle çözer.

    :param anahtar: Raylı anahtar (uzun bir metin parçası).
    :param sifreli_metin: Şifresi çözülecek metin.
    :return: Çözülmüş metin.
    """
    sifreli_metin = sifreli_metin.replace(" ", "").upper()
    anahtar = anahtar.replace(" ", "").upper()
    anahtar_uzunlugu = len(anahtar)
    metin = []
    ord_a = ord("A")

    for i, karakter in enumerate(sifreli_metin):
        c = ord(karakter) - ord_a
        k = ord(anahtar[i % anahtar_uzunlugu]) - ord_a
        p = (c - k) % 26
        metin.append(chr(p + ord_a))

    return "".join(metin)


def test_rayli_anahtar_sifrele() -> None:
    """
    >>> anahtar = "Örnek anahtar metni"
    >>> sifreli_metin = rayli_anahtar_sifrele(anahtar, "SAVUNUN")
    >>> rayli_anahtar_coz(anahtar, sifreli_metin) == "SAVUNUN"
    True
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_rayli_anahtar_sifrele()

    metin = input("Metni girin: ").upper()
    print(f"\n{metin = }")

    anahtar = "Örnek anahtar metni"
    sifreli_metin = rayli_anahtar_sifrele(anahtar, metin)
    print(f"{sifreli_metin = }")

    cozulmus_metin = rayli_anahtar_coz(anahtar, sifreli_metin)
    print(f"{cozulmus_metin = }")
