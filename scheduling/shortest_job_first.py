"""
En kısa iş önceliği
Lütfen varış zamanını ve işlem süresini not edin.
Lütfen girilen zamanları ayırmak için boşluk kullanın.

Organiser: K. Umut Araz
Github: https://github.com/arazumut
"""

from __future__ import annotations

import pandas as pd


def bekleme_süresi_hesapla(
    varış_zamanı: list[int], işlem_süresi: list[int], işlem_sayısı: int
) -> list[int]:
    """
    Her bir işlemin bekleme süresini hesaplar.
    Dönüş: Bekleme süreleri listesi.
    >>> bekleme_süresi_hesapla([1,2,3,4],[3,3,5,1],4)
    [0, 3, 5, 0]
    >>> bekleme_süresi_hesapla([1,2,3],[2,5,1],3)
    [0, 2, 0]
    >>> bekleme_süresi_hesapla([2,3],[5,1],2)
    [1, 0]
    """
    kalan_süre = [0] * işlem_sayısı
    bekleme_süresi = [0] * işlem_sayısı
    # İşlem sürelerini kalan_süre[] dizisine kopyala
    for i in range(işlem_sayısı):
        kalan_süre[i] = işlem_süresi[i]

    tamamlanan = 0
    zaman_artışı = 0
    min_süre = float('inf')
    kısa = 0
    kontrol = False

    # Tüm işlemler tamamlanana kadar devam et
    while tamamlanan != işlem_sayısı:
        for j in range(işlem_sayısı):
            if (
                varış_zamanı[j] <= zaman_artışı
                and kalan_süre[j] > 0
                and kalan_süre[j] < min_süre
            ):
                min_süre = kalan_süre[j]
                kısa = j
                kontrol = True

        if not kontrol:
            zaman_artışı += 1
            continue
        kalan_süre[kısa] -= 1

        min_süre = kalan_süre[kısa]
        if min_süre == 0:
            min_süre = float('inf')

        if kalan_süre[kısa] == 0:
            tamamlanan += 1
            kontrol = False

            # Mevcut işlemin bitiş zamanını bul
            bitiş_zamanı = zaman_artışı + 1

            # Bekleme süresini hesapla
            bekleme_süresi[kısa] = (bitiş_zamanı - varış_zamanı[kısa]) - işlem_süresi[kısa]
            bekleme_süresi[kısa] = max(bekleme_süresi[kısa], 0)

        # Zamanı artır
        zaman_artışı += 1
    return bekleme_süresi


def dönüş_süresi_hesapla(
    işlem_süresi: list[int], işlem_sayısı: int, bekleme_süresi: list[int]
) -> list[int]:
    """
    Her bir işlemin dönüş süresini hesaplar.
    Dönüş: Dönüş süreleri listesi.
    >>> dönüş_süresi_hesapla([3,3,5,1], 4, [0,3,5,0])
    [3, 6, 10, 1]
    >>> dönüş_süresi_hesapla([3,3], 2, [0,3])
    [3, 6]
    >>> dönüş_süresi_hesapla([8,10,1], 3, [1,0,3])
    [9, 10, 4]
    """
    dönüş_süresi = [0] * işlem_sayısı
    for i in range(işlem_sayısı):
        dönüş_süresi[i] = işlem_süresi[i] + bekleme_süresi[i]
    return dönüş_süresi


def ortalama_süreleri_hesapla(
    bekleme_süresi: list[int], dönüş_süresi: list[int], işlem_sayısı: int
) -> None:
    """
    Bekleme ve dönüş sürelerinin ortalamasını hesaplar.
    Yazdırır: Ortalama Bekleme süresi ve Ortalama Dönüş Süresi
    >>> ortalama_süreleri_hesapla([0,3,5,0],[3,6,10,1],4)
    Ortalama bekleme süresi = 2.00000
    Ortalama dönüş süresi = 5.0
    >>> ortalama_süreleri_hesapla([2,3],[3,6],2)
    Ortalama bekleme süresi = 2.50000
    Ortalama dönüş süresi = 4.5
    >>> ortalama_süreleri_hesapla([10,4,3],[2,7,6],3)
    Ortalama bekleme süresi = 5.66667
    Ortalama dönüş süresi = 5.0
    """
    toplam_bekleme_süresi = 0
    toplam_dönüş_süresi = 0
    for i in range(işlem_sayısı):
        toplam_bekleme_süresi += bekleme_süresi[i]
        toplam_dönüş_süresi += dönüş_süresi[i]
    print(f"Ortalama bekleme süresi = {toplam_bekleme_süresi / işlem_sayısı:.5f}")
    print("Ortalama dönüş süresi =", toplam_dönüş_süresi / işlem_sayısı)


if __name__ == "__main__":
    print("Analiz etmek istediğiniz işlem sayısını girin")
    işlem_sayısı = int(input())
    işlem_süresi = [0] * işlem_sayısı
    varış_zamanı = [0] * işlem_sayısı
    işlemler = list(range(1, işlem_sayısı + 1))

    for i in range(işlem_sayısı):
        print(f"{i + 1}. işlem için varış zamanı ve işlem süresini girin:")
        varış_zamanı[i], işlem_süresi[i] = map(int, input().split())

    bekleme_süresi = bekleme_süresi_hesapla(varış_zamanı, işlem_süresi, işlem_sayısı)

    bt = işlem_süresi
    n = işlem_sayısı
    wt = bekleme_süresi
    dönüş_süresi = dönüş_süresi_hesapla(bt, n, wt)

    ortalama_süreleri_hesapla(bekleme_süresi, dönüş_süresi, işlem_sayısı)

    fcfs = pd.DataFrame(
        list(zip(işlemler, işlem_süresi, varış_zamanı, bekleme_süresi, dönüş_süresi)),
        columns=[
            "İşlem",
            "İşlem Süresi",
            "Varış Zamanı",
            "Bekleme Süresi",
            "Dönüş Süresi",
        ],
    )

    # DataFrame'i yazdırma
    pd.set_option("display.max_rows", fcfs.shape[0] + 1)
    print(fcfs)
