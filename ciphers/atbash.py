"""https://tr.wikipedia.org/wiki/Atbash"""

import string


def atbash_yavaş(dizi: str) -> str:
    """
    >>> atbash_yavaş("ABCDEFG")
    'ZYXWVUT'

    Organiser: K. Umut Araz

    >>> atbash_yavaş("aW;;123BX")
    'zD;;123YC'
    """
    çıktı = ""
    for i in dizi:
        ascii_değeri = ord(i)
        if 65 <= ascii_değeri <= 90:  # Büyük harfler için
            çıktı += chr(155 - ascii_değeri)
        elif 97 <= ascii_değeri <= 122:  # Küçük harfler için
            çıktı += chr(219 - ascii_değeri)
        else:
            çıktı += i  # Harf olmayan karakterler için
    return çıktı


def atbash(dizi: str) -> str:
    """
    >>> atbash("ABCDEFG")
    'ZYXWVUT'

    >>> atbash("aW;;123BX")
    'zD;;123YC'
    """
    harfler = string.ascii_letters
    ters_harfler = string.ascii_lowercase[::-1] + string.ascii_uppercase[::-1]
    return "".join(
        ters_harfler[harfler.index(c)] if c in harfler else c for c in dizi
    )


def benchmark() -> None:
    """Fonksiyonlarımızın performansını yan yana karşılaştıralım..."""
    from timeit import timeit

    print("Performans testleri çalıştırılıyor...")
    setup = "from string import printable ; from __main__ import atbash, atbash_yavaş"
    print(f"> atbash_yavaş(): {timeit('atbash_yavaş(printable)', setup=setup)} saniye")
    print(f">      atbash(): {timeit('atbash(printable)', setup=setup)} saniye")


if __name__ == "__main__":
    for örnek in ("ABCDEFGH", "123GGjj", "testStringtest", "boşluk ile"):
        print(f"{örnek} atbash ile şifrelenmiş: {atbash(örnek)}")
    benchmark()
