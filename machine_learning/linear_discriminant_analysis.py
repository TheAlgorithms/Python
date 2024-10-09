"""
Doğrusal Ayrım Analizi

Veri Hakkında Varsayımlar:
    1. Girdi değişkenlerinin bir Gauss dağılımı vardır.
    2. Sınıf gruplaması ile hesaplanan her girdi değişkeninin varyansı aynıdır.
    3. Eğitim setinizdeki sınıf karışımı, problemin temsilcisidir.

    Organised to K. Umut Araz

Modeli Öğrenme:
    LDA modeli, eğitim verilerinden istatistiklerin tahmin edilmesini gerektirir:
        1. Her sınıf için her girdi değerinin ortalaması.
        2. Bir örneğin her sınıfa ait olma olasılığı.
        3. Her sınıf için girdi verilerinin kovaryansı.

    Sınıf ortalamalarını hesaplayın:
        mean(x) = 1/n * sum(xi) for i = 1 to n

    Sınıf olasılıklarını hesaplayın:
        P(y = 0) = count(y = 0) / (count(y = 0) + count(y = 1))
        P(y = 1) = count(y = 1) / (count(y = 0) + count(y = 1))

    Varyansı hesaplayın:
        Varyansı iki adımda hesaplayabiliriz:
            1. Her girdi değişkeni için grup ortalamasından kare farkı hesaplayın.
            2. Kare farkın ortalamasını hesaplayın.
            ------------------------------------------------
            Kare_Fark = (x - mean(k)) ** 2
            Varyans = (1 / (count(x) - count(classes))) * sum(Kare_Fark(xi)) for i = 1 to n

Tahmin Yapma:
    diskriminant(x) = x * (mean / varyans) - ((mean ** 2) / (2 * varyans)) + ln(olasılık)
    ---------------------------------------------------------------------------
    Her sınıf için diskriminant değeri hesaplandıktan sonra, en büyük diskriminant değerine sahip sınıf tahmin olarak alınır.

Yazar: @EverLookNeverSee
"""

from collections.abc import Callable
from math import log
from os import name, system
from random import gauss, seed
from typing import TypeVar


# Gauss dağılımından alınan bir eğitim veri seti oluşturun
def gauss_dagilimi(mean: float, std_dev: float, ornek_sayisi: int) -> list:
    """
    Verilen ortalama ve standart sapmaya göre Gauss dağılımı örnekleri oluşturun.
    :param mean: Sınıfın ortalama değeri.
    :param std_dev: Kullanıcı tarafından girilen veya varsayılan standart sapma değeri.
    :param ornek_sayisi: Sınıftaki örnek sayısı.
    :return: Verilen ortalama, std_dev ve ornek_sayısına göre oluşturulan değerleri içeren bir liste.

    >>> gauss_dagilimi(5.0, 1.0, 20) # doctest: +NORMALIZE_WHITESPACE
    [6.288184753155463, 6.4494456086997705, 5.066335808938262, 4.235456349028368,
     3.9078267848958586, 5.031334516831717, 3.977896829989127, 3.56317055489747,
      5.199311976483754, 5.133374604658605, 5.546468300338232, 4.086029056264687,
       5.005005283626573, 4.935258239627312, 3.494170998739258, 5.537997178661033,
        5.320711100998849, 7.3891120432406865, 5.202969177309964, 4.855297691835079]
    """
    seed(1)
    return [gauss(mean, std_dev) for _ in range(ornek_sayisi)]


# Sınıfları tespit etmek için karşılık gelen Y bayraklarını oluşturun
def y_olusturucu(sinif_sayisi: int, ornek_sayisi: list) -> list:
    """
    Karşılık gelen sınıflar için y değerleri oluşturun.
    :param sinif_sayisi: Veri setindeki sınıf (veri gruplaması) sayısı.
    :param ornek_sayisi: Sınıftaki örnek sayısı.
    :return: Veri setindeki veri gruplamaları için karşılık gelen değerler.

    >>> y_olusturucu(1, [10])
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> y_olusturucu(2, [5, 10])
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    >>> y_olusturucu(4, [10, 5, 15, 20]) # doctest: +NORMALIZE_WHITESPACE
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
     2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    """
    return [k for k in range(sinif_sayisi) for _ in range(ornek_sayisi[k])]


