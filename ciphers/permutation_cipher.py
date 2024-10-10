"""
Permütasyon şifrelemesi, transpozisyon şifrelemesi olarak da bilinen, bir mesajdaki karakterleri gizli bir anahtara dayalı olarak yeniden düzenleyen basit bir şifreleme tekniğidir. Mesajı bloklara ayırır ve her blok içindeki karakterlere anahtara göre bir permütasyon uygular. Anahtar, karakterlerin yeniden düzenlenme sırasını belirleyen benzersiz tam sayıların bir dizisidir.

Daha fazla bilgi için: https://www.nku.edu/~christensen/1402%20permutation%20ciphers.pdf

Organiser: K. Umut Araz
"""

import random


def geçerli_blok_boyutu_oluştur(mesaj_uzunluğu: int) -> int:
    """
    Mesaj uzunluğunun bir çarpanı olan geçerli bir blok boyutu oluşturur.

    Args:
        mesaj_uzunluğu (int): Mesajın uzunluğu.

    Returns:
        int: Geçerli bir blok boyutu.

    Örnek:
        >>> random.seed(1)
        >>> geçerli_blok_boyutu_oluştur(12)
        3
    """
    blok_boyutları = [
        blok_boyutu
        for blok_boyutu in range(2, mesaj_uzunluğu + 1)
        if mesaj_uzunluğu % blok_boyutu == 0
    ]
    return random.choice(blok_boyutları)


def permütasyon_anahtarı_oluştur(blok_boyutu: int) -> list[int]:
    """
    Belirtilen blok boyutunda rastgele bir permütasyon anahtarı oluşturur.

    Args:
        blok_boyutu (int): Her permütasyon bloğunun boyutu.

    Returns:
        list[int]: Rastegele bir rakam permütasyonu içeren bir liste.

    Örnek:
        >>> random.seed(0)
        >>> permütasyon_anahtarı_oluştur(4)
        [2, 0, 1, 3]
    """
    rakamlar = list(range(blok_boyutu))
    random.shuffle(rakamlar)
    return rakamlar


def şifrele(
    mesaj: str, anahtar: list[int] | None = None, blok_boyutu: int | None = None
) -> tuple[str, list[int]]:
    """
    Bir permütasyon şifrelemesi kullanarak mesajı şifreler.

    Args:
        mesaj (str): Şifrelenecek düz metin mesajı.
        anahtar (list[int]): Şifre çözme için permütasyon anahtarı.
        blok_boyutu (int): Her permütasyon bloğunun boyutu.

    Returns:
        tuple: Şifreli mesaj ve şifreleme anahtarını içeren bir tuple.

    Örnek:
        >>> şifreli_mesaj, anahtar = şifrele("MERHABA DÜNYA")
        >>> çözülen_mesaj = şifre_çöz(şifreli_mesaj, anahtar)
        >>> çözülen_mesaj
        'MERHABA DÜNYA'
    """
    mesaj = mesaj.upper()
    mesaj_uzunluğu = len(mesaj)

    if anahtar is None or blok_boyutu is None:
        blok_boyutu = geçerli_blok_boyutu_oluştur(mesaj_uzunluğu)
        anahtar = permütasyon_anahtarı_oluştur(blok_boyutu)

    şifreli_mesaj = ""

    for i in range(0, mesaj_uzunluğu, blok_boyutu):
        blok = mesaj[i : i + blok_boyutu]
        yeniden_düzenlenmiş_blok = [blok[rakam] for rakam in anahtar]
        şifreli_mesaj += "".join(yeniden_düzenlenmiş_blok)

    return şifreli_mesaj, anahtar


def şifre_çöz(şifreli_mesaj: str, anahtar: list[int]) -> str:
    """
    Şifreli bir mesajı permütasyon şifrelemesi ile çözer.

    Args:
        şifreli_mesaj (str): Şifreli mesaj.
        anahtar (list[int]): Şifre çözme için permütasyon anahtarı.

    Returns:
        str: Çözülen düz metin mesajı.

    Örnek:
        >>> şifreli_mesaj, anahtar = şifrele("MERHABA DÜNYA")
        >>> çözülen_mesaj = şifre_çöz(şifreli_mesaj, anahtar)
        >>> çözülen_mesaj
        'MERHABA DÜNYA'
    """
    anahtar_uzunluğu = len(anahtar)
    çözülen_mesaj = ""

    for i in range(0, len(şifreli_mesaj), anahtar_uzunluğu):
        blok = şifreli_mesaj[i : i + anahtar_uzunluğu]
        orijinal_blok = [""] * anahtar_uzunluğu
        for j, rakam in enumerate(anahtar):
            orijinal_blok[rakam] = blok[j]
        çözülen_mesaj += "".join(orijinal_blok)

    return çözülen_mesaj


def ana() -> None:
    """
    Mesajı şifreleyip ardından çözen ana fonksiyon.

    Örnek:
    >>> ana()
    Çözülen mesaj: MERHABA DÜNYA
    """
    mesaj = "MERHABA DÜNYA"
    şifreli_mesaj, anahtar = şifrele(mesaj)

    çözülen_mesaj = şifre_çöz(şifreli_mesaj, anahtar)
    print(f"Çözülen mesaj: {çözülen_mesaj}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    ana()
