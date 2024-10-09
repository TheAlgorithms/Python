#!/usr/bin/env python3

# Bu Python programı, O(n^2) performans sunan dinamik programlama algoritması ile
# optimal bir ikili arama ağacı (BST) oluşturur.
#
# Optimal BST probleminin amacı, her biri kendi anahtar ve frekansına sahip bir
# dizi düğüm için düşük maliyetli bir BST oluşturmaktır. Düğümün frekansı, düğümün
# kaç kez arandığını tanımlar. İkili arama ağacının arama maliyeti şu formülle verilir:
#
# maliyet(1, n) = sum{i = 1 to n}((derinlik(düğüm_i) + 1) * düğüm_i_frekans)
#
# burada n, BST'deki düğüm sayısıdır. Düşük maliyetli BST'lerin özelliği, diğer
# uygulamalara göre daha hızlı genel arama süresine sahip olmalarıdır. Bunun nedeni,
# yüksek frekanslı düğümlerin ağacın köküne yakın, düşük frekanslı düğümlerin ise
# ağacın yapraklarına yakın yerleştirilmesidir, bu da en sık arama durumlarında
# arama süresini azaltır.
import sys
from random import randint


class Dugum:
    """İkili Arama Ağacı Düğümü"""

    def __init__(self, anahtar, frekans):
        self.anahtar = anahtar
        self.frekans = frekans

    def __str__(self):
        """
        >>> str(Dugum(1, 2))
        'Dugum(anahtar=1, frekans=2)'
        """
        return f"Dugum(anahtar={self.anahtar}, frekans={self.frekans})"


def ikili_arama_agacini_yazdir(kok, anahtar, i, j, ebeveyn, sol_mu):
    """
    Bir kök tablosundan bir BST yazdırmak için özyinelemeli fonksiyon.

    >>> anahtar = [3, 8, 9, 10, 17, 21]
    >>> kok = [[0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 3], [0, 0, 2, 3, 3, 3], \
                [0, 0, 0, 3, 3, 3], [0, 0, 0, 0, 4, 5], [0, 0, 0, 0, 0, 5]]
    >>> ikili_arama_agacini_yazdir(kok, anahtar, 0, 5, -1, False)
    8 ikili arama ağacının köküdür.
    3, 8 anahtarının sol çocuğudur.
    10, 8 anahtarının sağ çocuğudur.
    9, 10 anahtarının sol çocuğudur.
    21, 10 anahtarının sağ çocuğudur.
    17, 21 anahtarının sol çocuğudur.
    """
    if i > j or i < 0 or j > len(kok) - 1:
        return

    dugum = kok[i][j]
    if ebeveyn == -1:  # kökün ebeveyni yoktur
        print(f"{anahtar[dugum]} ikili arama ağacının köküdür.")
    elif sol_mu:
        print(f"{anahtar[dugum]}, {ebeveyn} anahtarının sol çocuğudur.")
    else:
        print(f"{anahtar[dugum]}, {ebeveyn} anahtarının sağ çocuğudur.")

    ikili_arama_agacini_yazdir(kok, anahtar, i, dugum - 1, anahtar[dugum], True)
    ikili_arama_agacini_yazdir(kok, anahtar, dugum + 1, j, anahtar[dugum], False)


def optimal_ikili_arama_agacini_bul(dugumler):
    """
    Bu fonksiyon optimal ikili arama ağacını hesaplar ve yazdırır.
    Aşağıdaki dinamik programlama algoritması O(n^2) zamanında çalışır.
    CLRS (Introduction to Algorithms) kitabından uygulanmıştır.
    https://en.wikipedia.org/wiki/Introduction_to_Algorithms

    >>> optimal_ikili_arama_agacini_bul([Dugum(12, 8), Dugum(10, 34), Dugum(20, 50), \
                                         Dugum(42, 3), Dugum(25, 40), Dugum(37, 30)])
    İkili arama ağacı düğümleri:
    Dugum(anahtar=10, frekans=34)
    Dugum(anahtar=12, frekans=8)
    Dugum(anahtar=20, frekans=50)
    Dugum(anahtar=25, frekans=40)
    Dugum(anahtar=37, frekans=30)
    Dugum(anahtar=42, frekans=3)
    <BLANKLINE>
    Verilen ağaç düğümleri için optimal BST'nin maliyeti 324.
    20 ikili arama ağacının köküdür.
    10, 20 anahtarının sol çocuğudur.
    12, 10 anahtarının sağ çocuğudur.
    25, 20 anahtarının sağ çocuğudur.
    37, 25 anahtarının sağ çocuğudur.
    42, 37 anahtarının sağ çocuğudur.
    """
    # Ağaç düğümleri önce sıralanmalıdır, aşağıdaki kod anahtarları artan sırayla sıralar
    # ve frekanslarını buna göre yeniden düzenler.
    dugumler.sort(key=lambda dugum: dugum.anahtar)

    n = len(dugumler)

    anahtarlar = [dugumler[i].anahtar for i in range(n)]
    frekanslar = [dugumler[i].frekans for i in range(n)]

    # Bu 2D dizi, genel ağaç maliyetini saklar (mümkün olduğunca minimize edilmiş);
    # tek bir anahtar için maliyet, anahtarın frekansına eşittir.
    dp = [[frekanslar[i] if i == j else 0 for j in range(n)] for i in range(n)]
    # toplam[i][j], düğümler dizisinde i ve j dahil olmak üzere anahtar frekanslarının toplamını saklar
    toplam = [[frekanslar[i] if i == j else 0 for j in range(n)] for i in range(n)]
    # ikili arama ağacını oluşturmak için daha sonra kullanılacak ağaç köklerini saklar
    kok = [[i if i == j else 0 for j in range(n)] for i in range(n)]

    for aralik_uzunlugu in range(2, n + 1):
        for i in range(n - aralik_uzunlugu + 1):
            j = i + aralik_uzunlugu - 1

            dp[i][j] = sys.maxsize  # değeri "sonsuz" olarak ayarla
            toplam[i][j] = toplam[i][j - 1] + frekanslar[j]

            # Knuth'un optimizasyonunu uygula
            # Optimizasyon olmadan döngü: for r in range(i, j + 1):
            for r in range(kok[i][j - 1], kok[i + 1][j] + 1):  # r geçici bir köktür
                sol = dp[i][r - 1] if r != i else 0  # sol alt ağaç için optimal maliyet
                sag = dp[r + 1][j] if r != j else 0  # sağ alt ağaç için optimal maliyet
                maliyet = sol + toplam[i][j] + sag

                if dp[i][j] > maliyet:
                    dp[i][j] = maliyet
                    kok[i][j] = r

    print("İkili arama ağacı düğümleri:")
    for dugum in dugumler:
        print(dugum)

    print(f"\nVerilen ağaç düğümleri için optimal BST'nin maliyeti {dp[0][n - 1]}.")
    ikili_arama_agacini_yazdir(kok, anahtarlar, 0, n - 1, -1, False)


def main():
    # Örnek bir ikili arama ağacı
    dugumler = [Dugum(i, randint(1, 50)) for i in range(10, 0, -1)]
    optimal_ikili_arama_agacini_bul(dugumler)


if __name__ == "__main__":
    main()
