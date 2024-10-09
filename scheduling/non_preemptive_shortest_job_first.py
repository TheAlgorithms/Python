"""
Kesintisiz En Kısa İş Önceliği
En kısa yürütme süresine sahip işlem bir sonraki yürütme için seçilir.
https://www.guru99.com/shortest-job-first-sjf-scheduling.html
https://en.wikipedia.org/wiki/Shortest_job_next

Organiser: K. Umut Araz
Github: https://github.com/arazumut
"""

from __future__ import annotations

from statistics import mean


def bekleme_süresi_hesapla(
    varış_zamanı: list[int], patlama_süresi: list[int], işlem_sayısı: int
) -> list[int]:
    """
    Her bir işlemin bekleme süresini hesaplar.

    Dönüş: Her işlem için bekleme süresi.
    >>> bekleme_süresi_hesapla([0,1,2], [10, 5, 8], 3)
    [0, 9, 13]
    >>> bekleme_süresi_hesapla([1,2,2,4], [4, 6, 3, 1], 4)
    [0, 7, 4, 1]
    >>> bekleme_süresi_hesapla([0,0,0], [12, 2, 10],3)
    [12, 0, 2]
    """

    bekleme_süresi = [0] * işlem_sayısı
    kalan_süre = [0] * işlem_sayısı

    # kalan_süre'yi bekleme_süresi ile başlat.

    for i in range(işlem_sayısı):
        kalan_süre[i] = patlama_süresi[i]
    hazır_proses: list[int] = []

    tamamlanan = 0
    toplam_zaman = 0

    # İşlemler tamamlanmadığında,
    # Varış zamanı geçmiş ve kalan yürütme süresi olan bir işlem hazır_proses'e eklenir.
    # Hazır_proses içindeki en kısa işlem, hedef_proses olarak yürütülür.

    while tamamlanan != işlem_sayısı:
        hazır_proses = []
        hedef_proses = -1

        for i in range(işlem_sayısı):
            if (varış_zamanı[i] <= toplam_zaman) and (kalan_süre[i] > 0):
                hazır_proses.append(i)

        if len(hazır_proses) > 0:
            hedef_proses = hazır_proses[0]
            for i in hazır_proses:
                if kalan_süre[i] < kalan_süre[hedef_proses]:
                    hedef_proses = i
            toplam_zaman += patlama_süresi[hedef_proses]
            tamamlanan += 1
            kalan_süre[hedef_proses] = 0
            bekleme_süresi[hedef_proses] = (
                toplam_zaman - varış_zamanı[hedef_proses] - patlama_süresi[hedef_proses]
            )
        else:
            toplam_zaman += 1

    return bekleme_süresi


def dönüş_süresi_hesapla(
    patlama_süresi: list[int], işlem_sayısı: int, bekleme_süresi: list[int]
) -> list[int]:
    """
    Her işlemin dönüş süresini hesaplar.

    Dönüş: Her işlem için dönüş süresi.
    >>> dönüş_süresi_hesapla([0,1,2], 3, [0, 10, 15])
    [0, 11, 17]
    >>> dönüş_süresi_hesapla([1,2,2,4], 4, [1, 8, 5, 4])
    [2, 10, 7, 8]
    >>> dönüş_süresi_hesapla([0,0,0], 3, [12, 0, 2])
    [12, 0, 2]
    """

    dönüş_süresi = [0] * işlem_sayısı
    for i in range(işlem_sayısı):
        dönüş_süresi[i] = patlama_süresi[i] + bekleme_süresi[i]
    return dönüş_süresi


if __name__ == "__main__":
    print("[TEST DURUMU 01]")

    işlem_sayısı = 4
    patlama_süresi = [2, 5, 3, 7]
    varış_zamanı = [0, 0, 0, 0]
    bekleme_süresi = bekleme_süresi_hesapla(varış_zamanı, patlama_süresi, işlem_sayısı)
    dönüş_süresi = dönüş_süresi_hesapla(
        patlama_süresi, işlem_sayısı, bekleme_süresi
    )

    # Sonuçları Yazdırma
    print("PID\tPatlama Süresi\tVarış Zamanı\tBekleme Süresi\tDönüş Süresi")
    for i, işlem_id in enumerate(list(range(1, 5))):
        print(
            f"{işlem_id}\t{patlama_süresi[i]}\t\t\t{varış_zamanı[i]}\t\t\t\t"
            f"{bekleme_süresi[i]}\t\t\t\t{dönüş_süresi[i]}"
        )
    print(f"\nOrtalama bekleme süresi = {mean(bekleme_süresi):.5f}")
    print(f"Ortalama dönüş süresi = {mean(dönüş_süresi):.5f}")
