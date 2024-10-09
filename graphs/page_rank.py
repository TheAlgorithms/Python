"""
Produced By: K. Umut Araz github.com/arazumut
"""

"""
Algoritma için giriş grafiği:

  A B C
A 0 1 1
B 0 0 1
C 1 0 0

"""

grafik = [[0, 1, 1], [0, 0, 1], [1, 0, 0]]


class Düğüm:
    def __init__(self, isim):
        self.isim = isim
        self.gelen = []
        self.giden = []

    def gelen_ekle(self, düğüm):
        self.gelen.append(düğüm)

    def giden_ekle(self, düğüm):
        self.giden.append(düğüm)

    def __repr__(self):
        return f"<düğüm={self.isim} gelen={self.gelen} giden={self.giden}>"


def sayfa_sıralaması(düğümler, limit=3, d=0.85):
    sıralamalar = {}
    for düğüm in düğümler:
        sıralamalar[düğüm.isim] = 1

    gidenler = {}
    for düğüm in düğümler:
        gidenler[düğüm.isim] = len(düğüm.giden)

    for i in range(limit):
        print(f"======= {i + 1}. İterasyon =======")
        for _, düğüm in enumerate(düğümler):
            sıralamalar[düğüm.isim] = (1 - d) + d * sum(
                sıralamalar[gelen] / gidenler[gelen] for gelen in düğüm.gelen
            )
        print(sıralamalar)


def ana():
    isimler = list(input("Düğümlerin İsimlerini Girin: ").split())

    düğümler = [Düğüm(isim) for isim in isimler]

    for ri, satır in enumerate(grafik):
        for ci, sütun in enumerate(satır):
            if sütun == 1:
                düğümler[ci].gelen_ekle(isimler[ri])
                düğümler[ri].giden_ekle(isimler[ci])

    print("======= Düğümler =======")
    for düğüm in düğümler:
        print(düğüm)

    sayfa_sıralaması(düğümler)


if __name__ == "__main__":
    ana()
