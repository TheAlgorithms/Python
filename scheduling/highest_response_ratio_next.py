"""
En yüksek yanıt oranı (HRRN) zamanlaması, kesintisiz bir disiplin olarak tanımlanır.
Bu yöntem, süreç açlığı sorununu hafifletmek için en kısa iş önceliği (SJN veya SJF) yönteminin bir modifikasyonu olarak geliştirilmiştir.
https://en.wikipedia.org/wiki/Highest_response_ratio_next
"""

#Organised by K. Umut Araz

from statistics import mean
import numpy as np

def donus_suresini_hesapla(
    proses_adlari: list, varis_zamanlari: list, patlama_zamanlari: list, proses_sayisi: int
) -> list:
    """
    Her bir sürecin dönüş süresini hesaplar.

    Dönüş: Her süreç için dönüş süresi.
    >>> donus_suresini_hesapla(["A", "B", "C"], [3, 5, 8], [2, 4, 6], 3)
    [2, 4, 7]
    >>> donus_suresini_hesapla(["A", "B", "C"], [0, 2, 4], [3, 5, 7], 3)
    [3, 6, 11]
    """

    mevcut_zaman = 0
    # Tamamlanan süreç sayısı
    tamamlanan_proses_sayisi = 0
    # Tamamlanan süreçleri gösterir.
    tamamlanan_proses = [0] * proses_sayisi
    # Hesaplama sonuçlarını içeren liste
    donus_sureleri = [0] * proses_sayisi

    # Varış zamanına göre sırala.
    patlama_zamanlari = [patlama_zamanlari[i] for i in np.argsort(varis_zamanlari)]
    proses_adlari = [proses_adlari[i] for i in np.argsort(varis_zamanlari)]
    varis_zamanlari.sort()

    while proses_sayisi > tamamlanan_proses_sayisi:
        """
        Mevcut zaman, henüz işlenmemiş süreçler arasında ilk gelenin varış zamanından
        küçükse, mevcut zamanı değiştir.
        """
        i = 0
        while tamamlanan_proses[i] == 1:
            i += 1
        mevcut_zaman = max(mevcut_zaman, varis_zamanlari[i])

        yanit_orani = 0
        # İşlem yapılan sürecin konumunu gösteren indeks
        konum = 0
        # Mevcut yanıt oranını kaydeder.
        temp = 0
        for i in range(proses_sayisi):
            if tamamlanan_proses[i] == 0 and varis_zamanlari[i] <= mevcut_zaman:
                temp = (patlama_zamanlari[i] + (mevcut_zaman - varis_zamanlari[i])) / patlama_zamanlari[i]
            if yanit_orani < temp:
                yanit_orani = temp
                konum = i

        # Dönüş süresini hesapla
        donus_sureleri[konum] = mevcut_zaman + patlama_zamanlari[konum] - varis_zamanlari[konum]
        mevcut_zaman += patlama_zamanlari[konum]
        # Sürecin işlendiğini gösterir.
        tamamlanan_proses[konum] = 1
        # Tamamlanan süreç sayısını 1 artır
        tamamlanan_proses_sayisi += 1

    return donus_sureleri

def bekleme_suresini_hesapla(
    proses_adlari: list,  # noqa: ARG001
    donus_sureleri: list,
    patlama_zamanlari: list,
    proses_sayisi: int,
) -> list:
    """
    Her bir sürecin bekleme süresini hesaplar.

    Dönüş: Her süreç için bekleme süresi.
    >>> bekleme_suresini_hesapla(["A", "B", "C"], [2, 4, 7], [2, 4, 6], 3)
    [0, 0, 1]
    >>> bekleme_suresini_hesapla(["A", "B", "C"], [3, 6, 11], [3, 5, 7], 3)
    [0, 1, 4]
    """

    bekleme_sureleri = [0] * proses_sayisi
    for i in range(proses_sayisi):
        bekleme_sureleri[i] = donus_sureleri[i] - patlama_zamanlari[i]
    return bekleme_sureleri

if __name__ == "__main__":
    proses_sayisi = 5
    proses_adlari = ["A", "B", "C", "D", "E"]
    varis_zamanlari = [1, 2, 3, 4, 5]
    patlama_zamanlari = [1, 2, 3, 4, 5]

    donus_sureleri = donus_suresini_hesapla(
        proses_adlari, varis_zamanlari, patlama_zamanlari, proses_sayisi
    )
    bekleme_sureleri = bekleme_suresini_hesapla(
        proses_adlari, donus_sureleri, patlama_zamanlari, proses_sayisi
    )

    print("Proses Adı \tVarış Zamanı \tPatlama Zamanı \tDönüş Süresi \tBekleme Süresi")
    for i in range(proses_sayisi):
        print(
            f"{proses_adlari[i]}\t\t{varis_zamanlari[i]}\t\t{patlama_zamanlari[i]}\t\t"
            f"{donus_sureleri[i]}\t\t\t{bekleme_sureleri[i]}"
        )

    print(f"ortalama bekleme süresi : {mean(bekleme_sureleri):.5f}")
    print(f"ortalama dönüş süresi : {mean(donus_sureleri):.5f}")
