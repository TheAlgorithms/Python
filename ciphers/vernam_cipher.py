def vernam_sifrele(düz_metin: str, anahtar: str) -> str:
    """
    >>> vernam_sifrele("MERHABA","ANAHTAR")


    'QFZKJQF'

    #Organiser: K. Umut Araz
    """
    sifreli_metin = ""
    for i in range(len(düz_metin)):
        ct = ord(anahtar[i % len(anahtar)]) - 65 + ord(düz_metin[i]) - 65
        ct %= 26  # 26'dan büyükse döngüye sokmak için
        sifreli_metin += chr(65 + ct)
    return sifreli_metin


def vernam_sifre_coz(sifreli_metin: str, anahtar: str) -> str:
    """
    >>> vernam_sifre_coz("QFZKJQF","ANAHTAR")
    'MERHABA'
    """
    cozulmus_metin = ""
    for i in range(len(sifreli_metin)):
        ct = ord(sifreli_metin[i]) - ord(anahtar[i % len(anahtar)])
        ct %= 26  # 0'dan küçükse döngüye sokmak için
        cozulmus_metin += chr(65 + ct)
    return cozulmus_metin


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    # Örnek kullanım
    düz_metin = "MERHABA"
    anahtar = "ANAHTAR"
    sifreli_metin = vernam_sifrele(düz_metin, anahtar)
    cozulmus_metin = vernam_sifre_coz(sifreli_metin, anahtar)
    print("\n\n")
    print("Düz Metin:", düz_metin)
    print("Şifreli Metin:", sifreli_metin)
    print("Çözülmüş Metin:", cozulmus_metin)
