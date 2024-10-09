"""0-1 Sırt Çantası Probleminin basit bir özyinelemeli uygulaması
https://en.wikipedia.org/wiki/Knapsack_problem
"""

from __future__ import annotations


def sirt_cantasi(kapasite: int, agirliklar: list[int], degerler: list[int], sayac: int) -> int:
    """
    Belirli bir kapasiteye sahip bir sırt çantasına konulabilecek maksimum değeri döndürür,
    burada her ağırlığın belirli bir değeri vardır.

    >>> kapasite = 50
    >>> degerler = [60, 100, 120]
    >>> agirliklar = [10, 20, 30]
    >>> sayac = len(degerler)
    >>> sirt_cantasi(kapasite, agirliklar, degerler, sayac)
    220

    Sonuç 220'dir çünkü 100 ve 120 değerleri, kapasite sınırı olan 50 ağırlığına sahiptir.
    """

    # Temel Durum
    if sayac == 0 and kapasite == 0:
        return 0

    # Eğer n'inci öğenin ağırlığı sırt çantasının kapasitesinden fazlaysa,
    #   bu öğe optimal çözüme dahil edilemez,
    # aksi takdirde iki durumun maksimumunu döndür:
    #   (1) n'inci öğe dahil
    #   (2) dahil değil
    if agirliklar[sayac - 1] > kapasite:
        return sirt_cantasi(kapasite, agirliklar, degerler, sayac - 1)
    else:
        kalan_kapasite = kapasite - agirliklar[sayac - 1]
        yeni_deger_dahil = degerler[sayac - 1] + sirt_cantasi(
            kalan_kapasite, agirliklar, degerler, sayac - 1
        )
        yeni_deger_haric = sirt_cantasi(kapasite, agirliklar, degerler, sayac - 1)
        return max(yeni_deger_dahil, yeni_deger_haric)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
