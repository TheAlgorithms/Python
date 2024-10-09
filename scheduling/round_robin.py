"""
Round Robin, bir zamanlama algoritmasıdır.
Round Robin'de her işlem, döngüsel bir şekilde sabit bir zaman dilimi ile atanır.
https://en.wikipedia.org/wiki/Round-robin_scheduling

Organiser: K. Umut Araz
Github: https://github.com/arazumut
"""

from __future__ import annotations

from statistics import mean


def bekleme_sürelerini_hesapla(burst_süreleri: list[int]) -> list[int]:
    """
    Belirtilen süreye sahip bir işlem listesi için bekleme sürelerini hesaplar.

    Dönüş: Her işlem için bekleme süresi.
    >>> bekleme_sürelerini_hesapla([10, 5, 8])
    [13, 10, 13]
    >>> bekleme_sürelerini_hesapla([4, 6, 3, 1])
    [5, 8, 9, 6]
    >>> bekleme_sürelerini_hesapla([12, 2, 10])
    [12, 2, 12]
    """
    kuantum = 2
    kalan_burst_süreleri = list(burst_süreleri)
    bekleme_süreleri = [0] * len(burst_süreleri)
    t = 0
    while True:
        tamamlandı = True
        for i, burst_süresi in enumerate(burst_süreleri):
            if kalan_burst_süreleri[i] > 0:
                tamamlandı = False
                if kalan_burst_süreleri[i] > kuantum:
                    t += kuantum
                    kalan_burst_süreleri[i] -= kuantum
                else:
                    t += kalan_burst_süreleri[i]
                    bekleme_süreleri[i] = t - burst_süresi
                    kalan_burst_süreleri[i] = 0
        if tamamlandı is True:
            return bekleme_süreleri


def dönüş_sürelerini_hesapla(
    burst_süreleri: list[int], bekleme_süreleri: list[int]
) -> list[int]:
    """
    >>> dönüş_sürelerini_hesapla([1, 2, 3, 4], [0, 1, 3])
    [1, 3, 6]
    >>> dönüş_sürelerini_hesapla([10, 3, 7], [10, 6, 11])
    [20, 9, 18]
    """
    return [burst + waiting for burst, waiting in zip(burst_süreleri, bekleme_süreleri)]


if __name__ == "__main__":
    burst_süreleri = [3, 5, 7]
    bekleme_süreleri = bekleme_sürelerini_hesapla(burst_süreleri)
    dönüş_süreleri = dönüş_sürelerini_hesapla(burst_süreleri, bekleme_süreleri)
    print("İşlem ID \tBurst Süresi \tBekleme Süresi \tDönüş Süresi")
    for i, burst_süresi in enumerate(burst_süreleri):
        print(
            f"  {i + 1}\t\t  {burst_süresi}\t\t  {bekleme_süreleri[i]}\t\t  "
            f"{dönüş_süreleri[i]}"
        )
    print(f"\nOrtalama bekleme süresi = {mean(bekleme_süreleri):.5f}")
    print(f"Ortalama dönüş süresi = {mean(dönüş_süreleri):.5f}")
