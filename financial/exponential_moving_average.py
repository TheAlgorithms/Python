"""
Hisse senedi fiyatları serisi üzerinde üssel hareketli ortalamayı (EMA) hesaplar.
Wikipedia Referansı: https://en.wikipedia.org/wiki/Exponential_smoothing
https://www.investopedia.com/terms/e/ema.asp#toc-what-is-an-exponential
-moving-average-ema

Üssel hareketli ortalama, finansal analizde hisse senedi fiyatlarındaki değişiklikleri
analiz etmek için kullanılır. EMA, Basit hareketli ortalama (SMA) ile birlikte kullanılır,
EMA, SMA'ya göre değerdeki değişikliklere daha hızlı tepki verir, bu da EMA kullanmanın
avantajlarından biridir.
"""

from collections.abc import Iterator


def ussel_hareketli_ortalama(
    hisse_fiyatlari: Iterator[float], pencere_boyutu: int
) -> Iterator[float]:
    """
    Verilen hisse senedi fiyatlarının üssel hareketli ortalamalarını döndürür.
    >>> tuple(ussel_hareketli_ortalama(iter([2, 5, 3, 8.2, 6, 9, 10]), 3))
    (2, 3.5, 3.25, 5.725, 5.8625, 7.43125, 8.715625)

    :param hisse_fiyatlari: Hisse senedi fiyatlarının bir akışı
    :param pencere_boyutu: Üssel ortalamanın yeni bir hesaplamasını tetikleyecek
                           hisse senedi fiyatlarının sayısı (pencere_boyutu > 0)
    :return: Üssel hareketli ortalamaların bir dizisini döndürür

    Formül:

    st = alpha * xt + (1 - alpha) * st_prev

    Burada,
    st : Zaman damgasında üssel hareketli ortalama t
    xt : Zaman damgasında hisse senedi fiyatı t
    st_prev : Zaman damgasında üssel hareketli ortalama t-1
    alpha : 2/(1 + pencere_boyutu) - yumuşatma faktörü

    Üssel hareketli ortalama (EMA), üssel pencere fonksiyonu kullanarak zaman serisi
    verilerini yumuşatma için bir kuraldır.
    """

    if pencere_boyutu <= 0:
        raise ValueError("pencere_boyutu > 0 olmalıdır")

    # Yumuşatma faktörünü hesaplama
    alpha = 2 / (1 + pencere_boyutu)

    # Zaman damgasında üssel ortalama t
    hareketli_ortalama = 0.0

    for i, hisse_fiyati in enumerate(hisse_fiyatlari):
        if i <= pencere_boyutu:
            # İlk kez pencere_boyutuna ulaşılana kadar basit hareketli ortalama atama
            hareketli_ortalama = (hareketli_ortalama + hisse_fiyati) * 0.5 if i else hisse_fiyati
        else:
            # Mevcut zaman damgası verisine ve önceki üssel ortalama değerine göre
            # üssel hareketli ortalamayı hesaplama
            hareketli_ortalama = (alpha * hisse_fiyati) + ((1 - alpha) * hareketli_ortalama)
        yield hareketli_ortalama


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    hisse_fiyatlari = [2.0, 5, 3, 8.2, 6, 9, 10]
    pencere_boyutu = 3
    sonuc = tuple(ussel_hareketli_ortalama(iter(hisse_fiyatlari), pencere_boyutu))
    print(f"{hisse_fiyatlari = }")
    print(f"{pencere_boyutu = }")
    print(f"{sonuc = }")
