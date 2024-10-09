"""
Basit Hareketli Ortalama (SMA), belirli bir zaman diliminde sürekli güncellenen
ortalama fiyatı oluşturarak veri noktalarını analiz etmek için kullanılan istatistiksel bir hesaplamadır.
Finansta, SMA genellikle fiyat verilerini düzleştirmek ve trendleri belirlemek için zaman serisi analizinde kullanılır.

Referans: https://en.wikipedia.org/wiki/Moving_average
"""

from collections.abc import Sequence


def basit_hareketli_ortalama(
    veri: Sequence[float], pencere_boyutu: int
) -> list[float | None]:
    """
    Verilen zaman serisi verileri için basit hareketli ortalamayı (SMA) hesaplayın.

    :param veri: Sayısal veri noktalarının bir listesi.
    :param pencere_boyutu: SMA penceresinin boyutunu temsil eden bir tamsayı.
    :return: Girdi verileriyle aynı uzunlukta bir SMA değerleri listesi.

    Örnekler:
    >>> sma = basit_hareketli_ortalama([10, 12, 15, 13, 14, 16, 18, 17, 19, 21], 3)
    >>> [round(value, 2) if value is not None else None for value in sma]
    [None, None, 12.33, 13.33, 14.0, 14.33, 16.0, 17.0, 18.0, 19.0]
    >>> basit_hareketli_ortalama([10, 12, 15], 5)
    [None, None, None]
    >>> basit_hareketli_ortalama([10, 12, 15, 13, 14, 16, 18, 17, 19, 21], 0)
    Traceback (most recent call last):
    ...
    ValueError: Pencere boyutu pozitif bir tamsayı olmalıdır
    """
    if pencere_boyutu < 1:
        raise ValueError("Pencere boyutu pozitif bir tamsayı olmalıdır")

    sma: list[float | None] = []

    for i in range(len(veri)):
        if i < pencere_boyutu - 1:
            sma.append(None)  # Erken veri noktaları için SMA mevcut değil
        else:
            pencere = veri[i - pencere_boyutu + 1 : i + 1]
            sma_degeri = sum(pencere) / pencere_boyutu
            sma.append(sma_degeri)
    return sma


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Örnek veri (kendi zaman serisi verilerinizle değiştirin)
    veri = [10, 12, 15, 13, 14, 16, 18, 17, 19, 21]

    # SMA için pencere boyutunu belirtin
    pencere_boyutu = 3

    # Basit Hareketli Ortalama'yı hesaplayın
    sma_degerleri = basit_hareketli_ortalama(veri, pencere_boyutu)

    # SMA değerlerini yazdırın
    print("Basit Hareketli Ortalama (SMA) Değerleri:")
    for i, deger in enumerate(sma_degerleri):
        if deger is not None:
            print(f"Gün {i + 1}: {deger:.2f}")
        else:
            print(f"Gün {i + 1}: SMA için yeterli veri yok")
