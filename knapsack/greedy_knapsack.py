# Sırt Çantası Problemi ile Açgözlü Algoritmaya bir bakış

#Katkı: Produced By K. Umut Araz

"""
Bir bakkalın her biri farklı ağırlıklara ve farklı karlara sahip buğday çuvalları vardır.
ör.
kar 5 8 7 1 12 3 4
ağırlık 2 7 1 6  4 2 5
maks_ağırlık 100

Kısıtlar:
maks_ağırlık > 0
kar[i] >= 0
ağırlık[i] >= 0
Taşınabilecek maksimum ağırlık verildiğinde bakkalın elde edebileceği maksimum karı hesaplayın.
"""


def kar_hesapla(kar: list, ağırlık: list, maks_ağırlık: int) -> int:
    """
    Fonksiyon açıklaması aşağıdaki gibidir-
    :param kar: Kar listesini alır
    :param ağırlık: Karlarla ilişkili ağırlık listesini alır
    :param maks_ağırlık: Taşınabilecek maksimum ağırlık
    :return: Beklenen maksimum kazanç

    >>> kar_hesapla([1, 2, 3], [3, 4, 5], 15)
    6
    >>> kar_hesapla([10, 9 , 8], [3 ,4 , 5], 25)
    27
    """
    if len(kar) != len(ağırlık):
        raise ValueError("Kar ve ağırlık uzunlukları aynı olmalıdır.")
    if maks_ağırlık <= 0:
        raise ValueError("maks_ağırlık sıfırdan büyük olmalıdır.")
    if any(p < 0 for p in kar):
        raise ValueError("Kar negatif olamaz.")
    if any(w < 0 for w in ağırlık):
        raise ValueError("Ağırlık negatif olamaz.")

    # Her bir ağırlık için 1 kg başına elde edilen karı depolamak için liste oluşturuldu
    # Her eleman için kar/ağırlık hesaplayıp ekleyin.
    kar_ağırlık_oranı = [p / w for p, w in zip(kar, ağırlık)]

    # Listenin bir kopyasını oluşturup kar/ağırlık oranını artan sırayla sıralama
    sıralı_kar_ağırlık_oranı = sorted(kar_ağırlık_oranı)

    # Faydalı değişkenler tanımlanıyor
    uzunluk = len(sıralı_kar_ağırlık_oranı)
    limit = 0
    kazanç = 0
    i = 0

    # Toplam ağırlık maks sınırına ulaşana kadar ve i<uzunluk olana kadar döngü
    while limit <= maks_ağırlık and i < uzunluk:
        # sıralı_kar_ağırlık_oranı içindeki en büyük eleman için bayrak değeri
        en_büyük_kar_ağırlık_oranı = sıralı_kar_ağırlık_oranı[uzunluk - i - 1]
        """
        kar_ağırlık_oranı listesinde en_büyük_kar_ağırlık_oranı'nın indeksini hesaplayın.
        Bu, en_büyük_kar_ağırlık_oranı ile aynı olan ilk karşılaşılan elemanın indeksini verir.
        en_büyük_kar_ağırlık_oranı ile aynı olan bir veya daha fazla değer olabilir, ancak indeks
        her zaman yalnızca ilk elemanı karşılar.  Bunu önlemek için kar_ağırlık_oranı'ndaki
        değerleri kullandıktan sonra değiştirin, burada -1 olarak yapılır çünkü ne kar ne de
        ağırlık negatif olamaz.
        """
        indeks = kar_ağırlık_oranı.index(en_büyük_kar_ağırlık_oranı)
        kar_ağırlık_oranı[indeks] = -1

        # Karşılaşılan ağırlığın daha önce karşılaşılan toplam ağırlıktan az olup olmadığını kontrol edin.
        if maks_ağırlık - limit >= ağırlık[indeks]:
            limit += ağırlık[indeks]
            # Verilen ağırlık için elde edilen karı ekleme 1 ===
            # ağırlık[indeks]/ağırlık[indeks]
            kazanç += 1 * kar[indeks]
        else:
            # Karşılaşılan ağırlık limitten büyük olduğundan, kalan kg sayısını alın ve karı hesaplayın.
            # kalan ağırlık / ağırlık[indeks]
            kazanç += (maks_ağırlık - limit) / ağırlık[indeks] * kar[indeks]
            break
        i += 1
    return kazanç


if __name__ == "__main__":
    print(
        "Karları, ağırlıkları ve ardından boşluklarla ayrılmış maksimum ağırlığı (hepsi pozitif tamsayılar) girin."
    )

    kar = [int(x) for x in input("Boşluklarla ayrılmış karları girin: ").split()]
    ağırlık = [int(x) for x in input("Boşluklarla ayrılmış ağırlıkları girin: ").split()]
    maks_ağırlık = int(input("İzin verilen maksimum ağırlık: "))

    # Fonksiyon Çağrısı
    kar_hesapla(kar, ağırlık, maks_ağırlık)