# Sınıf ortalamalarını hesaplayın
def ortalama_hesapla(ornek_sayisi: int, elemanlar: list) -> float:
    """
    Verilen sınıf ortalamasını hesaplayın.
    :param ornek_sayisi: Sınıftaki örnek sayısı.
    :param elemanlar: Belirli bir sınıfla (veri gruplaması) ilgili öğeler.
    :return: İlgili sınıfın hesaplanan gerçek ortalaması.

    >>> elemanlar = gauss_dagilimi(5.0, 1.0, 20)
    >>> ortalama_hesapla(len(elemanlar), elemanlar)
    5.011267842911003
    """
    # Tüm elemanların toplamı, örnek sayısına bölünür
    return sum(elemanlar) / ornek_sayisi


# Sınıf olasılıklarını hesaplayın
def olasilik_hesapla(ornek_sayisi: int, toplam_sayi: int) -> float:
    """
    Verilen bir örneğin hangi sınıfa ait olacağını hesaplayın.
    :param ornek_sayisi: Sınıftaki örnek sayısı.
    :param toplam_sayi: Tüm örneklerin sayısı.
    :return: İlgili sınıf için olasılık değeri.

    >>> olasilik_hesapla(20, 60)
    0.3333333333333333
    >>> olasilik_hesapla(30, 100)
    0.3
    """
    # Belirli bir sınıftaki örnek sayısı, tüm örneklerin sayısına bölünür
    return ornek_sayisi / toplam_sayi


# Varyansı hesaplayın
def varyans_hesapla(elemanlar: list, ortalamalar: list, toplam_sayi: int) -> float:
    """
    Varyansı hesaplayın.
    :param elemanlar: Tüm elemanları içeren bir liste (tüm sınıfların Gauss dağılımı).
    :param ortalamalar: Her sınıfın gerçek ortalama değerlerini içeren bir liste.
    :param toplam_sayi: Tüm örneklerin sayısı.
    :return: İlgili veri seti için hesaplanan varyans.

    >>> elemanlar = gauss_dagilimi(5.0, 1.0, 20)
    >>> ortalamalar = [5.011267842911003]
    >>> toplam_sayi = 20
    >>> varyans_hesapla([elemanlar], ortalamalar, toplam_sayi)
    0.9618530973487491
    """
    kare_fark = []  # Tüm kare farkları depolamak için boş bir liste
    # Elemanların içindeki eleman sayısı kadar döngü
    for i in range(len(elemanlar)):
        # Elemanların iç katmanındaki eleman sayısı kadar döngü
        for j in range(len(elemanlar[i])):
            # 'kare_fark' listesine kare farkları ekleme
            kare_fark.append((elemanlar[i][j] - ortalamalar[i]) ** 2)

    # Tüm örneklerin sayısının (sınıf sayısı - 1) eksi biri ile çarpılması ve
    # tüm kare farklarının toplamı
    sinif_sayisi = len(ortalamalar)  # Veri setindeki sınıf sayısı
    return 1 / (toplam_sayi - sinif_sayisi) * sum(kare_fark)


