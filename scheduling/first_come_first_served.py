# İlk Gelen İlk Hizmet (FCFS) zamanlama algoritmasının uygulanması
# Bu algoritmada, süreçlerin geldiği sıraya odaklanıyoruz
# sürelerine dikkat etmeden
# https://en.wikipedia.org/wiki/Scheduling_(computing)#First_come,_first_served
from __future__ import annotations

#Organised by K. Umut Araz


def bekleme_surelerini_hesapla(sureler: list[int]) -> list[int]:
    """
    Bu fonksiyon, belirli bir süreye sahip süreçlerin bekleme sürelerini hesaplar.
        Dönüş: Her süreç için bekleme süresi.
    >>> bekleme_surelerini_hesapla([5, 10, 15])
    [0, 5, 15]
    >>> bekleme_surelerini_hesapla([1, 2, 3, 4, 5])
    [0, 1, 3, 6, 10]
    >>> bekleme_surelerini_hesapla([10, 3])
    [0, 10]
    """
    bekleme_sureleri = [0] * len(sureler)
    for i in range(1, len(sureler)):
        bekleme_sureleri[i] = sureler[i - 1] + bekleme_sureleri[i - 1]
    return bekleme_sureleri


def donus_surelerini_hesapla(
    sureler: list[int], bekleme_sureleri: list[int]
) -> list[int]:
    """
    Bu fonksiyon, bazı süreçlerin dönüş sürelerini hesaplar.
        Dönüş: Tamamlanma süresi ile varış süresi arasındaki zaman farkı.
                Pratikte bekleme_süresi + süre
    >>> donus_surelerini_hesapla([5, 10, 15], [0, 5, 15])
    [5, 15, 30]
    >>> donus_surelerini_hesapla([1, 2, 3, 4, 5], [0, 1, 3, 6, 10])
    [1, 3, 6, 10, 15]
    >>> donus_surelerini_hesapla([10, 3], [0, 10])
    [10, 13]
    """
    return [
        sure + bekleme_sureleri[i]
        for i, sure in enumerate(sureler)
    ]


def ortalama_donus_suresini_hesapla(donus_sureleri: list[int]) -> float:
    """
    Bu fonksiyon, dönüş sürelerinin ortalamasını hesaplar.
        Dönüş: Dönüş sürelerinin ortalaması.
    >>> ortalama_donus_suresini_hesapla([0, 5, 16])
    7.0
    >>> ortalama_donus_suresini_hesapla([1, 5, 8, 12])
    6.5
    >>> ortalama_donus_suresini_hesapla([10, 24])
    17.0
    """
    return sum(donus_sureleri) / len(donus_sureleri)


def ortalama_bekleme_suresini_hesapla(bekleme_sureleri: list[int]) -> float:
    """
    Bu fonksiyon, bekleme sürelerinin ortalamasını hesaplar.
        Dönüş: Bekleme sürelerinin ortalaması.
    >>> ortalama_bekleme_suresini_hesapla([0, 5, 16])
    7.0
    >>> ortalama_bekleme_suresini_hesapla([1, 5, 8, 12])
    6.5
    >>> ortalama_bekleme_suresini_hesapla([10, 24])
    17.0
    """
    return sum(bekleme_sureleri) / len(bekleme_sureleri)


if __name__ == "__main__":
    # süreç kimlikleri
    surecler = [1, 2, 3]

    # gerçekten süreçlerin olduğundan emin ol
    if len(surecler) == 0:
        print("Süreç sayısı sıfır")
        raise SystemExit(0)

    # tüm süreçlerin süreleri
    sureler = [19, 8, 9]

    # her kimliği bir süre ile eşleştirebildiğimizden emin ol
    if len(sureler) != len(surecler):
        print("Tüm kimlikleri süreleri ile eşleştiremiyoruz")
        raise SystemExit(0)

    # bekleme sürelerini ve dönüş sürelerini al
    bekleme_sureleri = bekleme_surelerini_hesapla(sureler)
    donus_sureleri = donus_surelerini_hesapla(sureler, bekleme_sureleri)

    # ortalama süreleri al
    ortalama_bekleme_suresi = ortalama_bekleme_suresini_hesapla(bekleme_sureleri)
    ortalama_donus_suresi = ortalama_donus_suresini_hesapla(donus_sureleri)

    # tüm sonuçları yazdır
    print("Süreç ID\tSüre\tBekleme Süresi\tDönüş Süresi")
    for i, surec in enumerate(surecler):
        print(
            f"{surec}\t\t{sureler[i]}\t\t{bekleme_sureleri[i]}\t\t"
            f"{donus_sureleri[i]}"
        )
    print(f"Ortalama bekleme süresi = {ortalama_bekleme_suresi}")
    print(f"Ortalama dönüş süresi = {ortalama_donus_suresi}")
