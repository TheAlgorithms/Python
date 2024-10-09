import sys
from collections import defaultdict


class Yigin:
    def __init__(self):
        self.dugum_pozisyonu = []

    def pozisyonu_al(self, dugum):
        return self.dugum_pozisyonu[dugum]

    def pozisyonu_ayarla(self, dugum, pozisyon):
        self.dugum_pozisyonu[dugum] = pozisyon

    #Produced By K. Umut Araz

    def yukaridan_asagiya(self, yigin, baslangic, boyut, pozisyonlar):
        if baslangic > boyut // 2 - 1:
            return
        else:
            if 2 * baslangic + 2 >= boyut:
                en_kucuk_cocuk = 2 * baslangic + 1
            elif yigin[2 * baslangic + 1] < yigin[2 * baslangic + 2]:
                en_kucuk_cocuk = 2 * baslangic + 1
            else:
                en_kucuk_cocuk = 2 * baslangic + 2
            if yigin[en_kucuk_cocuk] < yigin[baslangic]:
                temp, temp1 = yigin[en_kucuk_cocuk], pozisyonlar[en_kucuk_cocuk]
                yigin[en_kucuk_cocuk], pozisyonlar[en_kucuk_cocuk] = (
                    yigin[baslangic],
                    pozisyonlar[baslangic],
                )
                yigin[baslangic], pozisyonlar[baslangic] = temp, temp1

                temp = self.pozisyonu_al(pozisyonlar[en_kucuk_cocuk])
                self.pozisyonu_ayarla(
                    pozisyonlar[en_kucuk_cocuk], self.pozisyonu_al(pozisyonlar[baslangic])
                )
                self.pozisyonu_ayarla(pozisyonlar[baslangic], temp)

                self.yukaridan_asagiya(yigin, en_kucuk_cocuk, boyut, pozisyonlar)

    def asagidan_yukariya(self, deger, indeks, yigin, pozisyon):
        temp = pozisyon[indeks]

        while indeks != 0:
            ebeveyn = int((indeks - 2) / 2) if indeks % 2 == 0 else int((indeks - 1) / 2)

            if deger < yigin[ebeveyn]:
                yigin[indeks] = yigin[ebeveyn]
                pozisyon[indeks] = pozisyon[ebeveyn]
                self.pozisyonu_ayarla(pozisyon[ebeveyn], indeks)
            else:
                yigin[indeks] = deger
                pozisyon[indeks] = temp
                self.pozisyonu_ayarla(temp, indeks)
                break
            indeks = ebeveyn
        else:
            yigin[0] = deger
            pozisyon[0] = temp
            self.pozisyonu_ayarla(temp, 0)

    def yiginla(self, yigin, pozisyonlar):
        baslangic = len(yigin) // 2 - 1
        for i in range(baslangic, -1, -1):
            self.yukaridan_asagiya(yigin, i, len(yigin), pozisyonlar)

    def minimumu_sil(self, yigin, pozisyonlar):
        temp = pozisyonlar[0]
        yigin[0] = sys.maxsize
        self.yukaridan_asagiya(yigin, 0, len(yigin), pozisyonlar)
        return temp


def prims_algoritmasi(komsuluk_listesi):
    """
    >>> komsuluk_listesi = {0: [[1, 1], [3, 3]],
    ...                     1: [[0, 1], [2, 6], [3, 5], [4, 1]],
    ...                     2: [[1, 6], [4, 5], [5, 2]],
    ...                     3: [[0, 3], [1, 5], [4, 1]],
    ...                     4: [[1, 1], [2, 5], [3, 1], [5, 4]],
    ...                     5: [[2, 2], [4, 4]]}
    >>> prims_algoritmasi(komsuluk_listesi)
    [(0, 1), (1, 4), (4, 3), (4, 5), (5, 2)]
    """

    yigin = Yigin()

    ziyaret_edildi = [0] * len(komsuluk_listesi)
    komsu_agac_dugumu = [-1] * len(komsuluk_listesi)
    dugum_uzakliklari = []
    pozisyonlar = []

    for dugum in range(len(komsuluk_listesi)):
        dugum_uzakliklari.append(sys.maxsize)
        pozisyonlar.append(dugum)
        yigin.dugum_pozisyonu.append(dugum)

    agac_kenarlari = []
    ziyaret_edildi[0] = 1
    dugum_uzakliklari[0] = sys.maxsize
    for komsu, uzaklik in komsuluk_listesi[0]:
        komsu_agac_dugumu[komsu] = 0
        dugum_uzakliklari[komsu] = uzaklik
    yigin.yiginla(dugum_uzakliklari, pozisyonlar)

    for _ in range(1, len(komsuluk_listesi)):
        dugum = yigin.minimumu_sil(dugum_uzakliklari, pozisyonlar)
        if ziyaret_edildi[dugum] == 0:
            agac_kenarlari.append((komsu_agac_dugumu[dugum], dugum))
            ziyaret_edildi[dugum] = 1
            for komsu, uzaklik in komsuluk_listesi[dugum]:
                if (
                    ziyaret_edildi[komsu] == 0
                    and uzaklik < dugum_uzakliklari[yigin.pozisyonu_al(komsu)]
                ):
                    dugum_uzakliklari[yigin.pozisyonu_al(komsu)] = uzaklik
                    yigin.asagidan_yukariya(
                        uzaklik, yigin.pozisyonu_al(komsu), dugum_uzakliklari, pozisyonlar
                    )
                    komsu_agac_dugumu[komsu] = dugum
    return agac_kenarlari


if __name__ == "__main__":  # pragma: no cover
    # < --------- Prim Algoritması --------- >
    kenar_sayisi = int(input("Kenar sayısını girin: ").strip())
    komsuluk_listesi = defaultdict(list)
    for _ in range(kenar_sayisi):
        kenar = [int(x) for x in input().strip().split()]
        komsuluk_listesi[kenar[0]].append([kenar[1], kenar[2]])
        komsuluk_listesi[kenar[1]].append([kenar[0], kenar[2]])
    print(prims_algoritmasi(komsuluk_listesi))