# Tahmin yapma
def y_degerlerini_tahmin_et(
    x_elemanlar: list, ortalamalar: list, varyans: float, olasiliklar: list
) -> list:
    """Bu fonksiyon yeni indeksleri (veri gruplarını) tahmin eder.
    :param x_elemanlar: Tüm elemanları içeren bir liste (tüm sınıfların Gauss dağılımı).
    :param ortalamalar: Her sınıfın gerçek ortalama değerlerini içeren bir liste.
    :param varyans: varyans_hesapla fonksiyonu tarafından hesaplanan varyans değeri.
    :param olasiliklar: Tüm sınıfların olasılıklarını içeren bir liste.
    :return: Tahmin edilen Y değerlerini içeren bir liste.

    >>> x_elemanlar = [[6.288184753155463, 6.4494456086997705, 5.066335808938262,
    ...                4.235456349028368, 3.9078267848958586, 5.031334516831717,
    ...                3.977896829989127, 3.56317055489747, 5.199311976483754,
    ...                5.133374604658605, 5.546468300338232, 4.086029056264687,
    ...                5.005005283626573, 4.935258239627312, 3.494170998739258,
    ...                5.537997178661033, 5.320711100998849, 7.3891120432406865,
    ...                5.202969177309964, 4.855297691835079], [11.288184753155463,
    ...                11.44944560869977, 10.066335808938263, 9.235456349028368,
    ...                8.907826784895859, 10.031334516831716, 8.977896829989128,
    ...                8.56317055489747, 10.199311976483754, 10.133374604658606,
    ...                10.546468300338232, 9.086029056264687, 10.005005283626572,
    ...                9.935258239627313, 8.494170998739259, 10.537997178661033,
    ...                10.320711100998848, 12.389112043240686, 10.202969177309964,
    ...                9.85529769183508], [16.288184753155463, 16.449445608699772,
    ...                15.066335808938263, 14.235456349028368, 13.907826784895859,
    ...                15.031334516831716, 13.977896829989128, 13.56317055489747,
    ...                15.199311976483754, 15.133374604658606, 15.546468300338232,
    ...                14.086029056264687, 15.005005283626572, 14.935258239627313,
    ...                13.494170998739259, 15.537997178661033, 15.320711100998848,
    ...                17.389112043240686, 15.202969177309964, 14.85529769183508]]

    >>> ortalamalar = [5.011267842911003, 10.011267842911003, 15.011267842911002]
    >>> varyans = 0.9618530973487494
    >>> olasiliklar = [0.3333333333333333, 0.3333333333333333, 0.3333333333333333]
    >>> y_degerlerini_tahmin_et(x_elemanlar, ortalamalar, varyans,
    ...                  olasiliklar)  # doctest: +NORMALIZE_WHITESPACE
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2, 2]

    """
    # Veri setindeki her sınıf için oluşturulan diskriminant değerlerini depolamak için boş bir liste
    sonuc = []
    # Listenin eleman sayısı kadar döngü
    for i in range(len(x_elemanlar)):
        # Her elemanın içindeki eleman sayısı kadar döngü
        for j in range(len(x_elemanlar[i])):
            temp = []  # Her elemanın diskriminant değerlerini liste olarak depolamak için
            # Veri setimizdeki sınıf sayısı kadar döngü
            for k in range(len(x_elemanlar)):
                # Her sınıf için diskriminant değerlerini 'temp' listesine ekleme
                temp.append(
                    x_elemanlar[i][j] * (ortalamalar[k] / varyans)
                    - (ortalamalar[k] ** 2 / (2 * varyans))
                    + log(olasiliklar[k])
                )
            # Her elemanın diskriminant değerlerini 'sonuc' listesine ekleme
            sonuc.append(temp)

    return [sonuc.index(max(sonuc)) for sonuc in sonuc]


