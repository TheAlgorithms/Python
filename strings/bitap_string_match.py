"""

# Organiser: K. Umut Araz

Bitap tam string eşleştirme
https://tr.wikipedia.org/wiki/Bitap_algoritması

Bir metin içinde bir desen arar ve desenin ilk kez bulunduğu indeksin konumunu döndürür.
Hem metin hem de desen yalnızca küçük harflerden oluşur.

Zaman karmaşıklığı: O(m*n)
    n = metnin uzunluğu
    m = desenin uzunluğu

Python doctest'leri şu komutla çalıştırılabilir:
python3 -m doctest -v bitap_string_match.py
"""


def bitap_string_eslestir(metin: str, desen: str) -> int:
    """
    Desenin metin içinde ilk kez bulunduğu indeksin konumunu döndürür.

    Args:
        metin: Sadece küçük harflerden oluşan bir string.
        desen: Sadece küçük harflerden oluşan bir string.

    Returns:
        int: Desenin ilk bulunduğu indeks. Bulunamazsa -1 döner.

    >>> bitap_string_eslestir('abdabababc', 'ababc')
    5
    >>> bitap_string_eslestir('aaaaaaaaaaaaaaaaaa', 'a')
    0
    >>> bitap_string_eslestir('zxywsijdfosdfnso', 'zxywsijdfosdfnso')
    0
    >>> bitap_string_eslestir('abdabababc', '')
    0
    >>> bitap_string_eslestir('abdabababc', 'c')
    9
    >>> bitap_string_eslestir('abdabababc', 'fofosdfo')
    -1
    >>> bitap_string_eslestir('abdab', 'fofosdfo')
    -1
    """
    if not desen:
        return 0
    m = len(desen)
    if m > len(metin):
        return -1

    # Bit string'in başlangıç durumu 1110
    durum = ~1
    # Karakterin indeksinde görünüyorsa bit 0, aksi takdirde 1
    desen_maskesi: list[int] = [~0] * 27  # 1111

    for i, karakter in enumerate(desen):
        # Bu karakter için desen maskesinde, karakterin her i için bit'i 0 yap
        desen_indeksi: int = ord(karakter) - ord("a")
        desen_maskesi[desen_indeksi] &= ~(1 << i)

    for i, karakter in enumerate(metin):
        metin_indeksi = ord(karakter) - ord("a")
        # Bu karakter desen içinde yoksa, desen maskesi 1111'dir.
        # Durum ile 1111 arasında bitwise OR işlemi yapmak durumu 1111'e sıfırlar
        # ve desenin başlangıcını aramaya başlar.
        durum |= desen_maskesi[metin_indeksi]
        durum <<= 1

        # Durumun m'inci biti (sağdan sola sayıldığında) 0 ise, deseni metin içinde bulmuşuz demektir.
        if (durum & (1 << m)) == 0:
            return i - m + 1

    return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
