def dencrypt(metin: str, n: int = 13) -> str:
    """
    https://en.wikipedia.org/wiki/ROT13

    #Organiser: K. Umut Araz

    >>> mesaj = "Gizli banka hesap numarası 173-52946, lütfen kimseye söyleme!!"
    >>> s = dencrypt(mesaj)
    >>> s
    "Tvzgy onxnu urcnv enzcne 173-52946, yvgu'v xzryr qvgr!!"
    >>> dencrypt(s) == mesaj
    True
    """
    sonuc = ""
    for karakter in metin:
        if "A" <= karakter <= "Z":
            sonuc += chr(ord("A") + (ord(karakter) - ord("A") + n) % 26)
        elif "a" <= karakter <= "z":
            sonuc += chr(ord("a") + (ord(karakter) - ord("a") + n) % 26)
        else:
            sonuc += karakter
    return sonuc


def main() -> None:
    girdi = input("Mesajı girin: ")

    sifreli_metin = dencrypt(girdi, 13)
    print("Şifreleme:", sifreli_metin)

    cozulmus_metin = dencrypt(sifreli_metin, 13)
    print("Şifre Çözme: ", cozulmus_metin)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