# Doğruluk Hesaplama
def dogruluk(gercek_y: list, tahmin_y: list) -> float:
    """
    Tahminlere dayalı olarak doğruluk değerini hesaplayın.
    :param gercek_y: 'y_olusturucu' fonksiyonu tarafından oluşturulan başlangıç Y değerlerini içeren bir liste.
    :param tahmin_y: 'y_degerlerini_tahmin_et' fonksiyonu tarafından oluşturulan tahmin edilen Y değerlerini içeren bir liste.
    :return: Doğruluk yüzdesi.

    >>> gercek_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
    ... 1, 1 ,1 ,1 ,1 ,1 ,1]
    >>> tahmin_y = [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0,
    ... 0, 0, 1, 1, 1, 0, 1, 1, 1]
    >>> dogruluk(gercek_y, tahmin_y)
    50.0

    >>> gercek_y = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
    ... 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    >>> tahmin_y = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
    ... 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    >>> dogruluk(gercek_y, tahmin_y)
    100.0
    """
    # Her seferinde bir eleman üzerinde yineleme (zip modu)
    # Tahmin doğruysa gerçek Y değeri tahmin edilen Y değerine eşittir
    dogru = sum(1 for i, j in zip(gercek_y, tahmin_y) if i == j)
    # Doğruluk yüzdesi, doğru tahminlerin sayısının tüm verilerin sayısına bölünmesi ve 100 ile çarpılmasıdır
    return (dogru / len(gercek_y)) * 100


num = TypeVar("num")


def gecerli_girdi(
    girdi_turu: Callable[[object], num],  # Genellikle float veya int
    girdi_mesaji: str,
    hata_mesaji: str,
    kosul: Callable[[num], bool] = lambda _: True,
    varsayilan: str | None = None,
) -> num:
    """
    Kullanıcı değerini isteyin ve bir koşulu yerine getirdiğini doğrulayın.

    :girdi_turu: Kullanıcı girdisinin beklenen değer türü.
    :girdi_mesaji: Kullanıcıya ekranda gösterilecek mesaj.
    :hata_mesaji: Hata durumunda ekranda gösterilecek mesaj.
    :kosul: Kullanıcı girdisinin geçerli olduğunu temsil eden fonksiyon.
    :varsayilan: Kullanıcı hiçbir şey yazmazsa varsayılan değer.
    :return: Kullanıcının girdisi.
    """
    while True:
        try:
            kullanici_girdisi = girdi_turu(input(girdi_mesaji).strip() or varsayilan)
            if kosul(kullanici_girdisi):
                return kullanici_girdisi
            else:
                print(f"{kullanici_girdisi}: {hata_mesaji}")
                continue
        except ValueError:
            print(
                f"{kullanici_girdisi}: Yanlış girdi türü, beklenen {girdi_turu.__name__!r}"
            )


