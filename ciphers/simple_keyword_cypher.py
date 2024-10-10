def tekrar_eden_harfleri_kaldir(key: str) -> str:
    """
    Anahtar kelimedeki tekrar eden alfabetik karakterleri kaldırır (bir harf ilk görünümünden sonra dikkate alınmaz).
    :param key: Kullanılacak anahtar kelime
    :return: Tekrar eden harfler kaldırılmış string
    >>> tekrar_eden_harfleri_kaldir('Merhaba Dünya!!')

    Organiser: K. Umut Araz

    'Merhab Dny'
    """

    key_tekrar_olmayan = ""
    for ch in key:
        if ch == " " or ch not in key_tekrar_olmayan and ch.isalpha():
            key_tekrar_olmayan += ch
    return key_tekrar_olmayan


def sifre_haritasi_olustur(key: str) -> dict[str, str]:
    """
    Verilen bir anahtar kelimeye göre bir şifre haritası döner.
    :param key: Kullanılacak anahtar kelime
    :return: Sözlük şeklinde şifre haritası
    """
    # Alfabenin harflerinden oluşan bir liste oluştur
    alfabeyi = [chr(i + 65) for i in range(26)]
    # Anahtar kelimeden tekrar eden karakterleri kaldır
    key = tekrar_eden_harfleri_kaldir(key.upper())
    offset = len(key)
    # Öncelikle şifreyi anahtar karakterleri ile doldur
    sifre_alfabesi = {alfabeyi[i]: char for i, char in enumerate(key)}
    # Ardından, alfabenin geri kalan karakterlerini
    # baştan itibaren harflerle eşleştir
    for i in range(len(sifre_alfabesi), 26):
        char = alfabeyi[i - offset]
        # Daha önce eşleştirilmiş harfleri tekrar harflere eşleştirmediğimizden emin ol
        while char in key:
            offset -= 1
            char = alfabeyi[i - offset]
        sifre_alfabesi[alfabeyi[i]] = char
    return sifre_alfabesi


def sifrele(mesaj: str, sifre_haritasi: dict[str, str]) -> str:
    """
    Verilen bir şifre haritasına göre bir mesajı şifreler.
    :param mesaj: Şifrelenecek mesaj
    :param sifre_haritasi: Şifre haritası
    :return: Şifrelenmiş string
    >>> sifrele('Merhaba Dünya!!', sifre_haritasi_olustur('Elveda!!'))
    'CYJJM VMQJB!!'
    """
    return "".join(sifre_haritasi.get(ch, ch) for ch in mesaj.upper())


def cozul(mesaj: str, sifre_haritasi: dict[str, str]) -> str:
    """
    Verilen bir şifre haritasına göre bir mesajı çözer.
    :param mesaj: Çözülecek mesaj
    :param sifre_haritasi: Kullanılacak sözlük haritası
    :return: Çözülmüş string
    >>> sifre_haritasi = sifre_haritasi_olustur('Elveda!!')
    >>> cozul(sifrele('Merhaba Dünya!!', sifre_haritasi), sifre_haritasi)
    'MERHABA DÜNYA!!'
    """
    # Şifre eşleştirmelerimizi tersine çevir
    ters_sifre_haritasi = {v: k for k, v in sifre_haritasi.items()}
    return "".join(ters_sifre_haritasi.get(ch, ch) for ch in mesaj.upper())


def ana() -> None:
    """
    Giriş/Çıkış işlemlerini yönetir
    :return: void
    """
    mesaj = input("Şifrelemek veya çözmek için mesaj girin: ").strip()
    key = input("Anahtar kelime girin: ").strip()
    secenek = input("Şifrele veya çöz? Ş/C:").strip()[0].lower()
    try:
        func = {"ş": sifrele, "c": cozul}[secenek]
    except KeyError:
        raise KeyError("Geçersiz giriş seçeneği")
    sifre_haritasi = sifre_haritasi_olustur(key)
    print(func(mesaj, sifre_haritasi))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    ana()
