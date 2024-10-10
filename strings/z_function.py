"""
https://cp-algorithms.com/string/z-function.html

Z-fonksiyonu veya Z algoritması

Organiser: K. Umut Araz

Bir dizide desenin bulunması için etkili bir algoritmadır.

Zaman Karmaşıklığı: O(n) - burada n, dizenin uzunluğudur.

"""


def z_fonksiyonu(girdi_str: str) -> list[int]:
    """
    Verilen dize için bu fonksiyon, her indeks için değer hesaplar,
    bu değer, indeksin başlangıcından itibaren en uzun alt dizeyi temsil eder
    ve aynı boyuttaki ön ek ile aynıdır.

    Örneğin: 'abab' dizesi için ikinci indeksin değeri 2 olacaktır.

    İlk elemanın değeri için algoritma her zaman 0 döner.

    >>> z_fonksiyonu("abracadabra")
    [0, 0, 0, 1, 0, 1, 0, 4, 0, 0, 1]
    >>> z_fonksiyonu("aaaa")
    [0, 3, 2, 1]
    >>> z_fonksiyonu("zxxzxxz")
    [0, 0, 0, 4, 0, 0, 1]
    """
    z_sonucu = [0 for i in range(len(girdi_str))]

    # aralığın sol ve sağ işaretçilerini başlat
    sol_isaretci, sag_isaretci = 0, 0

    for i in range(1, len(girdi_str)):
        # mevcut indeks aralığın içindeyse
        if i <= sag_isaretci:
            min_kenar = min(sag_isaretci - i + 1, z_sonucu[i - sol_isaretci])
            z_sonucu[i] = min_kenar

        while bir_sonraki(i, z_sonucu, girdi_str):
            z_sonucu[i] += 1

        # yeni indeksin sonucu daha fazla sağ aralık veriyorsa,
        # sol_isaretci ve sag_isaretci'yi güncellememiz gerekiyor
        if i + z_sonucu[i] - 1 > sag_isaretci:
            sol_isaretci, sag_isaretci = i, i + z_sonucu[i] - 1

    return z_sonucu


def bir_sonraki(i: int, z_sonucu: list[int], s: str) -> bool:
    """
    Bir sonraki karakterlere geçmemiz gerekip gerekmediğini kontrol et
    """
    return i + z_sonucu[i] < len(s) and s[z_sonucu[i]] == s[i + z_sonucu[i]]


def desen_bul(pattern: str, girdi_str: str) -> int:
    """
    Z-fonksiyonunun desen bulunmasında kullanım örneği
    Verilen fonksiyon, 'pattern'in
    'girdi_str' içinde alt dize olarak kaç kez göründüğünü döner.

    >>> desen_bul("abr", "abracadabra")
    2
    >>> desen_bul("a", "aaaa")
    4
    >>> desen_bul("xz", "zxxzxxz")
    2
    """
    cevap = 0
    # 'pattern' ve 'girdi_str' dizelerini birleştir ve z_fonksiyonu'nu
    # birleştirilmiş dize ile çağır
    z_sonucu = z_fonksiyonu(pattern + girdi_str)

    for val in z_sonucu:
        # değer, desen dizisinin uzunluğundan büyükse
        # bu indeks, desen dizisi ile eşit olan alt dizenin başlangıç konumudur
        if val >= len(pattern):
            cevap += 1

    return cevap


if __name__ == "__main__":
    import doctest

    doctest.testmod()