# Ana Fonksiyon
def main():
    """Bu fonksiyon yürütme aşamasını başlatır."""
    while True:
        print(" Doğrusal Ayrım Analizi ".center(50, "*"))
        print("*" * 50, "\n")
        print("Öncelikle, eğitim veri seti olarak oluşturmak istediğimiz")
        print("sınıf sayısını belirtmeliyiz.")
        # Sınıf sayısını almaya çalışmak
        sinif_sayisi = gecerli_girdi(
            girdi_turu=int,
            kosul=lambda x: x > 0,
            girdi_mesaji="Sınıf sayısını (Veri Gruplamaları) girin: ",
            hata_mesaji="Sınıf sayısı pozitif olmalıdır!",
        )

        print("-" * 100)

        # Standart sapma değerini almaya çalışmak
        std_dev = gecerli_girdi(
            girdi_turu=float,
            kosul=lambda x: x >= 0,
            girdi_mesaji=(
                "Standart sapma değerini girin"
                "(Varsayılan değer tüm sınıflar için 1.0'dır): "
            ),
            hata_mesaji="Standart sapma negatif olmamalıdır!",
            varsayilan="1.0",
        )

        print("-" * 100)

        # Sınıflardaki örnek sayısını ve veri setini oluşturmak için ortalamalarını almaya çalışmak
        sayilar = []  # Veri setindeki sınıfların örnek sayılarını depolamak için boş bir liste
        for i in range(sinif_sayisi):
            kullanici_sayisi = gecerli_girdi(
                girdi_turu=int,
                kosul=lambda x: x > 0,
                girdi_mesaji=(f"class_{i+1} için örnek sayısını girin: "),
                hata_mesaji="Örnek sayısı pozitif olmalıdır!",
            )
            sayilar.append(kullanici_sayisi)
        print("-" * 100)

        # Sınıfların kullanıcı tarafından girilen ortalama değerlerini depolamak için boş bir liste
        kullanici_ortalamalari = []
        for a in range(sinif_sayisi):
            kullanici_ortalamasi = gecerli_girdi(
                girdi_turu=float,
                girdi_mesaji=(f"class_{a+1} için ortalama değerini girin: "),
                hata_mesaji="Bu geçersiz bir değerdir.",
            )
            kullanici_ortalamalari.append(kullanici_ortalamasi)
        print("-" * 100)

        print("Standart sapma: ", std_dev)
        # Sınıflardaki örnek sayılarını ayrı bir satırda yazdırın
        for i, sayi in enumerate(sayilar, 1):
            print(f"class_{i} içindeki örnek sayısı: {sayi}")
        print("-" * 100)

        # Sınıfların ortalama değerlerini ayrı bir satırda yazdırın
        for i, kullanici_ortalamasi in enumerate(kullanici_ortalamalari, 1):
            print(f"class_{i} ortalaması: {kullanici_ortalamasi}")
        print("-" * 100)

        # Gauss dağılımından alınan eğitim veri seti oluşturma
        x = [
            gauss_dagilimi(kullanici_ortalamalari[j], std_dev, sayilar[j])
            for j in range(sinif_sayisi)
        ]
        print("Oluşturulan Normal Dağılım: \n", x)
        print("-" * 100)

        # Karşılık gelen sınıfları tespit etmek için Y'leri oluşturma
        y = y_olusturucu(sinif_sayisi, sayilar)
        print("Oluşturulan Karşılık Gelen Y'ler: \n", y)
        print("-" * 100)

        # Her sınıf için gerçek ortalama değerini hesaplama
        gercek_ortalamalar = [ortalama_hesapla(sayilar[k], x[k]) for k in range(sinif_sayisi)]
        # 'gercek_ortalamalar' listesindeki eleman sayısı kadar döngü ve ayrı bir satırda yazdırma
        for i, gercek_ortalama in enumerate(gercek_ortalamalar, 1):
            print(f"class_{i} gerçek ortalaması: {gercek_ortalama}")
        print("-" * 100)

        # Her sınıf için olasılık değerini hesaplama
        olasiliklar = [
            olasilik_hesapla(sayilar[i], sum(sayilar)) for i in range(sinif_sayisi)
        ]

        # 'olasiliklar' listesindeki eleman sayısı kadar döngü ve ayrı bir satırda yazdırma
        for i, olasilik in enumerate(olasiliklar, 1):
            print(f"class_{i} olasılığı: {olasilik}")
        print("-" * 100)

        # Her sınıf için varyans değerini hesaplama
        varyans = varyans_hesapla(x, gercek_ortalamalar, sum(sayilar))
        print("Varyans: ", varyans)
        print("-" * 100)

        # Y değerlerini tahmin etme
        # Tahmin edilen Y değerlerini 'tahmin_indeksleri' değişkenine depolama
        tahmin_indeksleri = y_degerlerini_tahmin_et(x, gercek_ortalamalar, varyans, olasiliklar)
        print("-" * 100)

        # Modelin Doğruluğunu Hesaplama
        print(f"Doğruluk: {dogruluk(y, tahmin_indeksleri)}")
        print("-" * 100)
        print(" TAMAMLANDI ".center(100, "+"))

        if input("Yeniden başlatmak için herhangi bir tuşa basın veya çıkmak için 'q' tuşuna basın: ").strip().lower() == "q":
            print("\n" + "Hoşçakal!".center(100, "-") + "\n")
            break
        system("cls" if name == "nt" else "clear")  # noqa: S605


if __name__ == "__main__":
    main()
